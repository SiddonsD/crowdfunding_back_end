# Crowdfunding Back End
Denise Siddons

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


## API Spec

| URL | HTTP Method | Response | Success Response Code | Authentication/Authorisation |
| ------------------ | :-----------: | ---------------------------------- | :------------: | ---------------------------- |
|*/api-token-auth/*|**POST**|User object. Get auth token|**200**|None required|
|*/projects/*|**GET**|Returns list of Project objects|**200**|None required|
|*/projects/*|**POST**|Create a new Project entry|**200**|Must be logged in / auth_token required|
|*/projects/<project_id>/*|**GET**|Returns Project detail page with id=<project_id>|**200**|None required|
|*/projects/<project_id>/*|**PUT**|Edit Project with id=<project_id>|**200**|Must be logged in / auth_token required|
|*/projects/<project_id>/*|**DELETE**|                        |                |                              |
|*/projects/?is_open=True/*|**GET**|                        |                |                              |
|*/projects/?order_by=date_created/*|**GET**|                        |                |                              |
|*/projects/?order_by=num_pledges/*|**GET**|                        |                |                              |
|*/projects/?order_by=recent_pledges/*|**GET**|                        |                |                              |
|*/projects/?order_by=target_raised/*|**GET**|                        |                |                              |
|*/users/*|**GET**|                        |                |                              |
|*/users/register/*|**POST**|                        |                |                              |
|*/users/login/*|**POST**|                        |                |                              |
|*/users/<user_id>/*|**GET**|                        |                |                              |
|*/users/<user_id>/*|**DELETE**|                        |                |                              |
|*/user/change_password/*|**PUT**|                        |                |                              |
|*/user/update_profile/<user_id>/*|**PUT**|                        |                |                              |
|*/pledges/*|**GET**|                        |                |                              |
|*/pledges/*|**POST**|                        |                |                              |
|*/pledges/<pledge_id>/*|**GET**|                        |                |                              |
|*/pledges/?order_by=date_created/*|**POST**|                        |                |                              |




## DB Schema
![]
( {{ ./relative/path/to/your/schema/image.png }} )
