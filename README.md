# Basic Network Monitor/Status Application

This application displays the status of different hosts/IPs by continuously pinging them. For 
every successful ping, the status is changed to ‘Success’ and for every unsuccessful ping, 
the status changes to ‘Failed’. So overall the user can know the actual status of each 
and every host by this app. Every unsuccessful ping follows a visual as well as audio 
feedback just for the ease of access for users.

## Installation


**For Windows:**
1. Install GitBash for windows to run linux type bash terminal, for help visit: https://git-scm.com/downloads
2. Install Python for windows, visit: https://www.python.org/
3. Install PostgreSQL, for help visit: https://www.postgresql.org/docs/9.2/app-psql.html
4. Open terminal and `cd` into the downloaded directory `Network-Status-App/testingPingWeb/fetchApp`
5. Make sure NodeJS and npm is installed. For help visit: https://www.nodejs.org/en/
6. Now run `npm install express` to install express framework.
7. Similarly install other dependencies using `npm` from `package.json` 
8. Set up the PostgreSQL database `hostinfo`(according to the Database Setup instructions) referencing the python script, 
   for reference visit : https://www.postgresql.org/
9. Now run `node index.js` 
10. Then cd into `Network-Status-App/testinPing/venv` 
11. Now on the Git Bash terminal run `python app.py` (or any Python IDE) to run the Python Script
12. Now go to `localhost:3000` from any web browser to view the home page of the app.

**For Linux/Mac:**
1. Open terminal and `cd` into the downloaded directory `Network-Status-App/testingPingWeb/fetchApp`
2. Make sure NodeJS and npm is installed. For help visit: https://www.nodejs.org/en/
3. Now run `npm install express` to install express framework.
4. Similarly install other dependencies using `npm` from `package.json` 
5. Set up the PostgreSQL database `hostinfo`(according to the Database Setup instructions) referencing the python script, 
   for reference visit : https://www.postgresql.org/
6. Now run `node index.js` 
7. Then cd into `Network-Status-App/testinPing/venv` 
8. Now on the terminal run `python app.py` (or any Python IDE) to run the Python Script
9. Now go to `localhost:3000` from any web browser to view the home page of the app.


**Database Setup**
1. Install PostgreSQL, visit: https://www.postgresql.org/ or http://www.postgresqltutorial.com/install-postgresql/
2. At the time of installation leave everything default except Username: `postgres`, Password: `1234`and Port: `5432` 
3. Run the following queries from running the PostgreSQL interactive terminal program, called psql.<br />
   `createdb hostinfo` <br />
   `psql hostinfo` <br />
   `create table details (name varchar(40), ip_address inet, status varchar(20));` <br />
4. Now, the database and table both are created, to rectify run the query `\dt;` inside psql and
   see if the name of the created table 'details' exists.
