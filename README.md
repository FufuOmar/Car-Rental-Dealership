<<<<<<< HEAD
# Car Rental Website
#### Description:
For my final project in CS50, I created a car rental website. This web application is designed to provide a seamless and intuitive experience for users looking to rent a car. The website offers various functionalities, including car inventory browsing, filtering based on user preferences, a detailed rental form, and a personalized rental management page.
This project uses various technologies to ensure a smooth and efficient user experience. For the front end, I used HTML, CSS, and JavaScript. HTML was used to structure the content of the web pages, CSS was employed to style the website and make it visually appealing, and JavaScript was utilized to add interactive elements and enhance user experience. Bootstrap, a popular CSS framework, was also incorporated to make the design responsive and mobile-friendly, ensuring that the website looks great on all devices.
For the backend, I chose Flask, a lightweight and flexible web framework for Python. Flask allowed me to handle HTTP requests, manage sessions, and integrate with the database effortlessly. It also provided a solid foundation for building a scalable and maintainable web application.
For the database, I used SQLite3 to store and manage all the data related to cars, rentals, and users. SQLite3 is a self-contained, serverless, and zero-configuration database engine, making it an excellent choice for this project. It allowed me to perform various CRUD (Create, Read, Update, Delete) operations using SQL commands, ensuring efficient data management.
Additionally, I utilized Jinja2 for templating, which comes integrated with Flask. Jinja2 enabled me to create dynamic web pages by embedding Python expressions into HTML. This approach helped me avoid code duplication and made the codebase more maintainable. By using Jinja2, I was able to generate HTML templates dynamically, passing data from the backend to the front end seamlessly.
This project consists of many files such as static which stores all the static content like images and CSS, Template which stores all the template HTML files which expands layout.html, so I do not need to copy paste stuff that stays the same (like the footer and navigation bar) from layout to the other pages, app.py which is the backend that uses Flask and Python to make the website function as intended, and finally cars.db which is the database which stores all the information for all the cars, and all the cars that people have rented out.
Layout.html contains all the main content that will be the same throughout all the webpages connected to this site. For example, this html file contains the header which is the navigation bar that users can press to redirect to a given page, which is always fixed on the top. It also contains the footer which just contains the website name.
Index.html is the homepage for my website. The homepage showcases a new car that we like to feature on the top of the page so it’s the first thing users see upon entering, and an option for them to rent it out. Scrolling down presents the user a redirection button to the inventory so the user is able to view the full inventory. Scrolling further down you’ll be able to see redirections to view your rentals and our contact information page.
Inventory.html is the inventory page which showcases all the cars available. On the top of the page you see another featured car which the user is able to rent out, or if you scroll down you can see our full inventory which is made out of cards with a image of the car, and all its information alongside a button for the user to press to rent it. There also a filter button for the user to fill in their preferences and see the cars that match it.
=======
# Full-Stack-Car-Rental-Dealership
A full stack car dealership website that users can use to rent cars and stores into a database.
>>>>>>> ebe8c0b5c83dcdc33354eb60665a90a00ca8f605
