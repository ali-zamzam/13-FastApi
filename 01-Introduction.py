"""Introduction"""

"""
- API literally stands for Application Programming Interface and is defined as a set of subroutine definitions, 
communication protocols and tools that mediate communication between two applications. For the Data Engineer and 
the Machine Learning Engineer, the use of APIs will prove very useful during the deployment and automation phases.

- An API is actually used to de-correlate the service from a client who wishes to use it. It makes it possible to abstract 
a complex operation by giving a list of protocols for using this service.

- You can think of an API as a power outlet. A power outlet defines a protocol for its use: the device you want to plug in 
must have two pins, spaced by a certain gap. If this difference is respected then the socket will deliver a current of 220V 
at a frequency of 50Hz. From the point of view of the customer, that is to say of the electrical appliance, the production
of the electricity does not matter. It can be all kinds of power plants. On the other side, that is to say from the point 
of view of the socket, one does not need to adapt to the electrical device: if the protocol is respected, the necessary 
energy is supplied.

- The advantage of using an API lies in the simplification of the use of a complex service via a simple interface. 
The term API therefore represents an interface that abstracts, simplifies the use of a service."""
# --------------------------------------------------------------------------------------------------------------------------------
"""There are therefore many types of possible APIs. We will mention a few of them:

- the pandas library can actually be seen as an API. There is a set of rules that allow the use of complex functions from 
simplified documentation.
- the OpenWeatherMap API is a data API. From an HTTP request, we receive meteorological data in the requested place, on the 
requested date.
- the Google Cloud Translate API allows you to use Google's translation function to easily translate the texts you use."""

"""
- We can see that some APIs can be very simple and simply return certain data while others can hide the use of very complete 
functions. Note that in the case of the Google Translate and OpenWeatherMap APIs, you must identify yourself and possibly 
subscribe to a plan to be able to access the service.

- This is indeed one of the very important advantages of APIs. By clearly rewriting the rules for using an API, we can introduce 
the use of authentication tokens. We can then give certain rights to certain users, define limits in the use of the API and 
possibly sell access to the API.

- In addition, these APIs are part of the philosophy of micro-service architecture, in which the components of a system must be 
the smallest possible and the most isolated in order to be easily updated without changing the overall architecture. of the 
system.

- Imagine, for example, a company that offers bicycles for rent. This company stores its data on the availability of bikes for 
hire in a database. This database is regularly queried by various tools: the company's website, the mobile application, 
which both allow data to be reserved, by the rental terminals which notify of the return of the bicycles as well as by an 
internal dashboard . If the company does not use an API, then it will be necessary to update all the tools when the company 
will have to change its database (for example to allow distributed use of it). With an API, all you have to do is update 
the API which will act as an intermediary. In addition, we can develop certain functionalities that will allow external 
actors to access certain data (we can think of local authorities who could use this data to monitor the service).

- In the same way, if we build an efficient sentiment analysis algorithm, i.e. one that manages to correctly predict the 
positive or negative sentiment of a sentence or a text, we can hide the functioning of this algorithm by an API. Thus, 
we will be able to build subscriptions with various limits of use of our algorithm. Moreover, the day the algorithm is 
replaced by another more powerful one, its use does not change for the end user.

- The use of APIs therefore has many advantages: they make it possible to differentiate access to services according to 
users, to simplify updates of the service for which the API is the interface.

- Some companies rely heavily on this principle of APIs. A very famous example is Amazon: in 2002, Jeff Bezos would have 
asked all these teams to always create APIs each time they create a feature or expose data.

- We can see that APIs are therefore very interesting from an architectural point of view but also from a more business 
point of view because they offer economic perspectives.

- Finally, it should be noted that to guarantee the use of these APIs, the communication protocols must be very clear and 
well documented on the parameters to be provided as well as on their effects."""

# ---------------------------------------------------------------------------------------------------------------------
"""Micro-service architecture"""

"""
- With increasingly complex applications, organizations are increasingly turning to micro-services architectures, that is, 
architectures in which services are highly decoupled.

- Take the example of a social network. The company needs a user identification and management system, a system that allows 
messages to be created and posted, monitoring systems, etc. A classic solution would be to create a kind of very complex 
script which allows you to manage everything at once: from the reception of data to their storage, including the 
implementation of rights. **We then speak of monolithic architecture**.

- The other approach would be to create a storage architecture. We will separate user management from post management, etc. 
These different services will be able to communicate with each other through APIs."""

# ---------------------------------------------------------------------------------------------------------------------
"""The micro-service architecture has many advantages:

- the different services are autonomous, can be developed by different teams, in different languages since they can 
communicate with each other via their API.
- each service is specialized in solving a unique task which makes it easier to identify problems or to evolve a service
- as each service is a small unit independent from the rest of the system and specialized, one can easily modify this service 
thus giving faster and more agile development cycles.
- if certain services require more resources (storage, calculation), or if their need for resources changes over time, it is 
easy to scale up a service without disturbing the operation of the other services.
- a service can easily be reused by other teams in other projects. The API makes it possible to have precise documentation 
of the use of the service which allows other teams to include the service in their applications.
- we can finally easily identify where the breakdowns come from in such a system and repair these breakdowns quickly or even 
modify the service so that the breakdown no longer reappears."""
