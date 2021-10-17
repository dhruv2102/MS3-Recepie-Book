# <center>TESTING</center>

## Index
- [Code Validators](#code-validators)
- [Resposiveness](#responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Testing User Stories](#testing-user-stories)
- [Bugs](#bugs)

## Code Validators
1. HTML Validator
    - With using the html5 validator I got the following error. On inspection I found these errors were caused by Jinja
    ![html error 1](/static/images/testing/html/html1.png)
    ![html error 2](/static/images/testing/html/html2.png)
2. CSS Validator
    - All tests passed for the CSS file
     ![css passed tests](/static/images/testing/css/css.png)
3. Python Validator
    - app.py is pep8 compliant
     ![pep8](/static/images/testing/pep8/python.png)

## Responsiveness
The resposiveness of the website is checked via Chrome developer tools and R
    - The site is reposive across all screens. 
    - Devices used to test are
        - Desktop: 1024px, 1366px, 1440px, 1600px and 1680px
        - Mobile and Tablet:  Galaxy S5, iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 plus, iPhone x, iPad and iPad Pro
    - All the links work as they are expected

## Browser Compatibility
The website works on google chrome, safari, mozilla firefox and edge

## Testing User Stories
- First Time Visitor Goals
    1. User can visit the website in any device
        - The user can visit the website from all the devices
    2. Navigate through the website easily
        - User can navigate through the website easily
    3. See an overview of recipes
        - User can vist the recpip's page and see all the recipes added
    4. Search specific recipes
        - User can search for specific recipes by looking at names or specific ingredients
    5. Register an account
        - User can register for an account easily
<br>
- Site Member Goals
    1. I want to share my recipes
        - Site members can log into the website and share their creations
    2. I want to edit my recipes
        - Site members can edit their own recipes
    3. I can see all the recipes I submitted
        - On the profile page, site members can see all their recipes
    4. I can delete my own recipes
        - On the profile page site member can delete the recipes
    5. I can logout of my profile
        - Site member can easily log out from their profile
    6. I can add comment on other recipes
        - Site member can add comments on any recipes
    7. I can edit my comments on other recipes
        - Site member can edit their comments on certain recipes
    8. I can delete my comments on other recipes
        - 
    9. I can delete any comments on my recipes 
<br>
- Admin Goals
    1. I can add new categories for recipes
    2. I can edit categories
    3. I can delete, non-relevant categories
    4. I can delete any recipes
    5. I can edit any recipes
    6. I can edit or delete any comments
## Bugs