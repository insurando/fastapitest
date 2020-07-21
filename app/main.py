import sys
import os
import time
import logging
from fastapi import APIRouter, Depends, FastAPI, Header, HTTPException,Request, Response, status
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Set
import pickle
import itertools
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import numpy as np

#=========== CONSTANTS and ERROR Definitions =================
global LANGUAGES
global ERROR_LAN
LANGUAGES = ['de-CH','fr-CH','it-CH','en-US']
ERROR_LAN = HTTPException(status_code=404, detail="language header not one of de-CH, fr-CH, it-CH, en-US")

################## Setup Logger from gunicorn (hack) #########################
import logging


################## MAIN App ####################
app = FastAPI(title='test',description='test',version='1.0.0')

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
	max_age=0
)

################## Main Endpoint ###################
@app.get("/probe")
def probe(*, accept_language: str = Header('de-CH'),x_session_id: str = Header('-'),response: Response):
    start = time.time()
    # sleep 1 second to check response time logging
    response.headers["X-Response-Time"] = str.format('{0:.6f}',np.round(time.time() - start,6))
    return {"message": "FastAPI Inconnect","release": "1"}