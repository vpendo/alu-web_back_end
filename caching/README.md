# Caching System

This project explores the implementation of various caching strategies in Python by creating classes that inherit from a common base class, `BaseCaching`.

## Project Structure

The caching strategies are implemented incrementally through a series of tasks, starting with a basic dictionary cache, and moving to more advanced eviction strategies like FIFO, LRU, and LFU.

## Files

- `base_caching.py`: Defines the `BaseCaching` class, which includes the cache dictionary (`cache_data`) and required interface (`put`, `get`).
- `0-basic_cache.py`: Implements a basic cache using a standard dictionary. No limit is placed on the number of cached items.
- `0-main.py`: Test script for the basic cache.

## How to Run

```bash
chmod +x *.py
./0-main.py
