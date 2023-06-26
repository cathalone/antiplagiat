import pymongo
import os
import numpy as np

# Укажите путь к папке, которую хотите открыть
path = '/Users/Home/PycharmProjects/antiplagiat/articles'

# Открываем папку с помощью метода listdir()
folder_contents = os.listdir(path)

# print(folder_contents)

# Создаём клиента в базе MongoDB
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

def create_dict_collections(Name: str,name_of_article: str, Link,spisok: list):
    return {"Author": Name,"Article": name_of_article,"link": Link, "Plagiats": spisok}

# Создаём Database в MongoDB
db = client["Antiplagiat"]
# Создаём коллекцию в Database list_Sound в MongoDB
series_collection1 = db["plagiat"]

def mongo_collections(i: int, spisok_souds):
    for j in range(i):
        if find_document(series_collection1,{'Article': folder_contents[j][:-4]}) == None:
            insert_document(series_collection1, create_dict_collections("nn",folder_contents[j][:-4], folder_contents[j],[{"Art":1},{"Min":3}]))

# Загружаем все голоса в базу MongoDB
mongo_collections(len(folder_contents),folder_contents)