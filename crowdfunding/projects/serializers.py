from rest_framework import serializers
from django.apps import apps
from django.utils import timezone
from datetime import timedelta
from .models import Project, Pledge, default_end_date
from users.serializers import CustomUserSerializer

class PledgeSerializer(serializers.ModelSerializer):
    supporter_detail = CustomUserSerializer(source='supporter', read_only=True)
    
    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'
        
class PledgeDetailSerializer(PledgeSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.supporter = validated_data.get('supporter', instance.supporter)
        instance.project = validated_data.get('project', instance.project)
        instance.save()
        return instance

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    
    class Meta:
        model = apps.get_model('projects.Project')

        fields = '__all__'

# sets constraints on campaign duration for user selected dates
    def validate_start_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("The start date cannot be in the past.")
        elif value > timezone.now() + timedelta(days=45):
            raise serializers.ValidationError("The start date must be within 45 days from now.")
        return value
    
    def validate_end_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("The end date must be in the future.")
        elif value > timezone.now() + timedelta(days=90):
            raise serializers.ValidationError("The end date must be within 90 days from now.")
        return value
    
    def create (self, validated_data):
        if 'end_date' not in validated_data:
            validated_data['end_date'] = default_end_date()
        project = Project.objects.create(**validated_data)
        return project
        
class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance