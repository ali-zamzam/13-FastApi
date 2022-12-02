"""Performance and asynchronous queries"""

"""Simple performance
We can also see that FastAPI is a relatively fast tool compared to Flask. We are far from the frameworks 
dedicated to the processing of HTTP requests which are much faster but we obtain interesting performances 
in terms of speed of responses. We can refer to the following benchmarks:"""

# https://web-frameworks-benchmark.netlify.app/result?l=python

# https://www.techempower.com/benchmarks/#section=data-r20&hw=ph&test=json&l=zijzen-sf&a=2

# ----------------------------------------------------------------------------------------------------------------
"""Competition"""

"""One of the advantages of FastAPI is to provide a simple way to process requests asynchronously. 
It is thus possible to launch processing which can take time, without blocking access to the API. 
To define an asynchronous function, here we only need to use the same syntax used with asyncio."""

import asyncio
import time

from fastapi import FastAPI

api = FastAPI()


def wait_sync():
    time.sleep(10)
    return True


async def wait_async():
    await asyncio.sleep(10)
    return True


@api.get("/sync")
def get_sync():
    wait_sync()
    return {"message": "synchronous"}


@api.get("/async")
async def get_async():
    wait_async()
    return {"message": "asynchronous"}


"""We just created an API that has two endpoints /sync and /async. These two endpoints do nothing except wait 
for 10s and then return a response. One could imagine that the query triggers a long operation on a database. 
We still want to receive a quick response on the acceptance of this order."""

# ----------------------------------------------------------------------------------------------------------------
import time
from multiprocessing import Pool

import requests
from fastapi import FastAPI

api = FastAPI()


def compute_response_time_sync(x):
    t0 = time.time()
    requests.get(url="http://127.0.0.1:8000/sync")
    t1 = time.time()
    return t1 - t0


def compute_response_time_async(x):
    t0 = time.time()
    requests.get(url="http://127.0.0.1:8000/async")
    t1 = time.time()
    return t1 - t0


def overflow_requests(function, number_of_parallel_operations=20):

    with Pool(number_of_parallel_operations) as p:
        values = p.map(function, [i for i in range(number_of_parallel_operations)])
        s = 0
        for i in values:
            s += i
        return s / len(values)


if __name__ == "__main__":
    print("making 20 requests on the `/sync` endpoint ...")
    delta_t = overflow_requests(compute_response_time_sync, 20)
    print("took {} seconds".format(delta_t))

    print("making 20 requests on the `/async` endpoint")
    delta_t = overflow_requests(compute_response_time_async, 20)
    print("took {} seconds".format(delta_t))


"""
In this script, we query both endpoints. To simulate a simultaneous arrival, we use a Pool which makes it 
possible to parallelize the requests. This script will therefore simulate the querying of our API by about 
twenty clients.

On a machine with 16 cores, we see that the first requests take on average 12 seconds. Indeed, the machine 
must process 20 requests but can only handle 16 at a time. There are then 4 queries left which will take double the time, i.e. 20 seconds: 10 * 16 + (10 + 10) * (20 - 16).

On the other hand, we see that asynchronous requests are almost instantaneous. Here, we have chosen not to 
wait for the response of the asynchronous function to send a response. But in the case where we choose to 
wait for the response, by adding the term await in front of wait_async, the requests will all take 10s.

Modify the wait_async() line by await wait_async() then relaunch the test

Requests all take 10s.

The integration of asynchronous functions is very easy and nothing prevents to systematize the use of the 
async keyword in front of all the functions called after method decorators or even error handling decorators."""
