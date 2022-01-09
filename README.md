# Hoods
#### 09/01/2022   
#### By **Annalis Kirwa** 
## Description  
This is a web application that allows you to be in the loop about everything happening in your neighborhood.
From contact information of different handyman to meeting announcements or even alerts, businesses and community posts.  

## Behaviour Driven Development(BDD) 
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Register into the application | Fill in the registration form with details | Details saved, the user can log in |
| Set up a profile | Click on accounts icon and edit user profile button| The new details of the user are saved and displayed under user details |
| Find businesses in the hood | Click available hoods on the navbar and join a hood | The available business of that hood are displayed under business section |
| Find contact information | Click available hoods on the navbar | The available hoods are displayed with their various contacts person information |
| Create Posts | Click available hoods on the navbar and join a hood. Click on add a post | The recently created post is displayed under the hood's posts |  
| Change Hood | Click on the leave hood button | The user is allowed to join other hoods by having the join buttons activated |   

## Features  
As a user of Hoods web application, you will be able to:  
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.  

## Setup/Installation Requirements  
 ### To interact with the Hoods web application:
 * Have the latest version of browser installed   
 * Click on this <a href = "https://hoodkikao.herokuapp.com/">link</a> to use Hoods  
  ### To contribute to Hoods web application:  
 #### Clone the Repo  
 * Create an account on Github
* Fork the repository from Github with this <a href = "https://github.com/Annaliskirwa/_Neighborhood" >link </a>
* Clone the repository
* Open the project cloned project
####  Activate virtual environment
Activate virtual environment using python3.8 as default handler
    `virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE neighbourhood;  
    
#### Run initial Migration
    python3.8 manage.py makemigrations    
    python3.8 manage.py migrate
#### Run the app
    python3.8 manage.py runserver
    Open terminal on localhost:8000  
    
  ## Known Bugs
There are no known bugs so far
## Technologies Used  
* Python v3.8  
* HTML
* Bootstrap
* Django  
* Postgres  
* Rest APIs  
## Support and contact details
In case of any problem while interacting with the web application, reach out to me at annalis.kirwa@student.moringaschool.com
### License.
MIT Copyright (c) 2021 **[MITlicense](LICENSE)**



