'The Pub Hub' is a full-stack application that allows students studying abroad to review the restaurants and pubs they visited during their time in Europe.
Users of the application will be able to browse students reviews of pubs and restaurants, respond to the reviews, and write reviews on their own to share
with others who will be able to plan their stay around the advice of their friends. 'The Pub Hub' is still currently in production, but I'm hoping to be finished
with the project by the end of the year.

'The Pub Hub' is a Django application which utilizes the CSS Bootstrap framework for the design of the webpage. The web application will also utilize JavaScript in 
order to make calls to the Google Places API to locate and list restaurants in a given location in Europe. JavaScript will also be utilized to create a paginator effect
for the reviews so that the home page does not get too cluttered. 

'The Pub Hub' will incorporate many features to improve the usability of the website. Users will be able to create an account and login to save their reviews and any pubs
or restaurants they enjoyed, as well as follow friends also using the application. Users will also be able to enter their location and browse restuarants/pubs and reviews
based on that location. Users will be able to sort between reviews based on their popularity, recency, as well as view reviews strictly posted by those they follow. When
writing reviews, users can optionally rate the various aspects of the restuarant/pub out of 5, such as the food, the drink, the environment, and the affordability. Then, 
users will rate the restaurant/pub out of 5, and optionally write a review and post pictures depicting your experience. When interacting with other users' reviews, users
can like a review or comment on a review. Users can also choose to follow the author of the review and view the other restaurants/pubs and locations they visited during
their time in Europe. Finally, users can search locations, users, and restaurants/pubs to make finding reviews easier. 

Currently, I'm working on a simple design of the website using the CSS Bootstrap framework. 

Unfortunately, there is no current webserver for 'The Pub Hub' application. To view the application, run the following commands in your terminal:
  1. Clone this git repository, running  the command **git clone https://github.com/wesley-lawson13/The-Pub-Hub**
  2. In your terminal, cd into the directory titled "The-Pub-Hub" and then into the "The_Pub_Hub" using the commands **cd The-Pub-Hub** and **cd The_Pub_Hub**
  3. Once in the "The_Pub_Hub" directory, run the command **python3 manage.py runserver**
  4. Copy the https address in your terminal and paste it into your web browser. 
