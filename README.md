# Data_Rep_Project2020

Student Name: Claire Nolan
Student No.: G00376464

This is the Data Representation 2020 project for student Claire Nolan (G00376464).

The aim of the project is to create a basic Flask server that has a REST API, (to perform CRUD operations), one database table and an accompanying web interface, using AJAX calls, to perform these CRUD operations.

For this project I will use my experience in the pharmaceutical industry to create a database for collecting information about tablet batches manufactured in a pharmaceutical manufacturing plant. I am basing this on a sample database available with the JMP(C) Statistical software (https://www.jmp.com/en_us/home.html) and saved in this repository as a CSV named "Tablet_Disso_Data". The aim is that a number of inputs (seven in total) in the manufacturing process can have a significant impact on the dissolution result of a tablet. While this is based on sample data it is very much a real-world example in the pharmaceutical industry.

There are a number of files saved in the repository:
1. initdb.sql - This is the description of the SQL database
2. requirements.txt - This is the catchall requirements for the Flask
3. rest_server.py - This is the basic Flask server and performs CRUD operations
4. Tablets2DAO.py - this connects to the SQL database and associated commands
5. dbconfig.py - this allows the database to ba accessed on various machines

There is also a folder called "static pages". This contains the HTML web interface. There are three HTML files. 
1. The "Home_Page.html" should be clicked first as it describes the collection of the batch data for a fictional pharmaceutical company - PharmaBusiness. 
2. Clicking into "Batch record information" on the home page brings you to the "batch_record_information.html" page which gives some general information about each of the attributes being recorded. 
3. Clicking into "create and edit batch record" on the home page brings you to the "batch_record.html" page which allows batch record data to be collected, updated, and deleted.
