import requests

def retrieve_efo_data(start_page,size,page_limit):
    # Define the base URL for the API
    base_url = "https://www.ebi.ac.uk/ols/api/ontologies/efo/terms"

    # Define the parameters for the API call
    request_params = {
        "page": start_page,
        "size": size
    }

    # Make API calls and retrieve data until all pages have been processed
    while True:       

        # Make the API call and retrieve the data
        response = requests.get(base_url, params=request_params)
        data = response.json()

        # Extract the EFO terms, synonyms, and ontology (parent links)
        efo_terms=[{'obo_id':term["obo_id"],'label':term["label"]} for term in data["_embedded"]["terms"] if term["obo_id"] is not None]
        efo_synonyms=[{'obo_id':term["obo_id"],'synonym':syn} for term in data["_embedded"]["terms"] for syn in term["synonyms"] if term["obo_id"] is not None]        
        efo_parent_links=[{'obo_id':term["obo_id"],'parent_link':term["_links"]["parents"]["href"]} for term in data["_embedded"]["terms"] if 'parents' in term["_links"]]
        
        yield efo_terms, efo_synonyms, efo_parent_links

        # Update the page number for the next API call
        request_params["page"] += 1
        
        # Check if there are no more pages or page limit is reached
        if "next" not in data["_links"] or page_limit<request_params["page"]:            
            break

def retrieve_ontology_data(efo_terms_obo_id,parent_link):

    # Define the base URL for the API
    base_url = parent_link   

    # Make the API call and retrieve the data
    response = requests.get(base_url)
    data = response.json()

    # Extract the EFO terms, synonyms, and ontology (parent links)
    term_ontology=[{'efo_terms_obo_id':efo_terms_obo_id,'ontology_id':term["obo_id"],'label':term["label"]} for term in data["_embedded"]["terms"] if term["obo_id"] is not None]        
    
    return term_ontology[0]

        

