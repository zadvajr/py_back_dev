#Concurrency and Async/Await in FastAPI
#FastAPI is designed to leverage Python's asyncio library to enable higly efficient asynchronous programming
#This allows for non-blocking operations which are critical for
# web applications handling multiple concurrent tasks like API requests, database interactions. or file I/O

#What is asynchronous programming? 
#Asynchronous programming allows tasks to run concurrently, especially when they involve waiting
#e.g. network requests or file operations. this is achieved using:
#1. async function - which defines coroutine
#2. await keyword - pause execution of a coroutine until a result is available

 #Asynchronouse support in FastAPI
#FastAPI Supports:
#1. Asynchronouse route handlers (async def)
#2. Integration with asynchronous libraries like htppx, SQLAlchemy and others.
#3. Combining async and sync route handlers ensuring flexibility.

#Examples
#1. Basic Async endpoint
from fastapi import FastAPI, Depends
from 
import httpx

app = FastAPI()

@app.get("/async-example")
async def async_endpoint():
    return {"message": "This is an async endpoint"}

#here, the async function ensures the endpoint can handle concurrent requests without blocking other tasks.

#2. Using await with IO operations
@app.get("/fetch-data")
async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/async-example")
    return {"message": "fetching data from http://localhost:8000/async-example", "data": response.json()}

#This example demonstrates
#1. Using the await keyword to perform an http request asynchronously
#2. Avoiding blocking the application while waiting for the response

#3. Mixing Async and Sync Endpoints
@app.get("/sync-example")
def sync_endpoint():
    return {"message": "This is a sync endpoint"}

@app.get("/async-example")
async def async_endpoint():
    return {"message": "This is an async endpoinnt"}

#FastAPI allows both synchronous and asynchronous route handlers. However, sync endpoints may block the -
#event loop if they perform long-running tasks.

#Performin Database Operations.
