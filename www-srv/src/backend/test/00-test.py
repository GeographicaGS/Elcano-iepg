# coding=UTF8

import requests, json


def post(url, data):
    """Make POST request. Returns response."""
    return(requests.post(url, data=json.dumps(data), headers=headers))

def get(url, data=None):
    """Make GET request. Returns response."""
    if data:
        return(requests.get(url, headers=headers, data=json.dumps(data)))
    else:
        return(requests.get(url, headers=headers))

def delete(url, data=None):
    """Make DELETE request. Returns response."""
    if data:
        return(requests.delete(url, data=json.dumps(data), headers=headers))
    else:
        return(requests.delete(url, headers=headers))

def put(url, data):
    """Make PUT request. Returns response."""
    return(requests.put(url, data=json.dumps(data), headers=headers))

def jsonResponse(response):
    """Returns a response string."""
    return(str(response.status_code)+': '+str(response.json()))


root = 'http://localhost:5000'
headers = {'Accept': 'application/json', 'Content-type': 'application/json'}

# Create users: newUser(), POST /user

data00 = {
    'name': 'Iliana',
    'surname': 'Olivié',
    'password': 'd0209bbd86dfcc7593de226203bb10e7',
    'email': 'iolivie@rielcano.org',
    'admin': 'true',
    'username': 'iolivie',
    'language': 'es',
    'status': '1'
}

data01 = {
    'name': 'Alberto',
    'surname': 'Asuero',
    'password': 'eac9e8dd8575f4c7831f1f6a72607126',
    'email': 'alberto.asuero@geographica.gs',
    'admin': 'true',
    'username': 'alasarr',
    'language': 'es',
    'status': '1'
}

r00 = post(root+'/user', data00)
r01 = post(root+'/user', data01)

print('newUser(), POST /user')
print(jsonResponse(r00))
print(jsonResponse(r01))


# Create labels: newLabel(), POST /label/(en/es)

print
print('newLabel(), POST /label/(en/es)')

for lang in ['en', 'es']:
    for n in range(1,5):
        data = {
            'label': 'New Label '+lang.upper()+' '+str(n)
        }

        r = post(root+'/label/'+lang, data)
        print(jsonResponse(r))


# Get labels: getLabels(), GET /label/(en/es)

print
print('getLabels(), GET /label/(en/es)')

for lang in ['en', 'es']:
    r = get(root+'/label/'+lang)
    print(jsonResponse(r))


# Create document: newDocument(), POST /document
# Lots of dummy documents to test lists

print
print('Creating 32 dummy documents... be patient!')

for n in range(1, 5):
    data = {
        "title_es": "Test document ES "+str(n),
        "title_en": "Test document EN "+str(n),
        "labels_es": [{"id": "1", "label": "Label A"},
                      {"id": "2", "label": "Label B"}],
        "labels_en": [{"id": "1", "label": "Label A"},
                      {"id": "4", "label": "Label c"}],
        "theme_es": "Theme ES "+str(n),
        "theme_en": "Theme EN "+str(n),
        "description_es": "Description ES "+str(n),
        "description_en": "Description EN "+str(n),
        "authors": ["@iliana"],
        "link_es": "Link ES "+str(n),
        "link_en": "Link EN "+str(n),
        "pdfs_es": [{"name": "pdf_es_1 "+str(n), "hash": "1111"+str(n)}, 
                    {"name": "pdf_es_2 "+str(n), "hash": "2222"+str(n)}],
        "pdfs_en": [{"name": "pdf_en_1 "+str(n), "hash": "3333"+str(n)}]
    }

    post(root+'/document', data)


# Edit document: editDocument(), PUT /document

data = {
    "title_es": "Test document ES",
    "title_en": "Test document EN",
    "labels_es": [{"id": "1", "label": "Label A"},
                  {"id": "2", "label": "Label B"},
                  {"id": "4", "label": "Label c"}],
    "labels_en": [{"id": "1", "label": "Label A"},
                  {"id": "3", "label": "Label B"},
                  {"id": "4", "label": "Label c"}],
    "theme_es": "Theme ES",
    "theme_en": "Theme EN",
    "description_es": "Description ES",
    "description_en": "Description EN",
    "authors": ["@iliana", "@jpperez"],
    "link_es": "Link ES",
    "link_en": "Link EN",
    "pdfs_es": [{"name": "pdf_es_1", "hash": "8383e83838283e838238"}, 
                {"name": "pdf_es_3", "hash": "22222"}],
    "pdfs_en": [{"name": "pdf_en_1", "hash": "33332334"},
                {"name": "pdf_en_1", "hash": "33332334eer"}], 
    "published": "True"
}

r = put(root+'/document/2', data)

print
print('editDocument(), PUT /document')
print(jsonResponse(r))


# Delete document: deleteDocument(), DELETE /document

r = delete(root+"/document/1")

print
print('deleteDocument(), DELETE /document')
print(jsonResponse(r))


# # # Get document: getDocumentList(), GET /document, unfiltered

# r = get(root+"/document?offset=0&search=&orderbyfield=title&orderbyorder=asc")

# print
# print('getDocumentList(), GET /document, unfiltered')
# print(jsonResponse(r))


# # Get document: getDocumentList(), GET /document, filtered

# data = {
#     "offset": "0",
#     "search": "ES 25",
#     "orderbyfield": "title",
#     "orderbyorder": "asc"
# }

# r = get(root+"/document?offset=0&search=%C3%A9%C3%A9%20ES%2025&orderbyfield=title&orderbyorder=asc")

# print
# print('getDocumentList(), GET /document, filtered')
# print(jsonResponse(r))


# # Create highlight: createHighlight(), POST /highlight

# data={
#     "title_es": "Hightlight title ES",
#     "title_en": "Hightlight title EN",
#     "text_es": "Text ES",
#     "text_en": "Text EN",
#     "image_name_en": "image_name_en.jpg",
#     "image_name_es": "image_name_es.jpg",
#     "image_hash_en": "3452342354534534234234",
#     "image_hash_es": "3452342354534534234234",
#     "credit_img_es": "Credit IMG ES",
#     "credit_img_en": "Credit IMG EN",
#     "link_es": "Link ES",
#     "link_en": "Link EN"
# }

# r = post(root+'/highlight', data)

# print
# print('createHighlight(), POST /highlight')
# print(jsonResponse(r))
