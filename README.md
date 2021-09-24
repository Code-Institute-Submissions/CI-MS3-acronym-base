# Vilmantas Zaleckas
## Code Institute Second Milestone Project 
## **Acronym Base** - acronym database

Acronym database design to store and search socialmedia acronyms.

## Index

- [Strategy](#strategy)
- [Scope](#scope)
- [User Stories](#user-stories)
- [Structure](#structure)
  - [Mobile](#mobile)
  - [Tablet](#tablet)
  - [Desktop](#desktop)
- [Features](#features)
- [Design](#design)
- [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)
- [Testing](#testing)

## Strategy

* Website with collection of internet acronyms.
* Socialmedia is full of acronyms and this website is made for user to be able to look up the meanings of acronyms.
* It has search functionality and add, update and remove functionality for registered users.
* Website has user login or register features.


## Scope

Website with it's main functionallity in mind- to enamble user to quickly search the acronyms and their meanings. 
Website will have additional functionality for registered users to add new acronyms and update them as well as delete.
Page structure:
1. NavBar accross all the pages with logo and links to homepage, register or login. Registered and loggedin users will have additional buttons to view their profile and log out.
2. Main page will have search function and results being displayed bellow.
3. Add acronym button available on the main page and profile page.
4. Register page will have a form for user creation: username and password fields.
5. Login page will have form for username and password input.
6. Profile page will have a list of data entries for registered users and buttons for edditing, adding or removing entries.
7. Footer accross all the pages with developers name and links for GitHub, LinkedIn pages and email.

## User Stories
* First Time Visitor:
  * As a user I would like to have a quick way to find meanings for socialmedia acronyms.
  * As a user I would like to register on the website and have my own profile.
  * As a curious user I would like to find out more about developer or contact developer.
  * As a user I would like to add a missing acronym.
  
* Returning Visitor:
  
  * As a returning user I would like to be able to register or ligin into my profile.
  * As a returning user i would like to add a new acronym to the database.
  * As a returning user I would like to update or delete my entries.
  * As a user I would like to logout of the session.
  * As a returning user I would like to contact developer with comments, ideas or compliments.

## Structure

* Simple interface, with main feature of quick acronym look up.

### Mobile

* Base page structure accross all pages:
  * NavBar with Logo and "hamburger" drop down menu for links to register / login. Additional links for registered or loggedin users- Profile page and Logout button.
  * Footer with developers name and GitHub, LinkedIn and Email links. 
* Home Page -  Search bar with search results displayed bellow.
* My Profile page - acronym entries I have created, edit/update my acronyms button, delete acronyms button.

### Tablet

* Base page structure accross all pages:
  * NavBar with Logo and links to register / login. Additional links for registered or logedin users- Profile page and Logout button.
  * Footer with developers name and GitHub, LinkedIn and Email links. 
* Home Page -  Search bar and search results displayed bellow.
* My Profile page - acronym entries I have created, edit/update my acronyms button, delete acronyms button.

### Desktop

* Base page structure accross all pages:
  * NavBar with Logo and links to register / login. Additional links for registered or loggedin users- Profile page and Logout button.
  * Footer with developers name and GitHub, LinkedIn and Email links. 
* Home Page -  Search bar and search results displayed bellow.
* My Profile page - acronym entries I have created, edit/update my acronyms button, delete acronyms button.

## Features

### Implemented

Website is created with functionallity in mind for looking up acronyms and their meanings. 
It has simple interface, to get "job done" without any additional distractions or uneccessary pictures, as the site has to have a feel of dictionary pages.

* The NavBar will consist of Logo and navigation links. Logo Will be located on the left side of the screen and links on the right. Mobile view will shift Logo to the center and will have "hamburger" drop down menu on the left.

* Footer will have developers name and contact links for Github, LinkedIn and Mail.

* Home page will consist of search bar and search results bellow. No additional distractions, as user main purpouse of visit is to find acronym meanings, it has to be simple and quick for getting results. In Home page Navbar will have links for Home, Register and Login. Mobile version will hide these options in "Hamburger" menu. Small "+" button for adding acronyms to the database in case user cannot find one and would like to contribute.

* Register page will have input fields for username creation and password aswell as re-enter password field. "Register" button to submit the registration form, "Cancel" button to cancel registration.
Register page Navbar will have links for Home, Register and Login. Mobile version will hide these options in "Hamburger" menu. Small link for "Login" in case user has registered already.

* Login page will have a field for entering username, password and "Login" button, aswell as "Cancel" button. Navbar will have links for Home, Register and Login. Mobile version will hide these options in "Hamburger" menu.

* My profile page will list acronym entries the user has created with options to edit or delete these entries. Navbar will have links for Home, My Profile and Logout. Mobile version will hide these options in "Hamburger" menu.

* Add Acronym page will have a form with acronym name field and meaning field, buttons to "Submit" and "Cancel".

* Confirm delete page will display a message to confirm, that user wants to delete the acronym, there will be buttons to "Confirm" or "Cancel".

* Update Acronym page will have form with prefilled Acronym Name and Meaning Fields, which he can then edit and update. Buttons to "Submit" and "Cancel".


### Enchansments For Fututre

* Have categories section to have acronyms from different areas of life.
* Have "Like" acronyms functionality.
* Email functionality for sending users their registration confirmation, login resets or updates on their acronym posts.

## Design

Page design accross all the pages will consist of black and white theme with some gray fields to stand out in white background. The idea is to have similar look of physical dictionary page.
Logo will be basic and clear- "Acronym Base", hilighting it with typewritter fonts. All text and buttons will be plain and simple. 

* Logo - "Acronym Base" will have stronger look comparing to other fonts used in page, it will have typewriter style font to express the idea that page is all about text and is designed to have similar feel to physical dictionary page. Light gray background with black text fonts.

* Footer will have same look as Navbar, will be gray and white, simple text with year and developers name on the left side and icons for Github, LinkedIn and Email on the right side.

* Search Bar will be basic and will draw users attention by being placed in upper center of the main page, just bellow the NavBar. Will have searchglass icon and reset search entry button on the side.

* Search results will be shown in cards format with acronym names, it's meanings and contibutors username.

* Registration page - will have simple form for username and two fields for password and password confirmation. Header "Register" at the top left of the page for letting user know that they are in registration page.
All is centered on the page. With a submit button bellow. 

* Login page will look similar to registration page, with header "Login" and username, password input boxes. Button confirming login bellow.

* My profile page will have all current user entries displayed in rows with edit and delete buttons on the right side. Edit and delete buttons bellow each entry. "Admin" functionality will display all acronyms entered by different users, it will also display usernames.

* Colours - website will mainly consist of white background and black text, with light grey colors for Navbar, footer, acronym cards and forms to login, register, add or edit acronym. Delete and cancel buttons will have light red colour to attrackt users attention, but not overwhelm the overal light feel of the site. Submit, register and login buttons will have a light green colour. Flash messages shown at the top of the page to communicate with the user and their interactions will have slightley more solid Teal colour to catch users attention and inform him if there was mistake with an entry or entry was successful. Colours used:
  * White for background.
  * Black for text.
  * Gray #f5f5f5 for Navbar and Footer, slightly darken than cards gray to match the rest of the page but also to hilight the the top and bottom areas of the page.
  * Gray #fafafa for the cards and forms content background, to have a mild contrast with white background.
  * Light red #ef5350 to gentley draw users attention for important actions like cancel, reload or delete, without overwhelming the light view of the page and content.
  * Light green #66bb6a for submit, register, login and add acronym buttons. Matching overal light colour pallet.
  * Light Teal #26a69a colour, the strongest colour of all to catch users attention for important flash messages. 

  ### Typography

  Only two types of Google fonts has been used:
    * Special Elite - used only for logo, to add a special, stronger typwriter feel. It is easy to read, also suits perfectly for typwriter logo font idea.
    * Public Sans - font used for the rest of body and accross all elements of website. It has very conventional look, easy to read, but also has a hint of unique feel.

  ## Wireframes

  