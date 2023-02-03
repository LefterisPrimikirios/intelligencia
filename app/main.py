import client
import postgresql_insert

def start(request):

    DEFAULT_PAGE_LIMIT=100000

    start_page = request['start_page']
    size = request['size']
    if 'page_limit' in request:
        page_limit = request['page_limit']
    else:
        page_limit=DEFAULT_PAGE_LIMIT
    
    for efo_terms, efo_synonyms, efo_parent_links in client.retrieve_efo_data(start_page,size,page_limit): 
        efo_terms_ontology=[]
        print(efo_terms)
        for link in efo_parent_links:
            efo_terms_ontology.append(client.retrieve_ontology_data(link['obo_id'],link['parent_link']))
        print(efo_terms_ontology)
        postgresql_insert.insert_data_to_db(efo_terms, efo_synonyms, efo_terms_ontology)

    return {}, 200


if __name__ == '__main__':
    start({
            "start_page":1,
            "size":50,
            "page_limit":5,
        })