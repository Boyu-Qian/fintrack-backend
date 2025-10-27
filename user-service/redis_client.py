import os
import redis
import time

HOST = redis
PORT = 6379
PASSWORD = "AsDfQwEr123777"
DB = 0
redis_url = f"redis://:{PASSWORD}@{HOST}:{PORT}/{DB}"
redis_client = redis.Redis.from_url(redis_url)

if __name__ == "__main__":
    try:
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
        print("Redis Error:", e)
