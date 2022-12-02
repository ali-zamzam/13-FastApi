"""Improve documentation"""

"""We have seen in the previous parts that FastAPI allows you to create a data type check and to create rules as to the 
required or optional data to request an endpoint. We can thus easily generate a manifesto (/openapi.json) as well as 
an OpenAPI documentation (/docs) or ReDoc (/redoc).

However, it is interesting to organize the knowledge as well as to document the arguments."""

# ----------------------------------------------------------------------------------------------------------------------
"""Customize feature documentation"""

"""To add comments to the usage of an endpoint, we can use the function's docstring. We can also give a name to our API via 
the FastAPI class."""

from fastapi import FastAPI, Header

api = FastAPI(
    title="My API", description="My own API powered by FastAPI.", version="1.0.1"
)


@api.get("/")
def get_index():
    """Returns greetings"""
    return {"greetings": "welcome"}


"""
The name of the API, its version as well as its description have changed compared to the previous examples. 
Additionally, we can see that the GET / route now has a description straight from the function's docstring.

You can also add the name argument to the decorator to give a name to the route in OpenAPI: by default, route 
names are created from the titles of the functions used: Get Index for get_index."""


"""Change function name get_index in source code to Hello World"""


@api.get("/", name="Hello World")
def get_new_index():
    """Returns greetings"""
    return {"greetings": "welcome"}


# ----------------------------------------------------------------------------------------------------------------
"""Function body documentation"""

"""We will now see how FastAPI handles the definition of models from the BaseModel class:"""

from typing import Optional

from pydantic import BaseModel


class Computer(BaseModel):
    computerid: int
    cpu: Optional[str]
    gpu: Optional[str]
    price: float


@api.put("/computer", name="Create a new computer")
def get_computer(computer: Computer):
    """Creates a new computer within the database"""
    return computer


"""We see that the second route has been added. We also notice that Schemas have appeared. You can select 
Computer's diagram to understand how this entity is formed."""


# Replace the Computer class definition with the following lines
class Computer(BaseModel):
    """a computer that is available in the store"""

    computerid: int
    cpu: Optional[str]
    gpu: Optional[str]
    price: float


"""In the ***Schemas tab***, the Computer class description is now available."""

# *********

"""Headers can also have a description using the description argument."""


@api.get("/custom", name="Get custom header")
def get_content(
    custom_header: Optional[str] = Header(None, description="My own personal header")
):
    return {"Custom-Header": custom_header}


"""You can see in the function description that the header is documented.
"""
# ----------------------------------------------------------------------------------------------------------------
"""Organize the documentation"""

"""By default, all functions are documented in a default tab. However, you can choose to organize these 
functions into different parts. To do this, we need to specify the tags argument in the decorator."""

from fastapi import FastAPI

api = FastAPI(
    openapi_tags=[
        {"name": "home", "description": "default functions"},
        {"name": "items", "description": "functions that are used to deal with items"},
    ]
)


@api.get("/", tags=["home"])
def get_index():
    """returns greetings"""
    return {"greetings": "hello world"}


@api.get("/items", tags=["items"])
def get_items():
    """returns an item"""
    return {"item": "some item"}


"""
The functions are now distributed in different parts. The same function can be put in several parts. 
We were able to add a description for the different parts using the openapi_tags argument of the FastAPI 
class constructor.

You can also change the address of the OpenAPI and Redoc documentation using the docs_url or redoc_url 
arguments. If these arguments are passed to None, these endpoints are disabled. Finally, we can choose 
to change the address of the OpenAPI manifesto with the openapi_url argument."""

# -------------------------------------------------------------------------------------------------------------------


from fastapi import FastAPI

api = FastAPI()

data = [1, 2, 3, 4, 5]


@api.get("/data")
def get_data(index):
    return {"data": data[int(index)]}


"""Opening the OpenAPI documentation, we can see that two errors are offered. In this specific case, we can see 
that if the index value is greater than 4 or less than 0, we risk getting an IndexError type error. 
Also, if index is not an integer, we should get a ValueError there."""

# index = 6
"""
IndexError: list index out of range  """

# index = SS
"""ValueError: invalid literal for int() with base 10: 'SS'"""

"""In both cases, we get a 500: Interval Server Error type error. The error takes place in the source code of 
the application but FastAPI does not know what information is returned to the user."""

# ----------------------------------------------------------------------------------------------------------------
"""We also saw that FastAPI generated its own errors for routes not found 
(404: we can make a GET /nowhere request to be convinced) or for data formats that do not correspond to the 
defined expectations 
(422: notably through the use of annotations or classes inherited from BaseModel). """


"""We will use try-except blocks to catch Python errors and throw HTTPException with associated HTTP codes."""

from fastapi import HTTPException


@api.get("/data")
def get_data(index):
    try:
        return {"data": data[int(index)]}
    except IndexError:
        raise HTTPException(status_code=404, detail="Unknown Index")
    except ValueError:
        raise HTTPException(status_code=400, detail="Bad Type")


"""You can therefore easily change the error codes and the data returned when an error occurs. 
For the detail argument, you can give a dictionary or any other structure that can be interpreted as a JSON."""

# -------------------------------------------------------------------------------------------------------------------------------
"""create our own exceptions"""

"""Finally, if we want to modify the form of the data returned during the error, we can create our own 
exceptions and pass them in the @api.exception_handler decorator."""

import datetime

from fastapi import Request
from fastapi.responses import JSONResponse


class MyException(Exception):
    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date


@api.exception_handler(MyException)
def MyExceptionHandler(request: Request, exception: MyException):
    return JSONResponse(
        status_code=418,
        content={
            "url": str(request.url),
            "name": exception.name,
            "message": "This error is my own",
            "date": exception.date,
        },
    )


@api.get("/my_custom_exception")
def get_my_custom_exception():
    raise MyException(name="my error", date=str(datetime.datetime.now()))


"""
Let's take a little time to describe this code:
- In the first block, we define a new Exception. 
It is given the attributes name and date. In the second block, we tell FastAPI how to react when the 
exception is raised. We give a JSON type response to return, giving it a status_code and a status.
We can thus access the attributes of the request or the exception to return them in a JSON. 

- Finally the last block allows us to define a route that generates this error."""

# ----------------------------------------------------------------------------------------------------------------
"""To document the different possible errors for a given route, we can pass a dictionary containing the 
possible error codes as well as the associated descriptions."""

responses = {
    200: {"description": "OK"},
    404: {"description": "Item not found"},
    302: {"description": "The item was moved"},
    403: {"description": "Not enough privileges"},
}


@api.get("/thing", responses=responses)
def get_thing():
    return {"data": "hello world"}
