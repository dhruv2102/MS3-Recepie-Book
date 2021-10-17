# <center>Food Corner</center>

==================== ADD IMAGE HERE

Food corner is the place for people who want to explore new recipes. 

**[View the Live project here.](https://ms3-recepie-book.herokuapp.com/)**

<br>

## Index
---
<ol> 
<li>User Experience (UX)
    <ul>
        <li> Project Goals
        <li> User Stories
        <li> Database Architecture
        <li> Wireframes
    </ul>
<li> Features
<li> Technologies Used
<li> Testing
<li> Deployment
<li> Credits
</ol>


## User Experience
---
### Project Goals
- Design a full stack application using HTML, CSSS, Javascript, Python, Flask and MongoDB
- Implement CRUD functionality with MongoDB

### User Stories
- First Time Visitor Goals
    1. User can visit the website in any device
    2. Navigate through the website easily
    3. See an overview of recipes
    4. Search recipes by category
    5. Search specific recipes
    6. Register an account
<br>
- Site Member Goals
    1. I want to share my recipes
    2. I want to edit my recipes
    3. I can see all the recipes I submitted
    4. I can delete my own recipes
    5. I can logout of my profile
    6. I can add comment on other recipes
    7. I can edit my comments on other recipes
    8. I can delete my comments on other recipes
    9. I can delete any comments on my recipes 
<br>
- Admin Goals
    1. I can add new categories for recipes
    2. I can edit categories
    3. I can delete, non-relevant categories
    4. I can delete any recipes
    5. I can edit any recipes
    6. I can edit or delete any comments

### Database Architecture
The project uses the following schema 
![Datbase schema](/static/images/readme/database.png)

### Wireframes
================= Add wireframeeessss

## Features
- Existing Features
    1. Simple design and navigation
    2. Signup, login and logout functionality
    3. Subscribed user functionality
    4. People can create their own recipes, and comment on other recipes

- Features to be added  
    1. Users can unsubscribe from subscribe list    
    2. Users can vary the serving size and the website can dynamically ad   apt    to it
    3. Metrics for admin to see what recipes are more popular
    4. Possibly upload the image or add multiple images into carousel
    5. Users can delete their profile

## Technologies Used

- Languages Used
    - [HTML](https://en.wikipedia.org/wiki/HTML5)
        - HTML was user to give structure to page and content

    - [CSS](https://en.wikipedia.org/wiki/CSS)
        - CSS was used to style the content
    
    - [Python](https://www.python.org/)
        - It provides the backend functionality
    
    - [Jquery](https://jquery.com/)
        - It is used as an alternate to javascript to provide responsiveness
    
    - [Jinja]()
        - Jinja is a templating language used to write python code in HTML

- Frameworks, Libraries and Other

    - [Git](https://git-scm.com/)
        - Git was used for version control, which helped in keeping track of changed files

    - [GitHub](https://github.com/)
        - Github was used to store and deploy the project

    - [Gitpod](https://www.gitpod.io/)
        - Gitpod was used to write code in. It is a cloud based platform 

    - [Materialize](https://materializecss.com/)
        - Materialize is used for the design the website.

    - [MobgoDB](https://www.mongodb.com/1)
        - MongoDb was used as the online database to store all the content
    
    - [Heroku](https://dashboard.heroku.com/)
        - Heroku is the cloud platform used to deploy the app

    - [Flask](https://flask.palletsprojects.com/en/1.1.x/)
        - Flask is the web framework used to provide libraries, tools and technologies for the app.

    - [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
        - Werkzeug is used for password hashing and authentication and authorization.

    - [Balsamiq](https://balsamiq.com/wireframes/)
        - Balsmiq was used to design the basic structure of the website

    - [Stack Overflow](https://stackoverflow.com/)
        - Stack overflow was used to debug code

    - [Code Institute learning platform](https://codeinstitute.net/)
        - With the help of code institute I was able to understand how to build a dynamic website with different tools

    - [Am I Responsive](http://ami.responsivedesign.is/)
        - Tool used to check how website will look across different screen  size

- Testing
    - [Jigsaw](https://jigsaw.w3.org/css-validator/validator)
        - Tool for CSS validation

    - [W3C validator](https://validator.w3.org/)
        - Tool for HTML validation

    - [Lighthouse](https://developers.google.com/web/tools/lighthouse)
        - Tool for performance, accessiblity analysis
    
    - [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/)
        - This was used to identify any gaps in responsiveness
    
    - [PEP8](http://pep8online.com/)
        - This was used to validate python code

## Testing
---
================= Add link to Testing.md

## Deployment
To deploy the project you need the following
- Github account
- Mongodb account
- Heroku account

### Clone the project
1. Log into github and go to repo https://github.com/dhruv2102/MS3-Recepie-Book
2. Click on code from the dropdown
3. Copy the IRL for the rep
4. OPen cmd prompt on you local computer and go to the repo you want to clone the project in
5. Paste the url with the glit clone command 
`git clone https://github.com/dhruv2102/MS3-Recepie-Book`

PS In order to run the file you will need to create and env.py using your own variables and by creating an account in mongo db and create matching database as documented in [database section](#database-architecture)


### Heroku Deployment

#### Requirements and Procfile
In order to deploy to heroku we need to provide it with a list of requirements. You need to follow these steps befor eyou can deploy to heorku
- In the terminal of your IDE, type `pip3 freeze --local > requirements.txt` to create the requirements file
- After this run the command `echo web: python run.py > Procfile` to create the Procfile
- The procfile needs contain the line `web: python app.py` and make sure there is no empty line after that
- Push these files into rep

#### Environment File

Create and env.py file with the following information

```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", " *unique secret key* ")
os.environ.setdefault("MONGO_URI", " *unique uri from mongo.db * ")
os.environ.setdefault("MONGO_DB", " *database name* ")
```

Add the env file to the .gitignore as you wouldn't want your database credentials in the hand of other people

#### Creating the heroku app
- Log into heroku
- Select create new app from dashboard
- Choose the app name
- Select the region closest to you
- Click `Create app`

#### Connecting to github
- From dashboard, click on the `Deploy` tab
- Locate `Deployment Method` and select Github
- In the search bar, locate your repository by name. After finding your repo click on `Connect`
- Do not click automatic deployment at the moment as without proper configurations in place deployment can give some unexpected errors
- Click on the settings tab and cick on `Reveal config vars`
- Use the following variables which are pretty similar to your environment variables

| Key           | Value               |
| ------------- |:--------------------|
| IP            | 0.0.0.0             |
| PORT          | 5000                |
| SECRET_KEY    |*Secure secret key*  |
| MONGO_URI     |mongodb+srv://*USER*:*PASSWORD*@myfirstcluster.dr4g1.mongodb.net/cocktail_hour?retryWrites=true&w=majority |
| MONGO_DBNAME  | my_receipes       |
|               |                     |

- Go back to the `Deploy` tab and you can now enable automatic deployment
- Locate `Manual Deploy` option and choose the master branch and click `Deploy Branch`
- Once the app is built, click `Open App` from the page. 

### Running Project Locally
Assuming you have cloned the project and added the environemnt file, in the command line run the command `python app.py`. This will run the app locally. 