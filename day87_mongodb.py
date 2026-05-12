from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://localhost:27017")
db = client["ml_db"]
collection = db["predictions"]

def log_to_collection(data):
    collection.insert_one(data)

def predict(n):
    pred = 2*n
    input_data = {
    "id": 1,
    "timestamp": datetime.datetime.now(),
    "value": n,
    "prediction": pred,
    "meta": {
        "author": "Dagaga",
        "day": 87,
    }
}
    
    log_to_collection(input_data)
    return pred

if __name__=="__main__":
    predict(100)
