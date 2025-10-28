import os
import redis
import time

HOST = os.getenv("REDIS_HOST")
PORT = int(os.getenv("REDIS_PORT"))
PASSWORD = os.getenv("REDIS_PASSWORD")
DB = 0

redis_client = redis.Redis(host=HOST,username="default",port=PORT,password=PASSWORD,db=DB,decode_responses=True)

if __name__ == "__main__":
    try:
        print(type(HOST))
        print(type(PORT))
        print(type(PASSWORD))
        # 先 ping 一下
        print("PING:", redis_client.ping())

        # 写一个 key
        redis_client.set("foo", "bar")

        # 读回这个 key
        value = redis_client.get("foo")
        print("GET foo:", value)

        # 写一个带过期时间的 key
        redis_client.set("temp", "123", ex=10)  # 10 秒后过期
        print("GET temp:", redis_client.get("temp"))

    except Exception as e:
        import traceback
        traceback.print_exc()
