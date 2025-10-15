import os,httpx


from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
from typing import Dict 



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"]
)


url = "https://catfact.ninja/fact"
data= {
        "email": "adesolaisa3@gmail.com",
        "name": "Busari Adesola Issah",
        "stack": "Python/Flask"
    }
HTTP_CLIENT=httpx.AsyncClient()

async def fetch_cat() -> str:
    """Fetch random cat fact"""
    try:
        response = await HTTP_CLIENT.get(url, timeout=60)

        response.raise_for_status()
        data= response.json()
        return data.get("fact", "No fact available")
    except httpx.TimeoutException:
        print("ERROR: Cat API call timed out.")
        return "No fact available"
    except httpx.HTTPStatusError as e:
        print(f"ERROR: Cat API returned status code {e.response.status_code}")
        return"No fact available"
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")
        return "No fact available"
    

@app.get('/me',
         status_code=status.HTTP_200_OK,
         response_class=JSONResponse)
async def  info():
    """return users profile alongside the funfact"""

    
    response= await fetch_cat()
    current_datetime=(datetime.now()).isoformat().replace("+00:00", "Z")
        
    response_data={
        "status":"success",
        "user":data,
        "timestamp":current_datetime,
        "fun_fact": response
    }
    return response_data 

