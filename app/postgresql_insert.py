import psycopg2

def insert_data_to_db(efo_terms,efo_synonyms, efo_ontology):
    # Connect to the database
    conn = psycopg2.connect("dbname=ols_data")

    # Create a cursor object to execute SQL statements
    cur = conn.cursor()

    # Insert the EFO terms into the 'efo_terms' table
    for term in efo_terms:
        cur.execute("""
        INSERT INTO efo_terms (obo_id, label)
        VALUES (%s, %s)
        ON CONFLICT (obo_id) DO NOTHING;
        """, (term['obo_id'], term['label']))

    # Insert the EFO synonyms into the 'efo_synonyms' table
    for synonym in efo_synonyms:
        cur.execute("""
        INSERT INTO efo_synonyms (obo_id, synonym)
        VALUES (%s, %s)
        ON CONFLICT (obo_id,synonym) DO NOTHING;
        """, (synonym['obo_id'], synonym['synonym']))

    # Insert the EFO ontology into the 'efo_ontology' table
    for ontology in efo_ontology:
        cur.execute("""
        INSERT INTO efo_ontology (obo_id, parent_link)
        VALUES (%s, %s)
        ON CONFLICT (obo_id,parent_link) DO NOTHING;
        """, (ontology['obo_id'], ontology['parent_link']))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and the connection to the database
    cur.close()
    conn.close()