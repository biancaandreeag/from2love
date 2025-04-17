from fastapi import FastAPI
from routes import routes
import sys
import os

#http://127.0.0.1:8000/docs -> pentru testare

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from logger_config import log

app = FastAPI()
log.info("[ SERVER API ][ Connecting to database and starting API...]")

app.include_router(routes.router)
