from fastapi import FastAPI
import redis

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "AI DevOps Assignment Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/redis-test")
def redis_test():
    try:
        r = redis.Redis(host="redis", port=6379)
        r.set("assignment", "working")
        value = r.get("assignment").decode()
        return {"redis": value}
    except Exception as e:
        return {"error": str(e)}