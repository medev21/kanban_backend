from typing import Dict, List
from .session import database
from .db_helpers import response_helper, set_object_id

# TODO: Change this collection name
category_collection = database.liststest


async def insert_category(category: dict) -> Dict:
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
