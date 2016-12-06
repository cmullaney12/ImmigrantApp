# ImmigrantApp
A small Django application that allows the user to search through records of immigrants and insert, update, and delete records.

The main page of our application shows the list of immigrant records. 
  * To __filter__ this list, select values from the drop down boxes and click 'Filter'.
  * To __delete__ or __edit__ an entry from this list, select the corresponding option in the 'Actions' column.
  * To __add__ a new entry to the database, click the 'Create' button and select values for each field.


Prerequisites to run:
* Install [Python 3.5.2](https://www.python.org/downloads/)
* Double check that pip is installed by running `which pip`
 * If the console prints somthing starting with `which: no pip in...`, then [install pip manually here](https://pip.pypa.io/en/stable/)
* Once Pip is installed, navigate to the code directory and run `pip install -r requirements.txt` to install all dependencies for the project

If there are any issues with the automatic dependency install, you can install Django 1.10 and PyMySQL 0.7.9 by running `pip install Django==1.10.3` and `pip install PyMySQl==0.7.9`
 
To Run:
* Navigate to the root directory and run the command `python manage.py runserver`
* Find the port number for the development server in the console log and type them into your internet browser
 * By default, it should be accessable at `http://localhost:3000/`
