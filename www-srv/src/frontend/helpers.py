# coding=UTF8

"""

Helpers for the frontend.

"""

def authorHelper(authorData, lang):
    """Gets the data of an author and returns a comprehensive analysis of them."""
    author = dict()
    author["id_author"]=authorData["id_author"]
    author["id_document"]=authorData["id_document"]

    if authorData["twitter_user"]!=None:
        author["twitter_user"]=authorData["twitter_user"]
    else:
        author["name"]=authorData["name"]
        author["position"]=authorData["position_"+lang]

    return author

def coalesce(matrix):
    """Coalesces a matrix to the first element not None."""
    for i in matrix:
        if i!=None:
            return i
    
    return None
