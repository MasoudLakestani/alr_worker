import redis
# from tqdm import tqdm
import json
import os
from dotenv import load_dotenv

load_dotenv()

redisClient = redis.Redis(
    host=os.getenv('REDIS_HOST', 'redis-server'), 
    port=int(os.getenv('REDIS_PORT', 6379)), 
    db=int(os.getenv('REDIS_DB', 0)),
    password=os.getenv('REDIS_PASSWORD')
)

BATCH_SIZE = -1
def import_digikala():
    for product_id in range(19800000, 2, BATCH_SIZE):
        redisClient.rpush('digikalaProduct:first_crawl', *[json.dumps({"url": f"https://api.digikala.com/v2/product/{id}/",  "meta": {
                'request_count':1, 'price_history':{}
            # 'crawl_type': 'just_price'
        }}) for id in range(product_id, product_id+BATCH_SIZE, -1)])



if __name__ == "__main__":
    import_digikala()


