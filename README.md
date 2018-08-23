# steamPype
This python program performs web scraping on Steam to obtain public user data without an API key for those open sourced projects. This is currently a sample project I created to put my programming skills to the test.

This video showcases the function of the program:  
https://www.youtube.com/watch?v=cd3H2tUDU0Q

Features:  
pulls the following data from a steam ID profile:  
-Steam profile picture  
-Friends list: all the steam IDs on that person's friends list with  
  -their profile picture  
  -their online status  
-Games list: shows a list of all owned games with  
  -its picture  
  -how many hours has the user played the game  
-Badges: all the badges they own with  
  -the picture of each  
  -the XP earned for each  

File Breakdown:  
-the main Python file "steamPype.py" holds an object that you instantiate with the user name  
-there is a method that retrieves a list for Friends, Games, and Badges: double array list  
  -1st array is the list  
  -2nd array index 0= the name of the object  
  -2nd array index 1= image of the object  
  -2nd array index 2= the trailing info  
    -online status for friends  
    -hours played for games  
    -XP earned for badges  
-the file "controlla.py" is an example showcasing the information display utilizing tkinter  
-to initialize the GUI program, please enter the desired steam name under the "steamid" variable as a string  
-Once the program loads, it retrieves the Steam profile picture and has 3 options below for displaying friends list, games owned list, and acquired badges for that steam profile.  

Used Techniques:  
-To create flexibiltiy, i encorporated the entire web scraping tool in one file as an object in the file "steampype.py"  
-selenium is used to web scrape a website with active JavaScript. It requires a web driver which I used a headless command with Google Chrome.  
-once the HTML is imported, I exported it into BeautifulSoup to quickly extract data. I felt it was more powewrful than utilizing Selenium for HTML tag/attribute extraction.  
-once the object is instantiated, the constructor obtains the steamid from the text username. It does this by initiating a search query in steam. Once found, the steamID is concatenated for each request.  
-each method returns an array with details for each item, 2d array  
-the "controlla.py" is simply a test GUI that generates the data from the main API file. It utilizes tkinter and I added a custom theme that should be close enough to the Steam theme.  
-I used a grid system to keep adding items. For each action button, I had a frame below it destroyed and recreated to redraw the array list. Functions were used to loop through the arrays and output them with the Steam theme.  
-For every image, I retrieved it using urllib3 and displayed it using ImageTK resized.  
-For the list in the action center, I had to generate the list externally so that the images can stay in memory. Once the method was closed, it was deleting the images so I set it globally and reinitialized it upon executiion.  


Limitations:  
-Steam loads data for users dynamically. Javascript is required to load on the page before scraping data. This circumvents web scraping tools from other programs such as directly from beautiful soups. As such, I utilized the selenium tool with the chrome driver for responsiveness and compatibility. PhantomJS gave me errors. There is still delay in retreiving data.  
-I worked out most of the bugs on the test file "controlla.py". However, I have had difficulty incorporating scrolling as it is limited to selective tkinter items such as canvas.  

This requires the following:  
Python version 3.x  
(This was atleast tested on Windows 10 and 7)  
the "chromedriver.exe" for web scraping javascript with selenium + Chrome installed  
a valid steam id to test this out  
the following Python Packages not included (execute a pip):  
-pillow  
-bs4  
-selenium  
