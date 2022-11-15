from fastapi import FastAPI, Request
from datetime import datetime

storage = FastAPI(title='MY FASTAPI')


@storage.get('/')#ROUTE
def index():
    return "My name is Arnaud, This is my API!"

@storage.get('/today')#Route with GET METHOD
def today():
    return str(datetime.now())

@storage.get('/mynames')
def names(first_name: bool = False, last_name: bool = False, full_name: bool = False):
    full_names = ""
    if first_name:
        full_names += 'Arnaud'
    if last_name:
        full_names += ' Kayonga'
    if full_name:
        full_names = "Hello my name Arnaud Kayonga"
        
    return full_names

if __name__ == "__main__":
    storage.run()