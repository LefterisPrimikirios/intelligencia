# OLS Ontology Search #

This implementation is responsible to retrieve specific data provided by the Ontology Lookup Service repository https://www.ebi.ac.uk/ols/index
and store them in PostgreSQL Database.


## Description ##
In the app folder, there is a `main.py` module which is the starting point.

Define the bellow parameters:

start_page: The page to start accessing the data.
size: The number of items returned, up to a maximum of 500 for a single request.
page_limit: The page limitation in case you need to define a page limit (Default=100000)

Input Example:    
    {
        "start_page":1,
        "size":500,
        "page_limit":3 (optional)
    }


Output example:
    
   return {}, 200   

### Incremental updates ###
Set the parameters: `start_page` and `page_limit` accordingly to have incremental updates based on the specific number of pages to retrieve.


## How to execute ##
1. Create a virtual enviroment in ols directory:   
    python3 -m venv venv

2. Activate the venv:
    source ./venv/bin/activate

3. Install requirements.txt:
    cd app
    pip install -r requirements.txt

4. Define the required parameters in `create_postgresql_db.py` module:
    
    conn = psycopg2.connect(
        host=" ",
        database=" ",
        user=" ",
        password=" "
    )    
and execute the file to create the database with the required tables and indexes.

5. Define the requested parameters and execute the `main.py` module


