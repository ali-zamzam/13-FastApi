"""APIs with FastAPI"""

"""Elements of an HTTP request"""

"""The HTTP protocol is the protocol used for the Web.it allows you to ask a server to return certain data or take certain 
actions. Its secure HTTPS version is just an encrypted version of HTTP."""

"""An HTTP request is made up of different elements.

- First, there is the URI (Universal Resource Identifier). This is the address to which the request must be made. It generally consists of the protocol used, a domain name and an endpoint.

For example, the following URI http://example.org/resource might read as follows:

- http:// is the protocol used
- example.org is the domain name of the server, i.e. a simplification of the server's IP address.
- /resource is the endpoint we want to solicit

- Note that a URI can also include parameters. For example, the URI http://example.org/resource?key1=value1&key2=value2 makes 
it possible to pass the keys key1 and key2 which respectively have the values value1 and value2 to the server. 
We then speak of query string or query parameters, translated in this course by query string or query parameters.

** We must then also specify a method to request the data. The most used methods are**
- GET
- POST
- PUT
- DELETE

- A request can also contain a body. (Generally GET type requests cannot include a body). The body of a request is used to 
pass data to the request.

Finally, a request can also include headers. These headers contain the metadata relating to the request: type of data in the 
body of the request, cookies, authentication token, ...
"""
# --------------------------------------------------------------------------------------------------------------------------
"""HTTP responses"""

"""When an HTTP request is issued, the server sends a response back to the client. This answer is also composed of different 
elements:

- headers with response metadata
- a body with the content of the response
- a status code"""

"""***The content of an HTTP response is very often HTML for websites but it is easier to find **JSON or XML** for APIs.****"""
# --------------------------------------------------------------------------------------------------------------------------
"""The status code 

The status code makes it easy to understand if the request was successful. By convention, error codes should correspond to 

the following states:

100: Information
200: Means that the request has concluded / Success
300: Redirect
40X: Means client side error / Client Error
50X: means server side error / Server Error

Thus, a 404 code is an error from the client who did not enter the correct address to access the resource, 
while a 503 error will be an error from the server who is unable to run the requested service."""

# --------------------------------------------------------------------------------------------------------------------------
"""Links to the web"""

"""
- Websites operate on the same principle of server-client architecture that is requested via HTTP using a Web browser. 
Thus, by clicking on the site link, the browser sends a **GET** type request to the server of the site. 
If the address is correct, the server sends back a response which contains an HTML file which will then be interpreted 
by the browser.

- When you fill out a form on a website, it is generally a **POST** type request. The request then contains the data filled 
in the form."""

# --------------------------------------------------------------------------------------------------------------------------
"""HTTPS protocol"""

"""The 'HTTPS' protocol is a more secure version than the HTTP protocol. It is in fact the HTTP protocol to which is added 
a layer of SSL (Secure Socket Layer) encryption. It protects the authentication of a server, the confidentiality and 
integrity of the data exchanged, and sometimes the authentication of the client: a public key is given to the client so 
that the data sent back to the server is encrypted; these data are then decoded using a private key available on the server. 
It tends to impose itself as the norm, pushed by search engines which better reference sites using an HTTPS protocol."""

# --------------------------------------------------------------------------------------------------------------------------
"""HTTP clients"""

"""the browser is a client that makes it possible to make HTTP requests to servers that are able to return data according to 
the request. However, there are other easier tools to use when you want to interact with an API."""

# --------------------------------------------------------------------------------------------------------------------------
"""CURL"""  # https://jsonplaceholder.typicode.com/

"""We will query an API from the terminal using the cURL (Client URL Request Library) command line interface. 
To make an HTTP request from the terminal with cURL, the syntax for making a request is as follows:"""

# curl -X GET http://example.com

"""The (-X argument) here introduces the method,**GET**. Then we can write the URI. The API we are going to query is a 
dummy web API for developers. You can view the documentation for this API here."""

# curl -X GET https://jsonplaceholder.typicode.com/posts/1

# output:
# {
#   "userId": 1,
#   "id": 1,
#   "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#   "body": "quia et suscipit\nsuscipit recusandae t architecto"
# }

"""With this request, we receive a "stringified" JSON object containing information about a message. Here we have requested 
the post with ID 1. We can get all posts with a GET request to the /posts endpoint. This is a scenario we commonly encounter: 
the endpoint with an ID returns an individual observation while **without any ID** it returns all observations."""

"""The HTTP response to this request contains only the body. ***To see the headers**, we can add the(-i) argument to the command:
"""
# curl -X GET -i https://jsonplaceholder.typicode.com/posts/1

"""In the header, you can see information about the content of the response such as the status code which is here 200"""

# --------------------------------------------------------------------------------------------------------------------------
"""We have seen how to make a request with the GET method. 

Now, if you want to use the **PUT method** to add data to the API, you'll probably want to specify a body and some headers. 
To do this, you must precede your headers with the (-H argument) and the body with the (-d argument).
"""

# curl -X PUT -i\
#  -H "Content-Type: application/json"\              #### Here, we indicate in the header the type of data sent (JSON)
#  -d '{"id": 1, "content": "hello world"}'\         #### in the body the data in question
#  https://jsonplaceholder.typicode.com/posts/1

# --------------------------------------------------------------------------------------------------------------------------
"""Postman"""

"""Postman is a collaborative platform for API development. It allows to build and execute HTTP requests, to store them in a 
history in order to be able to replay them, and to organize them in collections.

Among other things, Postman allows:

quickly and easily send REST, SOAP and GraphQL requests
automate manual tests and integrate them into a CI/CD pipeline to ensure that no code changes will break the API in production.
communicate the expected behavior of an API by simulating endpoints and their responses without having to configure a 
backend server.
generate and publish beautiful machine-readable documentation to make the API easier to use.
Stay up to date on the health of their API by checking performance and response times at scheduled intervals.
collaborate in real time with built-in version control.
Postman therefore offers a very simple interface for making complex HTTP requests. It is a very useful tool for 
testing/exploring an API. In addition, the features of Postman allow you to easily export a request made with Postman 
in the language of your choice."""
# --------------------------------------------------------------------------------------------------------------------------
"""Python HTTP Libraries"""

"""The simplest library for making requests with Python is probably the Requests library.

You can install it using the Python package manager"""

# pip3 install requests        # or conda install requests

# *********************************
import requests

# creating a GET request
r = requests.get("https://jsonplaceholder.typicode.com/posts/1")


# getting the response elements
response_dict = r.json
response_header = r.headers
status_code = r.status_code


"""We can of course pass a body, headers thanks to this library."""

r = requests.put(
    url="https://jsonplaceholder.typicode.com/posts/1",
    data={"id": 1, "content": "hello world"},
    headers={"Content-Type": "application/json"},
)
# ****************************************
# --------------------------------------------------------------------------------------------------------------------------
"""The REST standard"""

"""
- Each API has a specific architecture, as well as rules to respect which determine the data formats and commands accepted 
to communicate with. In order to promote the accessibility and standardization of APIs for developers, there are now classic 
API architectures that are very often used.

- For example, the REST (Representational State Transfer) architecture is an architecture that is very often used in the 
creation of WEB services. It allows applications to communicate with each other regardless of the operating system via 
the HTTP protocol. A REST API uses HTTP requests to communicate and must respect the following principles:

- Client-server architecture: the client must make HTTP requests to request resources. There is independence between the 
client side and the server application so that changes to one endpoint do not affect the others.
- Uniform interface: simplified architecture that allows each part to evolve independently. To speak of a uniform interface, 
the 4 constraints must be respected:
- Identification of resources in requests: resources are identified in requests and are separated from the representations 
returned to the client.
- Manipulation of resources by representations: Clients receive files that represent resources. These representations should 
contain enough information to be edited or deleted.
- Self-describing messages: All messages returned to the client contain enough information to describe how the client should 
process the information.
- Hypermedia as an Application State Change Engine (HATEOAS): After accessing a resource, the REST client must be able to 
discover all other actions available through hyperlinks.
- With caching: the client must be able to cache the data that the API provides in response (https://aws.amazon.com/fr/caching/)
- Layered system: communication can take place through intermediate servers (proxy servers or load balancing devices).
- Stateless: no information is stored between two requests and the API thus treats each request as a first request

- REST is not the only one and is not mandatory to implement to obtain an efficient API, but it is undoubtedly the best known.

- Note that in the REST standard, the endpoint must designate an object that we want to manipulate and the methods must 
correspond to the following effects:"""

# GET    to retrieve information
# POST   to add new data to the server
# PUT    to modify data already present on the server
# DELETE to delete data

# --------------------------------------------------------------------------------------------------------------------------
"""The FastAPI library"""  # https://fastapi.tiangolo.com/

"""The FastAPI library is a very interesting library for developing APIs with Python. Indeed, the APIs are relatively fast 
compared to other Python frameworks. In addition, FastAPI makes it easy to implement documentation as well as type 
constraints on the data."""

# --------------------------------------------------------------------------------------------------------------------------
"""First implementation"""

"""In this part, we will see the basic principles of FastAPI. The first is to install the fastapi and uvicorn libraries. 
uvicorn, which is a library that allows you to launch the server created by FastAPI.

Python libraries for creating APIs generally use another server to launch the API. For example, you can launch a 
Flask API without uvicorn but this is generally not recommended (see the launch message)."""

# pip3 install fastapi uvicorn

"""To create an API, we will need to instantiate the FastAPI class from the fastapi package.

****Create a file called ****main.py**** and paste the following lines****"""


"""after that give the permissions of a file"""

# chmod 777 main.py

""" open another console and use this code"""

# uvicorn main:api --reload

"""Here, we specify the (main file) and the (name of the API) to launch inside this (file: api). 
The (--reload argument )automatically updates the API when making changes to the source file. 
In the console, we must observe the following line:"""

# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

"""This line gives us the address at which the API is running."""

# ------------------------------------------------------------------------------------------------
"""In another console, run the following command to query the endpoint /"""

# curl -X GET http://127.0.0.1:8000/

"""The result corresponds to what we passed as a value to return:
{ "data": "hello world" }"""


"""Run the following command to display the response headers:"""

# curl -X GET -i http://127.0.0.1:8000/

# output:

# HTTP/1.1 200 OK
# date: Sun, 06 Nov 2022 01:48:34 GMT
# server: uvicorn
# content-length: 22
# content-type: application/json

"""Note that the content returned is of the application/json type: 
- we did not specify this argument but FastAPI by default returns data in json format."""
# --------------------------------------------------------------------------------------------------------------------------
"""Without stopping the API, modify the main.py file by replacing the get_index function with the following lines:"""


def get_index():
    return "Hello world"


"""Rerun the previous curl command

We can see that the change has been taken into account by the server. The content type is always application/json."""
# --------------------------------------------------------------------------------------------------------------------------
"""In the code we have executed we can see the presence of a decorator: @api.get('/'). This decorator is used to specify a route, 
that is to say an endpoint as well as a method. So the function that is decorated by this line will run when a GET type
request is made to endpoint /.

This way of managing endpoints as well as methods makes it easy to see which function is called when and under what conditions.

You can of course use different methods and specify different endpoints."""

"""Modify the main.py file by putting the following routes in it"""


@api.get("/")
def get_index():
    return {"method": "get", "endpoint": "/"}


@api.get("/other")
def get_other():
    return {"method": "get", "endpoint": "/other"}


@api.post("/")
def post_index():
    return {"method": "post", "endpoint": "/"}


@api.delete("/")
def delete_index():
    return {"method": "delete", "endpoint": "/"}


@api.put("/")
def put_index():
    return {"method": "put", "endpoint": "/"}


@api.patch("/")
def patch_index():
    return {"method": "patch", "endpoint": "/"}


# --------------------------------------------------------------------------------------------------------------------------
"""Run the following commands to test all routes"""

# # GET at /
# curl -X GET -i http://127.0.0.1:8000/

# # POST at /
# curl -X POST -i http://127.0.0.1:8000/

# # PUT at /
# curl -X PUT -i http://127.0.0.1:8000/

# # DELETE at /
# curl -X DELETE -i http://127.0.0.1:8000/

# # PATCH at /
# curl -X PATCH -i http://127.0.0.1:8000/

# # GET at /other
# curl -X GET -i http://127.0.0.1:8000/other

"""In a few lines, we were able to create routes for different methods and different endpoints."""

# --------------------------------------------------------------------------------------------------------------------------
"""Now let's try to query an endpoint that doesn't exist"""

# curl -X GET -i http://127.0.0.1:8000/no_where

# output
# HTTP/1.1 404 Not Found

"""We do get a 404 Not Found type error with content in json format: {"detail": "Not found"}. 
FastAPI therefore handles these routing errors quite gracefully
"""
# --------------------------------------------------------------------------------------------------------------------------
"""Documentation"""

"""One of the important challenges of APIs is to provide precise documentation that allows simple use of the API. 
FastAPI has the advantage of automatically generating this documentation.

By using a tunnel between port 8000 of the remote machine and port 8000 of the local machine, the API can be opened in a 
web browser."""

# --------------------------------------------------------------------------------------------------------------------------
"""By using a tunnel between port 8000 of the remote machine and port 8000 of the local machine, the API can be opened in a 
web browser.

Create this tunnel and open a web browser to http://localhost:8000/ (or change the port if you decided to forward the 
data on another port)

***i did it by using terminal of vscode because i didn't know how to create a tunnel***
"""

"""One should retrieve the result of the GET request at endpoint /, i.e., the result of the get_index function:

Open the endpoint docs in the browser: """

# http://localhost:8000/docs

"""This is the OpenAPI (formerly Swagger) interface. This interface makes it easy to see the endpoints and accepted methods."""

""""((images in readme))""""

"""
- Click on the GET method of the endpoint /.
- You can click on the Try it out button then execute to launch a GET request on the endpoint /. The response is transcribed:
- This interface gives us the response, the headers of the response. In addition, we can see the curl request associated with 
the test we just made:

curl -X 'GET' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json'
"""

"""FastAPI offers another version of this interface at the /redoc endpoint.
"""
# Open the URL http://localhost:8000/redoc

"""Finally, we can go to the /openapi.json endpoint. We will find the declaration of the API used by ReDoc and OpenAPI 
to generate the documentation:"""

# Open the URL http://localhost:8000/openapi.json

"""We should get the json below: here we have formatted it to make it more readable."""

# {
#   "openapi": "3.0.2",
#   "info": {
#     "title": "FastAPI",
#     "version": "0.1.0"
#   },
#   "paths": {
#     "/": {
#       "get": {
#         "summary": "Get Index",
#         "operationId": "get_index__get",
#         "responses": {
#           "200": {
#             "description": "Successful Response",
#             "content": {
#               "application/json": {
#                 "schema": {}
#               }
#             }
#           }
#         }
#       },
#       "put": {
#         "summary": "Put Index",
#         "operationId": "put_index__put",
#         "responses": {
#           "200": {
#             "description": "Successful Response",
#             "content": {
#               "application/json": {
#                 "schema": {}
#               }
#             }
#           }
#         }
#       },
#       "post": {
#         "summary": "Post Index",
#         "operationId": "post_index__post",
#         "responses": {
#           "200": {
#             "description": "Successful Response",
#             "content": {
#               "application/json": {
#                 "schema": {}
#               }
#             }
#           }
#         }
#       },
#       "delete": {
#         "summary": "Delete Index",
#         "operationId": "delete_index__delete",
#         "responses": {
#           "200": {
#             "description": "Successful Response",
#             "content": {
#               "application/json": {
#                 "schema": {}
#               }
#             }
#           }
#         }
#       },
#       "patch": {
#         "summary": "Patch Index",
#         "operationId": "patch_index__patch",
#         "responses": {
#           "200": {
#             "description": "Successful Response",
#             "content": {
#               "application/json": {
#                 "schema": {}
#               }
#             }
#           }
#         }
#       }
#     },
#     "/other": {
#       "get": {
#         "summary": "Get Other",
#         "operationId": "get_other_other_get",
#         "responses": {
#           "200": {
#             "description": "Successful Response",
#             "content": {
#               "application/json": {
#                 "schema": {}
#               }
#             }
#           }
#         }
#       }
#     }
#   }
# }