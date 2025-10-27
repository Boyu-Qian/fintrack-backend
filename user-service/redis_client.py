import os
import redis
import time

HOST = os.getenv("REDIS_HOST")
PORT = int(os.getenv("REDIS_PORT"))
PASSWORD = os.getenv("REDIS_PASSWORD")
DB = 0
redis_client = redis.Redis(host=HOST,port=PORT,db=DB,password=PASSWORD,decode_responses=True)