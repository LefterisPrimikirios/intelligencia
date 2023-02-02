import client as client
import postgresql_insert as postgresql_insert

def start(request):

    DEFAULT_PAGE_LIMIT=100000

    start_page = request['start_page']
    size = request['size']
    if 'page_limit' in request:
        page_limit = request['page_limit']
    else:
        page_limit=DEFAULT_PAGE_LIMIT

    for efo_terms, efo_synonyms, efo_ontology in client.retrieve_data(start_page,size,page_limit): 
        print(efo_terms)       
        postgresql_insert.insert_data_to_db(efo_terms, efo_synonyms, efo_ontology)

    return {}, 200


if __name__ == '__main__':
    start({
            "start_page":10,
            "size":500,
            "page_limit":11,
        })