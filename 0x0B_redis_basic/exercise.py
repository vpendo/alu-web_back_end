#!/usr/bin/env python3
""" Redis Cache File """
import redis
from typing import Union, Callable, Optional, Any
from functools import wraps
from uuid import uuid4


def replay(obj: Union[Callable, str]) -> None:
    """ Returns a printed history of inputs and outputs """
    cache = obj.__self__

    call_count = str(cache.get(cache.store.__qualname__), 'UTF-8')
    inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
    outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

    print(f'{obj.__qualname__} was called {call_count} times:')

    for input, output in zip(inputs, outputs):
        input, output = str(input, 'UTF-8'), str(output, 'UTF-8')
        print(f'{obj.__qualname__}(*{input}) -> {output}')


def count_calls(method: Callable) -> Callable:
    """ Count calls decorator method """
    key = method.__qualname__

    @wraps(method)
    def call_counter(self, *args) -> bytes:
        self._redis.incr(key)
        return method(self, *args)

    return call_counter


def call_history(method: Callable) -> Callable:
    """
    --------------------
    METHOD: call_history
    --------------------
    Description:
        Keeps a history the inputs and outputs
    """
    key = method.__qualname__

    @wraps(method)
    def history_dec(self, *args) -> bytes:
        self._redis.rpush(f'{key}:inputs', str(args))
        data = method(self, *args)
        self._redis.rpush(f'{key}:outputs', data)
        return data

    return history_dec


class Cache:
    """ Redis Caching class """

    def __init__(self):
        """ Initializes the Cache object with a redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Adds data to the redis database """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """ Given a key, fetches data from the redis client """
        data = self._redis.get(key)
        return data if not callable(fn) else fn(data)

    def get_int(self, key: str) -> int:
        """ Given a key, returns the key as an int value """
        return int(self._redis.get(key))

    def get_str(self, key: str) -> str:
        """ Given a key, returns the key as a string value """
        return str(self._redis.get(key), 'UTF-8')
