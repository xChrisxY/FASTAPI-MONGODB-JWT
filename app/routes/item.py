from fastapi import APIRouter, HTTPException, status
from app.models.Item import Item
from app.models.ItemUpdate import ItemUpdate
from app.services.item import get_all_items, create_item, update_item, delete_item
from bson import ObjectId

item_router = APIRouter(prefix="/items", tags=["Items"])

@item_router.get("/", status_code=status.HTTP_200_OK, response_model=dict)
async def read_all_items():
    response_service = await get_all_items()
    if response_service is not None:
        
        return {
            "message": "success", 
            "items": response_service
        }
        
    return {"error": response_service}
        
@item_router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_new_item(item: Item):

    response_service = await create_item(item)

    if not response_service:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to create item")

    return {"message": "success", "item_id": response_service}


@item_router.put("/{item_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def update_existing_item(item_id: str, updates: ItemUpdate):

    if not ObjectId.is_valid(item_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid item ID format")
        
    updates_dict = updates.model_dump(exclude_unset=True)

    modified_item = await update_item(item_id, updates_dict)
    if modified_item == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    if modified_item is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to retrive updated item")
    
    return {"message": "success", "item": modified_item}

@item_router.delete("/{item_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_existing_item(item_id: str):
    
    if not ObjectId.is_valid(item_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid item ID format")

    result = await delete_item(item_id)
    
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    
    return {"message": "Item deleted successfully"}