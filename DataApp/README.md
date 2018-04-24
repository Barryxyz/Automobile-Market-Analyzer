# VandelayIndustries
Mock Technical Interview Response

Requirements:
	- Must be able to help client identify which Markets and models are most profitable
	- Must be simple and easy to use, assuming that clients are not tech savy 
	- Must be easily mantainable and adaptable to suit new needs or data

Design:
	Deliver an application that will be able to better showcase the data to the client
		-Uses a Django Website
			- A website is a pretty simple protype, and can be used by the clients simultaneously
		-Includes a table 
			- Displays the data in an easier to read format than the database
		-Includes a search bar 
			- Used to filter out models and countries
			- However, will not be able to filter price

Complications:
	- Database was referecing the local table rather than the customly created one.
	- Should have asked more questions about clients preference such as mobile vs pc
	- Needed more front and back communication to ensure that the right product is being built

Process:
	1. Created a new Django project
	2. Loaded API and converted results into a .csv file using a sample size of 500
	3. Imported the .csv file onto the db.sqlite3 within the Django Project
	4. Write the html file along with create model objects of imports
	5. Create the table within html and a function to search through

Future Features:
	-Fix that linking to the database situation
	-Include a sort feature in addition to search
	-Provide a visual display which will include charts and graphs of the average
	-Create an efficient way of importing data to database so that the sample size can be humongous to make conclusions more accurate
	-More data fields may potentially be added



