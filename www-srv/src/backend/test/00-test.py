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

def delete(url, data):
    """Make DELETE request. Returns response."""
    return(requests.delete(url, data=json.dumps(data), headers=headers))

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
    'password': 'eac9e8dd8575f4c7831f1f6a72607126',
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

data00 = {
    "title_es": "Test document ES 0",
    "title_en": "Test document EN 0",
    "labels_es": [{"id": "1", "label": "Label A"},
                  {"id": "2", "label": "Label B"},
                  {"id": "4", "label": "Label c"}],
    "labels_en": [{"id": "1", "label": "Label A"},
                  {"id": "3", "label": "Label B"},
                  {"id": "4", "label": "Label c"}],
    "theme_es": "Theme ES 0",
    "theme_en": "Theme EN 0",
    "description_es": "Description ES 0",
    "description_en": "Description EN 0",
    "authors": ["@iliana", "@jpperez"],
    "link_es": "Link ES 0",
    "link_en": "Link EN 0",
    "pdfs_es": [{"name": "pdf_es_1 0", "hash": "8383e83838283e838238"}, 
                {"name": "pdf_es_2 0", "hash": "8383e83838283e838238"}, 
                {"name": "pdf_es_3 0", "hash": "8383e83838283e838238"}],
    "pdfs_en": [{"name": "pdf_en_1 0", "hash": "8383e83838283e838238"}, 
                {"name": "pdf_en_2 0", "hash": "8383e83838283e838238"}, 
                {"name": "pdf_en_3 0", "hash": "8383e83838283e838238"}]
}

data01 = {
    "title_es": "Test document ES 1",
    "title_en": "Test document EN 1",
    "labels_es": [{"id": "1", "label": "Label A"},
                  {"id": "2", "label": "Label B"}],
    "labels_en": [{"id": "1", "label": "Label A"},
                  {"id": "4", "label": "Label c"}],
    "theme_es": "Theme ES 1",
    "theme_en": "Theme EN 1",
    "description_es": "Description ES 1",
    "description_en": "Description EN 1",
    "authors": ["@iliana"],
    "link_es": "Link ES 1",
    "link_en": "Link EN 1",
    "pdfs_es": [{"name": "pdf_es_1 1", "hash": "8383e83838283e838238"}, 
                {"name": "pdf_es_3 1", "hash": "8383e83838283e838238"}],
    "pdfs_en": [{"name": "pdf_en_1 1", "hash": "8383e83838283e838238"}]
}

r00 = post(root+'/document', data00)
r01 = post(root+'/document', data01)

print
print('newDocument(), POST /document')
print(jsonResponse(r00))
print(jsonResponse(r01))

# Lots of dummy documents to test lists

print
print('Creating 64 dummy documents... be patient!')

for n in range(1, 65):
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
        "pdfs_es": [{"name": "pdf_es_1 "+str(n), "hash": "8383e83838283e838238"}, 
                    {"name": "pdf_es_3 "+str(n), "hash": "8383e83838283e838238"}],
        "pdfs_en": [{"name": "pdf_en_1 "+str(n), "hash": "8383e83838283e838238"}]
    }

    post(root+'/document', data)


# Edit document: editDocument(), PUT /document

data = {
    "id_document": "2",
    "title_es": "Test document ES 3",
    "title_en": "Test document EN 3",
    "labels_es": [{"id": "1", "label": "Label A"},
                  {"id": "4", "label": "Label C"}],
    "labels_en": [{"id": "1", "label": "Label A"},
                  {"id": "3", "label": "Label B"}],
    "theme_es": "Theme ES 3",
    "theme_en": "Theme EN 3",
    "description_es": "Description ES 3",
    "description_en": "Description EN 3",
    "authors": ["@iliana", "@jpperez"],
    "link_es": "Link ES 3",
    "link_en": "Link EN 3",
    "pdfs_es": [{"name": "pdf_es_1 3", "hash": "8383e83838283e838238"}, 
                {"name": "pdf_es_2 3", "hash": "8383e83838283e838238"}],
    "pdfs_en": [{"name": "pdf_en_2 3", "hash": "8383e83838283e838238"}]
}

r = put(root+'/document', data)

print
print('editDocument(), PUT /document')
print(jsonResponse(r))


# Delete document: deleteDocument(), DELETE /document

data = {
    "id_document": "1"
}

r = delete(root+"/document", data)

print
print('deleteDocument(), DELETE /document')
print(jsonResponse(r))


# Get document: getDocumentList(), GET /document

data = {
    "offset": "1",
    "search": "",
    "orderbyfield": "title",
    "orderbyorder": "asc"
}

r = get(root+"/document", data=data)

print
print('getDocumentList(), GET /document')
print(jsonResponse(r))
