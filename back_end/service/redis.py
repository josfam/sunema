"""
Module: redis
"""
import redis
import os

# Use environment variables for redis host, defaulting to 'localhost' if not set
class Redis:
    redis_host: str = ''
    r: redis = None

    def __init__(self) -> None:
        self.redis_host = os.getenv('REDIS_HOST', 'localhost')
        self.r = redis.Redis(host=self.redis_host, port=6379, db=0)

    def cache_user_location(self, user_id:str, location={}) -> None:
        """Cache user location data"""
        latitude = location.get('latitude')
        longitude = location.get('longitude')
        self.r.setex(f'user:{user_id}:location', 86400, f'{latitude}, {longitude}')

    def get_cached_user_location(self, user_id) -> tuple|None:
       location = self.r.get(f'user:{user_id}:location')
       if location:
           latitude, longitude = location.decode().split(',')
           return float(latitude), float(longitude)
       return None