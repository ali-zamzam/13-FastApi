"""Passing arguments to a query"""

"""FastAPI makes it easier to manage request arguments than with Flask. We will see in this part how to use dynamic 
routing and then how to pass arguments directly in a request. Finally, we'll see how FastAPI generates argument documentation."""

# ---------------------------------------------------------------------------------------------------------------------
"""Dynamic routing"""

"""Dynamic routing allows endpoints to be generated automatically."""


"""create a dynamic_routing.py and pasting the following lines into"""

from fastapi import FastAPI

api = FastAPI(title="My API")


@api.get("/")
def get_index():
    return {"data": "hello world"}


# run this:

# uvicorn dynamic_routing:api --reload

# -----------------------------------------------------------------------------------------------------------------
"""We are going to create a dynamic endpoint /item: we can then add an itemid to our endpoint to create a new endpoint:
"""
# Add the following lines to your dynamic_routing.py file without stopping the API


@api.get("/item/{itemid}")
def get_item():
    return {"route": "dynamic"}


"""We can now make a request on this dynamic endpoint:

Try this new endpoint with different queries"""

# curl -X GET -i http://127.0.0.1:8000/item/1

# curl -X GET -i http://127.0.0.1:8000/item/my_item


"""Replace the get_item function with the following lines
"""


@api.get("/item/{itemid}")
def get_item(itemid):
    return {"route": "dynamic", "itemid": itemid}


# curl -X GET -i http://127.0.0.1:8000/item/my_item

# output:
# {
#   "route": "dynamic",
#   "itemid": "my_item"
# }
# -----------------------------------------------------------------------------------------------------------------
"""We can have complex dynamic routes with different arguments. For instance:"""


@api.get("/item/{itemid}/description/{language}")
def get_item_language(itemid, language):
    if language == "fr":
        return {"itemid": itemid, "description": "un objet", "language": "fr"}
    else:
        return {"itemid": itemid, "description": "an object", "language": "en"}


# -----------------------------------------------------------------------------------------------------------------
"""itemid --> int"""

"""FastAPI additionally provides many ways to control the type of arguments supplied to the API. So, if we want itemid to 
be necessarily an integer, we can use annotations:"""


"""Replace the get_item function with the following lines"""


@api.get("/item/{itemid:int}")
def get_item(itemid):
    return {"route": "dynamic", "itemid": itemid}


# curl -X GET -i http://127.0.0.1:8000/item/1234

# curl -X GET -i http://127.0.0.1:8000/item/my_item

"""We notice that the second request returns a 404 error: since my_item does not correspond to an integer"""
# -----------------------------------------------------------------------------------------------------------------
"""
FastAPI does not know this route. We can have different routes that exist for the same dynamic endpoint and 
the same method if we want to take into account the different types of data."""

from fastapi import FastAPI

api = FastAPI(title="My API")


@api.get("/")
def get_index():
    return {"data": "hello world"}


@api.get("/item/{itemid:int}")
def get_item_int(itemid):
    return {"route": "dynamic", "itemid": itemid, "source": "int"}


@api.get("/item/{itemid:float}")
def get_item_float(itemid):
    return {"route": "dynamic", "itemid": itemid, "source": "float"}


@api.get("/item/{itemid}")
def get_item_default(itemid):
    return {"route": "dynamic", "itemid": itemid, "source": "string"}


# curl -X GET -i http://127.0.0.1:8000/item/1234

# {"route":"dynamic","itemid":1234,"source":"int"}

# curl -X GET -i http://127.0.0.1:8000/item/1.234

# {"route":"dynamic","itemid":1.234,"source":"float"}

# curl -X GET -i http://127.0.0.1:8000/item/my_item

# {"route": "dynamic", "itemid": "my_item", "source": "string"}


"""Note that the order in which the routes are defined matters! If we define the default path, without 
argument on the type of the data first, it is this function which will be evaluated first and which will 
return the result."""

"""if we put:"""


@api.get("/item/{itemid}")
def get_item_default(itemid):
    return {"route": "dynamic", "itemid": itemid, "source": "string"}


"""in the first place so when we run the command 
"""
# curl -X GET -i http://127.0.0.1:8000/item/1234

"""the output is string (wrong)"""

# {"route":"dynamic","itemid":"1234","source":"string"}

# -----------------------------------------------------------------------------------------------------------------
"""application exercise"""

"""To practice creating dynamic routes, we'll try creating a small API that returns information about a user 
base. This base will be represented by a list of dictionaries, presented below."""

users_db = [
    {"user_id": 1, "name": "Alice", "subscription": "free tier"},
    {"user_id": 2, "name": "Bob", "subscription": "premium tier"},
    {"user_id": 3, "name": "Clementine", "subscription": "free tier"},
]

"""The routes to be created are:

GET / returns a welcome message
GET /users returns the entire database
GET /users/userid returns all data for a user based on their id. userid should be an integer. 
If the supplied userid does not match an existing user, an empty dictionary will be returned.
GET /users/userid/name returns a user's name based on their id. userid should be an integer. 
If the supplied userid does not match an existing user, an empty dictionary will be returned.
GET /users/userid/subscription returns a user's subscription type based on their id. 
userid should be an integer"""

# user = list(filter(lambda x: x.get("user_id") == userid, users_db))[0] -->(( why [0]???????))

from fastapi import FastAPI

api = FastAPI(title="exercise")

users_db = [
    {"name": "Alice", "user_id": 1, "subscription": "free tier"},
    {"user_id": 2, "name": "Bob", "subscription": "premium tier"},
    {"user_id": 3, "name": "Clementine", "subscription": "free tier"},
]


@api.get("/")
def get_index():
    return {"greetings": "welcome"}


@api.get("/users")
def get_users():
    return users_db


@api.get("/users/{userid:int}")
def get_user(userid):
    try:
        user = list(filter(lambda x: x.get("user_id") == userid, users_db))[0]
        return user
    except IndexError:
        return {}


@api.get("/users/{userid:int}/name")
def get_user_name(userid):
    try:
        user = list(filter(lambda x: x.get("user_id") == userid, users_db))[0]
        return {"name": user["name"]}
    except IndexError:
        return {}


@api.get("/users/{userid:int}/subscription")
def get_user_suscription(userid):
    try:
        user = list(filter(lambda x: x.get("user_id") == userid, users_db))[0]
        return {"subscription": user["subscription"]}
    except IndexError:
        return {}


# -----------------------------------------------------------------------------------------------------------------
"""query string"""

"""We have seen how to pass data to the API using dynamic routing. In this part, we will see how to do it 
using query string. FastAPI makes it easy to specify which arguments can be passed via the query string. 
In the following example, we are going to define a function which can take an argument argument1. 
This argument must be passed in the query string."""


"""Replace the contents of the main.py file with the following lines"""

from fastapi import FastAPI

api = FastAPI()


@api.get("/")
def get_index(argument1):
    return {"data": argument1}


"""Run the following command to call this function"""

# curl -X GET -i http://127.0.0.1:8000/?argument1=hello%20world

"""The function has access to the data sent. Now let's try to make the same query without specifying the 
argument argument1:

Run the following command
"""
# curl -X GET -i http://127.0.0.1:8000/


"""We get a 422 Unprocessable Entity error with the following content:
"""
# {
#    "detail": [
#      {
#        "loc": ["query", "argument1"],
#        "msg": "field required",
#        "type": "value_error.missing"
#      }
#    ]
# }
"""This response therefore allows us to understand why our request failed: the argument1 field is missing."""

# -----------------------------------------------------------------------------------------------------------------
"""As with dynamic routing, Python annotations can be used to control the type of data being sent."""


@api.get("/typed")
def get_typed(argument1: int):
    return {"data": argument1 + 1}


# curl -X GET -i http://127.0.0.1:8000/typed?argument1=1234

# but this one generate error (because --> argument1: int)

# curl -X GET -i http://127.0.0.1:8000/typed?argument1=hello

# {
#   "detail": [
#     {
#       "loc": ["query", "argument1"],
#       "msg": "value is not a valid integer",
#       "type": "type_error.integer"
#     }
#   ]
# }


"""This data typing is very valuable for precisely defining the use of an API: in the Redoc interface, 
you can see very quickly which type of argument can be used for which endpoint:"""

# http://127.0.0.1:8000/redoc

# -------------------------------------------------------------------------------------------------
"""Finally, we can choose to have an optional argument. For this, we can use the Optional class from 
the typing library. However, a default value must be proposed."""

from typing import Optional


@api.get("/addition")
def get_addition(a: int, b: Optional[int] = None):
    if b:
        result = a + b
    else:
        result = a + 1
    return {"addition_result": result}


# -------------------------------------------------------------------------------------------------
"""Request body"""

"""To pass data to the API, the FastAPI library relies on the use of the BaseModel class of pydantic to explain 
the form of the request body.

We will first create an Item class inherited from the BaseModel class."""

from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    itemid: int
    description: str
    owner: Optional[str] = None


"""Here the Item class has the attributes itemid which must be an integer, description 
which must be a character string and owner which is an optional character string. We 
are going to create a route for which we will need to associate a request body containing these attributes. 
This obligation will be done using the annotations in the function definition:"""

"""Add these lines to your source file to define a route taking an Item as body"""


@api.post("/item")
def post_item(item: Item):
    return {"itemid": item.itemid}


# http://127.0.0.1:8000/docs

"""we can change the body (example owner --> int)"""

# {"itemid": 3, "description": "string", "owner": "int"}


"""We can see that the annotations given here are no longer counted as parameters 
(arguments to be specified in the query string). On the other hand, we must now specify the body of the 
request ("Request body required"). Thanks to the inheritance of the BaseModel class, we were able to 
change the interpretation of the annotation by FastAPI."""

# -------------------------------------------------------------------------------------------------
"""Run the following queries to test this route paying close attention to error codes"""

# curl -X 'POST' -i \
#   'http://127.0.0.1:8000/item'


# curl -X 'POST' -i \
#   'http://127.0.0.1:8000/item' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "itemid": 1234,
#   "description": "my object",
#   "owner": "Daniel"
# }'


# curl -X 'POST' -i \
#   'http://127.0.0.1:8000/item' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "itemid": 1234,
#   "description": "my object"
# }'


# curl -X 'POST' -i \
#   'http://127.0.0.1:8000/item' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "itemid": 12345
# }'


# curl -X 'POST' -i \
#   'http://127.0.0.1:8000/item' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "itemid": 12345,
#   "description": "my object",
#   "other": "something else"
# }'
"""that's mean we can change(owner to other because it's optional field) we can't change itemid or description"""

"""The first request returns a 422 error because it has no body. The second query has all the fields and 
therefore works fine. The third has all the required fields. The fourth returns a 422 error because it 
does not have the description field. Finally, the last works correctly. We notice that the queries work 
if we provide the non-optional fields of the Item class."""

# -------------------------------------------------------------------------------------------------
"""Change the post_item function to return the other attribute of item and rerun the last query"""


@api.post("/item")
def post_item(item: Item):
    return {"itemid": item.other}


# curl -X 'POST' -i \
#   'http://127.0.0.1:8000/item' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "itemid": 12345,
#   "description": "my object",
#   "other": "something else"
# }'


"""In this case, we get a 500 Internal Server Error error: indeed, the object of the Item class does not have an 
other attribute although it was passed in the body of the request. To be convinced, we can look at the 
console in which the API runs: AttributeError: 'Item' object has no attribute 'other'."""

# class Item(BaseModel):
# itemid: int
# description: str
# owner: Optional[str] = None

# -------------------------------------------------------------------------------------------------
"""Modify the post_item function so that it returns the item object directly"""


@api.post("/item")
def post_item(item: Item):
    return item


"""Run the following query again
"""
# curl -X 'POST' -i \
#    'http://127.0.0.1:8000/item'\
#    -H 'Content-Type: application/json'\
#    -d '{
#    "itemid": 12345,
#    "description": "my object",
#    "other": "something else"
# }'
"""
Using this BaseModel class as a parent class therefore allows a route to accept a body. We force the body of 
the request to respect a certain schema with certain values that can be optional. Moreover, the use of this 
class makes it possible to ignore fields which are not predefined. Finally, the BaseModel class makes it 
easy to return all the attributes of a request body that have been created in JSON format without needing 
to specify this definition."""

# -------------------------------------------------------------------------------------------------
"""Finally, note that we can use the typing and pydantic libraries to give more complex types to our data. 
The following example shows a use of these libraries."""

from typing import List, Optional

from pydantic import BaseModel


class Owner(BaseModel):
    name: str
    address: str


class Item(BaseModel):
    itemid: int
    description: str
    owner: Optional[Owner] = None
    ratings: List[float]
    available: bool


"""Pydantic also allows the use of "exotic" types such as http URLs, IP addresses, ... 
If you want to explore these types of data, you can go to this address."""

# https://pydantic-docs.helpmanual.io/usage/types/

# --------------------------------------------------------------------------------------------------------------------
"""application exercise_2"""

"""By using the API add the following routes:

- PUT /users creates a new user in the database and returns the data of the created user. Data about the new 
user must be provided in the body of the request.
- POST /users/userid modifies the data relating to the user identified by userid and returns the data of the 
 modified user. The user data to modify must be provided in the body of the request
- DELETE /users/userid deletes the user specified by userid and returns a deletion confirmation.

- We will choose to return an empty dictionary in the case of an internal error and we will use a User class 
inherited from BaseModel."""

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

api = FastAPI()

users_db = [
    {"name": "Alice", "user_id": 1, "subscription": "free tier"},
    {"name": "Bob", "user_id": 2, "subscription": "premium tier"},
    {"name": "Clementine", "user_id": 3, "subscription": "free tier"},
]


class User(BaseModel):
    userid: Optional[int]
    name: str
    subscription: str


@api.put("/users")
def put_users(user: User):
    new_id = max(users_db, key=lambda x: x.get("user_id"))["user_id"]
    new_user = {
        "user_id": new_id + 1,
        "name": user.name,
        "subscription": user.subscription,
    }
    users_db.append(new_user)
    return new_user


@api.post("/users/{userid:int}")
def post_users(user: User, userid):
    try:
        old_user = list(filter(lambda x: x.get("user_id") == userid, users_db))[0]

        users_db.remove(old_user)

        old_user["name"] = user.name
        old_user["subscription"] = user.subscription

        users_db.append(old_user)
        return old_user

    except IndexError:
        return {}


@api.delete("/users/{userid:int}")
def delete_users(userid):
    try:
        old_user = list(filter(lambda x: x.get("user_id") == userid, users_db))[0]

        users_db.remove(old_user)
        return {"userid": userid, "deleted": True}
    except IndexError:
        return {}


# --------------------------------------------------------------------------------------------------------------------
"""Headers"""

"""In this part, we will see how to pass data to the server via the request headers. This command can be very 
useful for passing authentication tokens or checking the type of content, the origin of the request, ... 
For this, we will be able to use the Header class of fastapi.

For example, the following function checks the value of User-Agent. This header is used to determine the 
source of a request:"""

from fastapi import FastAPI, Header

api = FastAPI()


@api.get("/headers")
def get_headers(user_agent=Header(None)):
    return {"User-Agent": user_agent}


# curl -X GET -i http://127.0.0.1:8000/headers

"""The answer should be:"""

# { "User-Agent": "curl/7.68.0" }


"""We see in this case that the User-Agent returned is the User-Agent of the browser."""

# --------------------------------------------------------------------------------------------------------------------
"""Conclusion
We have seen in this part how to pass data from the client to the server in 4 different ways:

using dynamic routing
using query strings
using the request body
using request headers"""
