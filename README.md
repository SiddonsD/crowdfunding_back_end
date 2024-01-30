# Crowdfunding Back End
 Link to deployed project [**AccessAid**](https://crowdfunding-back-end-siddonsd.fly.dev/projects/)

## Project Requirements
- [ ] Be separated into two distinct projects: an API built using the Django RestFramework and a website built using React.
- [ ] Have a cool name, bonus points if it includes a pun and/or missing vowels.
- [ ] Have a clear target audience.
- [ ] Have user accounts. A user should have at least the following attributes:
  - Date created
  - Username
  - Email address
  - Password
- [ ] Ability to create a “project” to be crowdfunded which will include at least thefollowing attributes:
   - Date created
   - Title
   - Owner (a user)
   - Description
   - Image
   - Target amount to fundraise
   - Whether it is currently open to accepting new supporters or not
   - When the project was created
- [ ] Ability to “pledge” to a project. A pledge should include at least the followingattributes:
   - Date created
   - An amount
   - The project the pledge is for
   - The supporter/user (i.e. who created the pledge)
   - Whether the pledge is anonymous or not
   - A comment to go along with the pledge
- [ ] Implement suitable update/delete functionality, e.g. should a project owner be allowed to update a project description?
- [ ] Implement suitable permissions, e.g. who is allowed to delete a project?
- [ ] Return the relevant status codes for both successful and unsuccessful requeststo the API.
- [ ] Handle failed requests gracefully (e.g. you should have a custom 404 pagerather than the default error page).
- [ ] Use Token Authentication.
- [ ] Implement responsive design.

## Planning:

### AccessAid
AccessAid is a platform dedicated to improving accessibility for people with disabilities.

Accessibility accommodations can be costly making self-funding prohibitive for many individuals. Additionally, opportunities for funding supports through Government programs such as NIDS or through private sector initiatives are limited and/or subject to lengthy approval processes.

AccessAid was born to empower differently abled individuals by enabling timely access to funding for accommodations and supports of their choice, bridging the gap between need and mainstream support options. We believe everyone with a disability should be able to live the life they want with the accommodation supports they choose.

Crowdfunding through AccessAid may include funds for assistive equipment, prosthetic devices, accessible technology, environmental modifications or education and awareness campaigns.

### Intended Audience/User Stories
AccessAid is for differently abled individuals who need accessibility support, people caring for individuals who need supports, and community groups who support differently abled individuals.

### Front End Pages/Functionality
**Home Page**
- Register new user
- Create a new project
- View open crowdfunding projects
- Filter/order crowdfunding projects by:
  - Date created
  - Target raised
  - Number of pledges
  - Most recent pledge

**Project Page**
- Edit a project (if logged in and authenticated as project owner)
- Make a pledge (if logged in and authenticated as user)
- View project pledges and comments
- View number of pledges
- View total of pledges

**Pledge Page**

**User Page**

**404 Page**

## Screenshots of Insomnia
**GET Method**

Returns a list of users
![A screenshot in Insomnia demonstrating a successful GET method endpoint for crowdfunding app AccessAid](https://github.com/SiddonsD/crowdfunding_back_end/blob/main/crowdfunding_GET_users.PNG)

Returns details of a specific user (must be logged in as authenticated user)
![A screenshot in Insomnia demonstrating a successful GET method endpoint for crowdfunding app AccessAid](https://github.com/SiddonsD/crowdfunding_back_end/blob/main/crowdfunding_GET_user%20id.PNG)

**POST Method**

Create a new project
![A screenshot in Insomnia demonstrating a successful POST method endpoint for crowdfunding app AccessAid](https://github.com/SiddonsD/crowdfunding_back_end/blob/main/crowdfunding_POST_create%20new%20user.PNG)

**PUT Method**

Change password (must be logged in as authenticated user)
![A screenshot in Insomnia demonstrating a successful PUT method endpoint for crowdfunding app AccessAid](https://github.com/SiddonsD/crowdfunding_back_end/blob/main/crowdfunding_PUT_password%20change%20new%20token.PNG)

Edit user profile (must be logged in as authenticated user)
![A screenshot in Insomnia demonstrating a successful PUT method endpoint for crowdfunding app AccessAid](https://github.com/SiddonsD/crowdfunding_back_end/blob/main/crowdfunding_PUT_profile%20update.PNG)

**Auth Token**

Auth token returned with correct login credentials
![A screenshot in Insomnia demonstrating a successful Auth Token issued for crowdfunding app AccessAid](https://github.com/SiddonsD/crowdfunding_back_end/blob/main/crowdfunding_POST_auth%20token.PNG)

## API Spec

| URL | HTTP Method | Response | Success Response Code | Authentication/Authorisation |
| ------------------ | :-----------: | ---------------------------------- | :------------: | ---------------------------- |
|*/api-token-auth/*|**POST**|User object. Get auth token|**200**|None required|
|*/projects/*|**GET**|Returns list of Project objects|**200**|None required|
|*/projects/*|**POST**|Create a new Project entry|**201**|Must be logged in / auth_token required|
|*/projects/<project_id>/*|**GET**|Returns Project detail page with id=<project_id>|**200**|None required|
|*/projects/<project_id>/*|**PUT**|Edit Project with id=<project_id>|**200**|Must be logged in / auth_token required|
|*/projects/<project_id>/*|**DELETE**|Delete Project with id=<project_id>|**200**|Must be logged in / auth_token required|
|*/projects/?is_open=True/*|**GET**|Returns list of projects with the status is_open = True|**200**|None required|
|*/projects/?order_by=date_created/*|**GET**|Returns list of projects in order of date created|**200**|None required|
|*/projects/?order_by=num_pledges/*|**GET**|Returns list of projects in order of number of pledges received|**200**|None required|
|*/projects/?order_by=recent_pledges/*|**GET**|Returns list of projects in order of recent pledge activity|**200**|None required|
|*/projects/?order_by=target_raised/*|**GET**|Returns list of projects with the status target_raised = True|**200**|None required|
|*/users/*|**GET**|Returns list of Users objects|**200**|None required|
|*/users/register/*|**POST**|Create new user|**201**|None required|
|*/users/login/*|**POST**|Login as User id=<user_id>, returns a token|**201**|None required|
|*/users/<user_id>/*|**GET**|Return User detail page with id=<user_id>|**200**|Must be logged in as User id=<user_id> / auth_token required|
|*/users/<user_id>/*|**DELETE**|Delete User with id=<user_id>|**200**|Must be logged in as User id=<user_id> / auth_token required|
|*/user/change_password/*|**PUT**|Change User password with id=<user_id>|**200**|Must be logged in as User id=<user_id> / auth_token required. On update, old auth_token deleted, new auth_token issued|
|*/user/update_profile/<user_id>/*|**PUT**| Update User detail with id=<user_id>|**200**|Must be logged in as User id=<user_id> / auth_token required|
|*/pledges/*|**GET**|Returns list of Pledge objects|**200**|None required|
|*/pledges/*|**POST**|Create a new Pledge entry|**201**|Must be logged in / auth_token required|
|*/pledges/<pledge_id>/*|**GET**|Returns Pledge detail page with id=<pledge_id>|**200**|Must be logged in / auth_token required. Must be maker of Pledge id=<pledge_id>|
|*/pledges/?order_by=date_created/*|**GET**|List of Pledge objects in order of date created.|**200**|None required|



## DB Schema
This schema allows for the necessary relationships between users, projects, and pledges. A user can own multiple projects and make multiple pledges, while a project can have multiple pledges from multiple users. 

**Detailed version can be accessed** [**here**](https://www.figma.com/proto/ixyPlzL5NSfiXpVVdhlip8/AccessAid?page-id=0%3A1&type=design&node-id=2-437&viewport=598%2C589%2C0.25&t=IZnUnY4jK78R4ytj-1&scaling=min-zoom&mode=design)
![A database diagram showing relationship between users, projects and pledges for crowdfunding app AccessAid](https://github.com/SiddonsD/crowdfunding_back_end/blob/main/AccessAid.png).

