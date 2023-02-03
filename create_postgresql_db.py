import psycopg2


# Connect to the default database (assuming it has already been created)
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

# Create a cursor object to execute SQL statements
cur = conn.cursor()
conn.autocommit = True

# Create the 'ols_data' database
cur.execute("CREATE DATABASE ols_data;")

# Commit the changes to the database
conn.commit()

# Close the cursor and the connection to the database
cur.close()
conn.close()

# Connect to the database (assuming it has already been created)
conn = psycopg2.connect("dbname=ols_data")

# Create a cursor object to execute SQL statements
cur = conn.cursor()

# Create the 'efo_terms' table
cur.execute("""
CREATE TABLE IF NOT EXISTS efo_terms (
    obo_id VARCHAR(255) PRIMARY KEY,
    label VARCHAR(1024) NOT NULL
);
""")

# Create the 'efo_synonyms' table
cur.execute("""
CREATE TABLE IF NOT EXISTS efo_synonyms (
    synonym_id serial PRIMARY KEY,
    obo_id VARCHAR(255),
    synonym VARCHAR(1024),
    FOREIGN KEY (obo_id) REFERENCES efo_terms (obo_id)
);
""")

# Create a unique index on the columns obo_id and synonym in the efo_synonyms table
cur.execute("""
CREATE UNIQUE INDEX IF NOT EXISTS efo_synonyms_unique_index 
ON efo_synonyms (obo_id, synonym);
""")

# Create the 'efo_ontology' table
cur.execute("""
CREATE TABLE IF NOT EXISTS efo_ontology (
    ontology_num serial PRIMARY KEY,
    ontology_id VARCHAR(255),
    efo_terms_obo_id VARCHAR(255),
    label VARCHAR(1024),
    FOREIGN KEY (efo_terms_obo_id) REFERENCES efo_terms (obo_id)
);
""")

# Create a unique index on the columns obo_id and synonym in the efo_synonyms table
cur.execute("""
CREATE UNIQUE INDEX IF NOT EXISTS efo_ontology_unique_index 
ON efo_ontology (ontology_id, efo_terms_obo_id);
""")

# Commit the changes to the database
conn.commit()

# Close the cursor and the connection to the database
cur.close()
conn.close()
