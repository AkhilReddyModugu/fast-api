from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient


app=FastAPI()
# conn= MongoClient("mongodb+srv://akhilreddymodugu13:reddyakhil13@cluster0.opexl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")




