import pymongo
import datetime
from cheker import compute_cosine_similarity
import file_utilities


client = pymongo.MongoClient('localhost', 27017)

def insert_document(collection, data):
    return collection.insert_one(data).inserted_id

def find_document(collection, elements, multiple=False):
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)

def update_document(collection, query_elements, new_values):
    collection.update_one(query_elements, {'$set': new_values})

def delete_document(collection, query):
    collection.delete_one(query)

def create_dict_collections(Name: str,name_of_article: str, Link, spisok):
    return {"Author": Name,"Article": name_of_article,"link": Link, "Plagiats": spisok}

db = client["Antiplagiat"]

series_collection1 = db["plagiat"]

def mongo_collections(i: int, spisok):
    for j in range(i):
        if find_document(series_collection1, {"Author": spisok[j][0], 'Article': spisok[j][1][:-3]}) == None:
            with open(spisok[j][1], 'r') as f:
                temp = f.read()
            insert_document(series_collection1, create_dict_collections(spisok[j][0],
                                spisok[j][1][:-3],temp, []))
        else:
            with open(spisok[j][1], 'r') as f:
                temp = f.read()
            update_document(series_collection1,{"Author": spisok[j][0], 'Article': spisok[j][1][:-3]},
            create_dict_collections(spisok[j][0],spisok[j][1][:-3],temp, []))
    all = []
    a = series_collection1.find()
    for data in a:
        all.append(data)
    for i in range(len(all)):
        plagi = []
        for j in range(len(all)):
            if (compute_cosine_similarity(file_utilities.preprocess_code(all[i]["link"]), file_utilities.preprocess_code(all[j]["link"]))) >= 0.5 and i != j:
                plagi += [{"Time": str(datetime.datetime.today())[:-7], "_id": all[j]["_id"],
                           "Prosent": compute_cosine_similarity(file_utilities.preprocess_code(all[i]["link"]), file_utilities.preprocess_code(all[j]["link"])) * 100}]
        update_document(series_collection1, {"_id": all[i]["_id"]},
                        {"Plagiats": plagi})


def insert_plagiats(collections,file,author: str):
    with open(file,"r") as f:
        temp = f.read()
    all = []
    a = collections.find()
    for data in a:
        all.append(data)
    plag = []
    id = insert_document(collections, create_dict_collections(author, file[:-3], temp, plag))
    for i in range(len(all)):
        if compute_cosine_similarity(file_utilities.preprocess_code(all[i]["link"]), file_utilities.preprocess_code(temp)) >= 0.50:
            update_document(collections,{"_id": all[i]["_id"]},{"Plagiats": all[i]["Plagiats"] +
                            [{"Time": str(datetime.datetime.today())[:-7], "_id": id,
                           "Prosent": compute_cosine_similarity(file_utilities.preprocess_code(all[i]["link"]), file_utilities.preprocess_code(temp)) * 100}]})
            plag += [{"Time": str(datetime.datetime.today())[:-7], "_id": all[i]["_id"],
                           "Prosent": compute_cosine_similarity(file_utilities.preprocess_code(all[i]["link"]), file_utilities.preprocess_code(temp)) * 100}]

    update_document(collections,{"_id": id},{"Plagiats": plag})




