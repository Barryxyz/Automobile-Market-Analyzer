# Automobile Market Analyzer
Web App that displays mock data about sales based on vehicle factors such as make, year, model to maximize profit for auto-makers

Requirements
- Must be able to help the client identify which Markets and models are most profitable
- Must be simple and easy to use, assuming that clients are not tech savy 
- Must be easily mantainable and adaptable to suit new needs or data

Design:
Deliver an application that will be able to better showcase the data to the client
- Uses a Django Website
	- A website is a pretty simple protype, and can be used by the clients simultaneously
- Includes a table 
	- Displays the data in an easier to read format than the database
- Includes a search bar 
	- Used to filter out models and countries
	- However, will not be able to filter price (a sort is needed)

Complications:
- Had trouble referencing the API so local database was used
- Need to somehow make the search bar multipurpose or make the search by model work (seach may be limited to only one field)
- Should have asked more questions about clients preferences such as mobile vs pc
- Needed more front and back communication to ensure that the right product is being built 
- More fields definitely need to be added because there is insufficient information to calculate profit

Process:
1. Created a new Django project
2. Loaded API and converted results into a .csv file using a sample size of 500
3. Imported the .csv file onto the db.sqlite3 (called 'imports') within the Django Project
4. Wrote the html file along with create model objects of imports
5. Create the table within html and a function to search through
6. Attempted to call values from the databased but failed
7. Ended up manually creating Sale objects to properly show the front end

How to run:
1. Make sure Django and Python is properly installed
2. Download repo 
3. Go into the repo
4. Go into the directory with manage.py and run 'python manage.py runserver'
5. Use the local address and make sure to include '/table' at the end of the url. The linked should be "http://127.0.0.1:8000/table/#"

How to add more fields:
- Edit models.py to include more variables
- Add a column to the database table for the field and input new data
- Go to table.html to add a column to the table on the page and pull another field within the table for loop

Future Features:
- Correctly implement the web API so that all data is displayed
- Include a sort feature in addition to search, especially useful for sales_price
- Provide a visual display which will include charts and graphs of the average and means
- Write function to calculate mean and average for specific countries and models
- Create an efficient way of importing data to database so that the sample size can be humongous to make conclusions more accurate
- More data fields may potentially be added
- Deploy the website on Heroku or some other cloud server



