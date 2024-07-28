"""
File: main.py
Author: Steven "Kabbe" Karbjinsky
Description: ...

For more information, see: https://github.com/xKabbe/ascendify
"""
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Welcome to Ascendify API'}
