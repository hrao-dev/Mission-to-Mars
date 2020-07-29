# Web Scraping - Mission to Mars
 A web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

<img src="https://github.com/the-Coding-Boot-Camp-at-UT/UT-MCC-DATA-PT-01-2020-U-C/raw/master/homework-instructions/12-Web-Scraping-and-Document-Databases/Instructions/Images/mission_to_mars.png" alt="Mars Mission">

## Step 1 - Scraping
  Initial scraping is done using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
  <ul>
  <li> NASA Mars News
        NASA Mars News Site is scraped and the latest News Title and Paragraph Text are collected.</li>
  <li> JPL Mars Space Images - Featured Image
        Splinter is used to navigate to the site and the image url for the current Featured Mars Image is collected.</li>
  <li> Mars Weather
       Latest Mars weather tweet is scapped from the Mars Weather twitter account page.</li>
  <li> Mars Facts
        Facts about planet mars such as  Diameter, Mass, etc. are collected from the Mars Facts webpage using Pandas.</li>
  <li> Mars Hemispheres
        High resolution images and their corresponding titles for each of Mars's hemispheres are collected from  the USGS Astrogeology site in a Python dictionary.</li>
  </ul>
  
## Step 2 - MongoDB and Flask Application
MongoDB is used in conjunction with Flask templating to create a new HTML page that displays all of the information colllected above.
