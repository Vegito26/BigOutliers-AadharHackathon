# BigOutliers-UIDAI AadharHackathon
# INTRODUCTION:

This project was made for the Aadhaar Hackathon, 2021, organized by the Unique Identification Authority of India (UIDAI).

‣ Theme: Address Update

‣ Problem Statement: Address Formatting Issue


# OBJECTIVE:
‣ Identify and remove repetitive constituents in an address, and produce a merged JSON output
 
 Eg: Bangalore P.O and Bangalore can be merged and written only as Bangalore
 
 
‣ Create an API to undertake the required address formatting 

‣ Build a user interface to simplify the usage and ease evaluation.

# TECHNOLOGIES:

The project is created with:

‣ Python 3.9

    Libraries used: pandas, numpy, flask, flask-restful, jason
     
‣ Postman 8.12.5

‣ HTML

‣ CSS

‣ JavaScript

‣ Heroku (to deploy the API)


# STEPS INVOLVED:

1) Take the user’s address on the basis of the following labels-

  ‣ Building 

  ‣ Street

  ‣ Landmark 

  ‣ Locality

  ‣ VTC

  ‣ District

  ‣ State

2) Using simple string matching, exactly similar strings are identified, and all their occurrences are removed, except for the last occurrence. The hashing algorithm is used to optimize this process as it has linear time complexity. 

3) Using an external database consisting of all the VTCs of India (reference given below) the entries made by the user are cross-checked, and if any incorrect entries have been made, they are removed. 


4) We then created a User Interface using HTML, which takes in the input from the user, generates the output and displays it in various address fields via a search functionality. 


5) To connect the entire pipeline to the User Interface, we created an API, which helps in taking raw data from the UI, bringing it to the pipeline to be processed, and then returning the formatted output to the user through the UI. 

# FLOW DIAGRAM:



![2021-10-31 (10)](https://user-images.githubusercontent.com/86941433/139588278-fe4515f4-c86e-410c-8d5c-e702054c6ea9.png)

# SPECIAL CASES HANDLED:

# REFERENCES: 
‣ Database of Addresses provided by UIDAI: https://docs.google.com/spreadsheets/d/1wkvKGYeicntmHQpTPpONNweJdeqR0f6VuYXBBaa-c3I/edit?usp=sharing

‣ Database of all VTCs in India: https://censusindia.gov.in/2011census/censusdata2k11.aspx

‣ Creating an API using Flask: https://gist.github.com/jamescalam/0b309d275999f9df26fa063602753f73

