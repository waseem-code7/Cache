# LRUCache

A Python implementation of **Least Recently Used (LRU) Cache** with support for core operations like `get`, `put`, `remove`, and `remove_least_recently_used`. This implementation uses efficient data structures to maintain quick access and eviction policies.

## 📦 Features

- Fast `O(1)` access time for `get` and `put` operations.
- Automatic eviction of least recently used items when capacity is exceeded.
- Custom support for removing specific keys.

## 🚀 Usage

from lru_cache import LRUCache  # Rename as appropriate

# Initialize LRU Cache with capacity 3
cache = LRUCache(3)

# Add key-value pairs
cache.put(1, 'A')    # Cache: {1: 'A'}
cache.put(2, 'B')    # Cache: {1: 'A', 2: 'B'}
cache.put(3, 'C')    # Cache: {1: 'A', 2: 'B', 3: 'C'}

# Accessing key 2 makes it most recently used
print(cache.get(2))  # Output: 'B'

# Adding new entry causes eviction of least recently used key (1)
cache.put(4, 'D')    # Cache: {2: 'B', 3: 'C', 4: 'D'}

# Remove a key
cache.remove(3)      # Cache: {2: 'B', 4: 'D'}

# Explicitly remove the least recently used item
cache.remove_least_recently_used()  # Removes key 2


