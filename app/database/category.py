from typing import Dict, Union
from .session import database
from .db_helpers import response_helper, set_object_id

# TODO: Change this collection name
category_collection = database.liststest


async def insert_category(category: dict) -> Union[Dict, bool]:
    insert_response = await category_collection.insert_one(category)
    if insert_response.acknowledged:
        new_cat_dict = await category_collection.find_one(insert_response.inserted_id)
        response_dict = dict(
            data=response_helper(new_cat_dict),
            message="Category Created",
            status=200,
        )
        return response_dict
    return False


async def edit_category(category: dict) -> Union[Dict, bool]:
    category_object_id = set_object_id(category["id"])
    update_response = await category_collection.update_one(
        {"_id": category_object_id},
        {"$set": {"title": category["title"]}},
    )
    if update_response.modified_count:
        modified_board = await category_collection.find_one({"_id": category_object_id})
        response_obj = dict(
            data=response_helper(modified_board),
            message="Category updated!",
            status=200,
        )
        return response_obj
    return False
