import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

def enqueue(job):
    redis_client.lpush("gpu_jobs", job)

def dequeue():
    return redis_client.rpop("gpu_jobs")
