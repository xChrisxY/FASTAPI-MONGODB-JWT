from typing import List
from app.database.db import collection
from app.models.Item import Item
from bson import ObjectId

def serialize_item(item):
    item["_id"] = str(item["_id"])
    return item

async def get_all_items():

    try:
        items = await collection.find().to_list(100)
        serialized_items = [serialize_item(item) for item in items]

        return serialized_items
    except Exception as e:
        return str(e)

async def create_item(item: Item):
    try:
        result = await collection.insert_one(item.model_dump(exclude_unset=True, exclude_none=True))
        return str(result.inserted_id)
    except Exception as e:
        return str(e)
        
    
async def update_item(item_id: str, update_item: dict):
    try:
        
        result = await collection.update_one({"_id": ObjectId(item_id)}, {"$set": update_item})
        if result.matched_count == 0:
            return result

        updated_item = await collection.find_one({"_id": ObjectId(item_id)})
        new_item = {
            "_id" : str(updated_item["_id"]),
            "name": updated_item["name"],
            "description": updated_item["description"],
            "price": updated_item["price"]
        }
        
        if not update_item:
            return None

        return new_item
        
    except Exception as e:
        return str(e)

async def delete_item(item_id: str):
    
    try:
        result = await collection.delete_one({"_id": ObjectId(item_id)})
        return result.deleted_count
        
    except Exception as e:
        return str(e)