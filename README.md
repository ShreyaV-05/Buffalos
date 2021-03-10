# Team Buffalos
![add gif later](https://www.food-management.com/sites/food-management.com/files/international-food-thinkstock-promo.png)

Hi! This is our Cuisine Website Project! by p4 Buffalo during winter 2020.
# Cuisines
## Website Summary
Because our group is full of foodies, we want to show our love and appreciation for different cuisines through our website. In this website, you can look through different cuisines in three Californian cities: San Fransisco, Los Angeles, and San Diego. These cuisines will have restaurant suggestions and reviews from online sources.
There will be different restuarants information avaliable on each page sorted by location all falling under different cuisines.
# Original Plans for Website
* 3 tabs separated by place (SF, LA, SD)
* has about 6 restaurants each
* address embed to google maps
* description of type of food
* the three common cousines: Asian, Italian, Mexican
* user interactive features such as reviews, ratings, and Pick For Me option

Tabs: 
* home page
* drop down menu: 
  * san diego cuisine
  * san diego reviews
  * los angeles cuisine
  * los angeles reviews
  * san fran cuisine
  * san fran reviews
* Pick for me
* coming soon
* reviews form


# Current Pages in our website
Our current web pages on the running site include:
* Home
* Restaurant pages and their respective reviews page
* pick for me
* coming soon
* reviews form
* easter egg/blind tic-tac-toe
# Technicals achieved
| Author| Contributions/Technicals |
| -------- | ----------- |
|Andrea| CRUD database (coming soon page), rest/web api (pick for me! tab), San Diego Restaurant page |
|Diane| Raspberry Pi/deployment (site deployed and running), Tic-Tac-Toe that leads to easter egg, drop-down menu, web page design (LA, SF, Easter Egg, Home)|
|Shreya| Database, Review Form, Review Pages for SD, LA,SF restaurants, LA Restaurant page |


## Authors
* Andrea Abed
* Diane Tang
* Shreya Vasant
* 
## Links
* [Project Plan](https://docs.google.com/document/d/1dLMqnZHEYWIKWwu43sF4bD4V1O_2SbfBQtig9rhmOKI/edit?usp=sharing)
* [GitHub Repos](https://github.com/ShreyaV-05/Buffalos/blob/main/README.md)
* [College Board Requirements](https://apcentral.collegeboard.org/pdf/ap-computer-science-principles-course-and-exam-description.pdf?course=ap-computer-science-principles)
* 
# February 19: Project Review
|Tab  |Link to Code |
| --- |           ---           |
|Diane's Ticket: College Board Requirements (Easter Egg)| https://github.com/ShreyaV-05/Buffalos/blob/main/templates/easteregg.html|
|Navigation Bar to take to seperate tabs| Navigation Bar: https://github.com/ShreyaV-05/Buffalos/blob/main/templates/base.html, https://github.com/ShreyaV-05/Buffalos/blob/main/templates/home.html Homepage link: https://github.com/ShreyaV-05/Buffalos/blob/main/templates/home.html Restaurant base: https://github.com/ShreyaV-05/Buffalos/blob/main/templates/restaurantbase.html Base: https://github.com/ShreyaV-05/Buffalos/blob/main/templates/base.html|
|Shreya's Ticket: Login/Signup Tabs (Worked on create aspect but the rest is underway)| Code for login html:https://github.com/ShreyaV-05/Buffalos/blob/ad84d45a6a9a3713e6e052f962d4b71c0d477f27/templates/login.html#L1-L49 Code for Signup html:https://github.com/ShreyaV-05/Buffalos/blob/ad84d45a6a9a3713e6e052f962d4b71c0d477f27/templates/auth_user.html#L1-L51 Code for the backend (folders):https://github.com/ShreyaV-05/Buffalos/tree/main/models |
|Shreya's Ticket: Response Form (type in a review for a restuarant (only SD restuarant's in because playing with code that will display it))| html code:https://github.com/ShreyaV-05/Buffalos/blob/ad84d45a6a9a3713e6e052f962d4b71c0d477f27/templates/responserev.html#L1-L124 backend (link to folder with multiple .py files):https://github.com/ShreyaV-05/Buffalos/tree/main/resprev |
|Shreya's Ticket: Rating| html frontend layout (will have three seperate review pages for each location):https://github.com/ShreyaV-05/Buffalos/blob/ad84d45a6a9a3713e6e052f962d4b71c0d477f27/templates/rating.html#L1-L297 backend code (for the San Diego Code (playing around and unfinished therefore not in website):https://github.com/ShreyaV-05/Buffalos/blob/ad84d45a6a9a3713e6e052f962d4b71c0d477f27/templates/SDREV.html#L40-L59 |
|Andrea's Ticket: Coming Soon Page (CRUD)| frontend form: https://github.com/ShreyaV-05/Buffalos/blob/main/templates/coming_soon.html, establishing table and creating database: https://github.com/ShreyaV-05/Buffalos/blob/main/app.py#L63-L84, showing old items and adding items into table: https://github.com/ShreyaV-05/Buffalos/blob/main/app.py#L246-L268|
|Andrea's Ticket: "Pick Me!" (Includes web api)| form for interactive button: https://github.com/ShreyaV-05/Buffalos/blob/main/templates/random.html#L187-L192, backend for web api: https://github.com/ShreyaV-05/Buffalos/blob/main/app.py#L167-L177, creating wheel for the cuisines (as recommended by crossover team): https://github.com/ShreyaV-05/Buffalos/blob/main/templates/random.html#L197-L237|
|Diane's Ticket: Restuarants Drop Down Menu| Navigation Bar: https://github.com/ShreyaV-05/Buffalos/blob/main/templates/base.html, https://github.com/ShreyaV-05/Buffalos/blob/main/templates/home.html Homepage link: https://github.com/ShreyaV-05/Buffalos/blob/main/templates/home.html Restaurant base: https://github.com/ShreyaV-05/Buffalos/blob/main/templates/restaurantbase.html Base: https://github.com/ShreyaV-05/Buffalos/blob/main/templates/base.html|
|Los Angeles Tab|Frontend Code:https://github.com/ShreyaV-05/Buffalos/blob/ad84d45a6a9a3713e6e052f962d4b71c0d477f27/templates/losangeles.html#L1-L145 |
|Future Plans| For the dashboard that each user has we will use coding similar to what our crossover group had for the evaluation pages but instead allowing the user to rate favorite restuarants and rank by prices. Here is a link to their code that we have been looking over at: https://github.com/LordRoop/P4-Ducks/blob/6d677c0c39cd48fde398a158b4cb150c2232b675/templates/math.html#L66-L278 |
# February 17: Cross-over Grading
|Requirements|Comments|
|---| --- |
|Clone, Run, Code Organization: 5/5| Code looks very organized. All pages of the code are in folders and were easy to find. Their code runs correctly and smoothly. Everyone is able to clone the code from GitHub and contribute to the project.|
|Idea, Visuals, HTML, CSS, JS: 5/5| Pages look very polished. The text and images are all organized into different sections and those sections are defined by the rectangle backgrounds. The website is easy to follow and navigate.|
|Routes, Model Code & CRUD: 4/5| Crud UI fully in place. Looks nice, but can only create/add cuisines. No function to read or delete yet. Routes added and can navigate to all pages.  |
|Easter Egg: 3/3| Implemented very well. Goes over College Board requirements as well as who am I requirements. Funny how the button linking to the easter egg was “Buffalo Wild Wings” since their group is named Buffalos.|
|Project WOW: 2/2| RNG restaurant generator wow chooses a restaurant for you. UI is very polished and professional.|
|Individual Participation (Tickets/Completions 2 pts, GitHub Heatmap 2 pts, WOW presence in group 1 pt): Andrea A. 5/5; Shreya V 5/5; Diane T 5/5| Ample evidence of full group participation. Each member was knowledgeable on their own tickets and what needed to be done in the future to improve the website. The heat map on GitHub showed their contributions |
|Total: 24/25 | Group score:19 /20|
|Recommendations for enhancements | Need to work on updating and deleting from the database. They should also change the background colour for their random restaurant chooser to a more vibrant green or blue. They can also work on how they present the result of the random restaurant. For example, they can add a wheel to get a random spin so it is more appealing to the users. |


# January 15 - Big Tickets
|Big Tickets   |Assigned To   |Description   |Grade   |
|---|---|---|---|
|Ticket 1: Response form    |Shreya   |Link to folder with all pages relating to code: https://github.com/ShreyaV-05/Buffalos/tree/main/resprev This ticket is about the response form in which the user will select a restaurant to offer a review and a rating. On the scrum board it is in the completed section (https://github.com/ShreyaV-05/Buffalos/projects/1).| 19/20  |
|Ticket 2: Recommendation page   |Andrea   |Front end html code: https://github.com/ShreyaV-05/Buffalos/blob/main/templates/recommend.html and link to back end code (still a work in progress): https://github.com/ShreyaV-05/Buffalos/blob/main/app.py#L122 (lines 122-182). This ticket is about the recommendation page (which will be a part of the nav bar) where users will be able to recommend more types of cuisines and specific restuarants they would like to see added to the website in the future. On the srum board, the front end is in the "ready to deploy column" and the back end of this page is in the "in progress" column as I am still working through errors: https://github.com/ShreyaV-05/Buffalos/projects/1#card-52937575, https://github.com/ShreyaV-05/Buffalos/projects/1#card-52937578  | 19/20  |
|Ticket 3: Drop Down Menu, Deployment (given extension due to technical errors)   |Diane   |Fixed drop-down menu (menu originally did not register when I hovered over it): https://github.com/ShreyaV-05/Buffalos/blob/main/templates/base.html, https://github.com/ShreyaV-05/Buffalos/tree/main/static. Also worked on deployment but per our discussion on Friday, I am restarting with Raspberry Pi and am still working on it over the weekend. On scrumboard, dropdown is complete: https://github.com/ShreyaV-05/Buffalos/projects/1#card-52420810.   | 18/20  |

# January 28: Ticket Plans for Week 2/1-2/5
|Tickets   |Assigned To   |Description   |Scrumboard   |
|---|---|---|---|
|Ticket 1: Review Page/ Login Page/ Sessions Ticket  |Shreya   |Changed the response form so that it shows the different restaurants that are in the website and changed all the code in the tables to reflect that(eventually will figure out how to code so that there are subcategories under cuisinesbut may not happen). Made a new tab that has the resturant names bolded and under them there are the reviews (will try to see if I can include the ratings as well so user can see what people have rated the restaurant out of 5 stars). If time work on login page frontend and start backend (or if the review page is too hard to generate within a week), which would include code for the sessions.| https://github.com/ShreyaV-05/Buffalos/projects/1#card-52455899, https://github.com/ShreyaV-05/Buffalos/projects/1#card-52914573, https://github.com/ShreyaV-05/Buffalos/projects/1#card-53776747, https://github.com/ShreyaV-05/Buffalos/projects/1#card-53804584  |
|Ticket 2: "Coming Soon" Page   |Andrea   |"Coming Soon" Page will consist of a table of cuisines that will be "coming soon" to the website. Will use meta data to be able to sort the cuisines by location (San Diego, Los Angeles, San Francisco) and possibly by the general price as well ($,$$,$$$)  | https://github.com/ShreyaV-05/Buffalos/projects/1#card-53804462  |
|Ticket 3: Easter Egg with page   |Diane   |Create a page holding exam resources such as journals, articles/sites, TPTs, slideshows. I want to try to create a secret "passageway" to the page. An idea I have right now is the search bar where if you search up "buffalos" it will direct you to the page. We are also planning on changing the searchbar to a logo/picture tab thing.   | https://github.com/ShreyaV-05/Buffalos/projects/1#card-53778656  |

# Feburary 5: Tickets and Easter Egg
| Ticket | Assigned To | Description | Link to Code | Link to Scrum Board |
| --- | --- |           ---           | --- | --- |
| Coming Soon Page | Andrea | Page with table of cuisines, user can create/add a cuisine to the list. Later will filter the data so there will be options to only view cuisines of a certain location or a certain price. | `frontend form:` https://github.com/ShreyaV-05/Buffalos/blob/main/templates/coming_soon.html<br/> `establishing table and creating database:` https://github.com/ShreyaV-05/Buffalos/blob/main/app.py#L63-L84<br/>`showing old items and adding items into table:` https://github.com/ShreyaV-05/Buffalos/blob/main/app.py#L246-L268  | https://github.com/ShreyaV-05/Buffalos/projects/1#card-53804462,     https://github.com/ShreyaV-05/Buffalos/projects/1#card-54323634 |
| Login and SignUp Page (and got Response Form to work) | Shreya | I was able to create the login and signup page. In the login page there was a way to direct to signup. The response form glitches are fixed and the page is working (though needs to be styled better in terms of color) | Login html:https://github.com/ShreyaV-05/Buffalos/commit/5813679ed8c49f04ff158df02d0f83d349073952#diff-4af836eb021bc8fe7036b64a9af9a7298b8476f6cf09ec179c7be95b9c051c30 Signup html:https://github.com/ShreyaV-05/Buffalos/commit/a5d7c0e4096a26daf49b1185a019adc0dd9a3c4f Model directory file (backend):https://github.com/ShreyaV-05/Buffalos/tree/main/models Response form html:https://github.com/ShreyaV-05/Buffalos/commit/a461c4eb06891bc400ff743f87029d15b551fb36#diff-32272cb63f3a92cb64466fe5bba7aa3b5e0822d5f472d85af26d8f61ac447c63| https://github.com/ShreyaV-05/Buffalos/projects/1#card-53776747 https://github.com/ShreyaV-05/Buffalos/projects/1#card-54340832 https://github.com/ShreyaV-05/Buffalos/projects/1#card-54340860 |
| Easter Egg/College Board page | Diane | I was able to create the easter egg page with our "I am" statememnts, links to our scrumboard, github, journals, and planning pages, and also a category for College Board requirements for the exam. I linked it to the navigation bar for now and also as an image but will be hyperlinking it as search bar later.| Easter Egg page: https://github.com/ShreyaV-05/Buffalos/blob/main/templates/easteregg.html Navigation Bar: https://github.com/ShreyaV-05/Buffalos/blob/main/templates/base.html, https://github.com/ShreyaV-05/Buffalos/blob/main/templates/home.html Homepage link: https://github.com/ShreyaV-05/Buffalos/blob/main/templates/home.html| Ticket: https://github.com/ShreyaV-05/Buffalos/projects/1#card-53778656, https://github.com/ShreyaV-05/Buffalos/projects/1#card-54352106, https://github.com/ShreyaV-05/Buffalos/projects/1#card-54305169 (WIP) |
