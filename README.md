# LRUCache

A Python implementation of **Least Recently Used (LRU) Cache** with support for core operations like `get`, `put`, `remove`, and `remove_least_recently_used`. This implementation uses efficient data structures to maintain quick access and eviction policies.

## 📦 Features

- Fast `O(1)` access time for `get`, `put` & `remove` operations.
- Automatic eviction of least recently used items when capacity is exceeded.
- Custom support for removing specific keys.

## 🚀 Usage

```python
from LRU import LRUCache  # Rename as appropriate
```

### Initialize LRU Cache with capacity 3
```python
cache = LRUCache(3)
```
### Add key-value pairs
```python
cache.put(1, 'A')    # Cache: {1: 'A'}
cache.put(2, 'B')    # Cache: {2: 'B', 1: 'A'}
cache.put(3, 'C')    # Cache: {3: 'C', 2: 'B', 1: 'A'}
```

### Accessing key 2 makes it most recently used
```python
print(cache.get(2))  # Output: 'B', Cache: {2: 'B', 3: 'C', 1: 'A'}
```

### Adding new entry causes eviction of least recently used key (1)
```python
cache.put(4, 'D')    # Cache: {4: 'D', 2: 'B', 3: 'C'}
```

### Remove a key
```python
cache.remove(3)      # Cache: {2: 'B', 4: 'D'}
```

### Explicitly remove the least recently used item
```python
cache.remove_least_recently_used()  # Removes key 2
```

# LFUCache

This Python module implements an **Least Frequently Used Cache** (LFU) with O(1) time complexity for core operations (`get`, `set`). The cache combines frequency tracking with LRU (Least Recently Used) eviction policies to handle items with the same frequency count.

## 📦 Features
- `O(1)` time complexity for `get` and `put` operations
- `O(K)` time complexity for `remove`, K =  number of frequency buckets
- **Frequency-based eviction** with LRU tie-breaking
- **Configurable cache capacity**

## 🚀 Usage

```python
from LFU import LFUCache
```

### Initialize LFU Cache with capacity 3
```python
cache = LFU(3)
```

### Add key-value pairs (all start with frequency=1)
```python
cache.set(1, 'A')    # Cache: {1: 'A'} (freq=1)
cache.set(2, 'B')    # Cache: {2: 'B', 1: 'A'} (both freq=1)
cache.set(3, 'C')    # Cache: {3: 'C', 2: 'B', 1: 'A'} (all freq=1)
```

### Access keys to increase their frequencies
```python
print(cache.get(1))  # Output: 'A' → Key1 now freq=2
print(cache.get(1))  # Output: 'A' → Key1 now freq=3
print(cache.get(2))  # Output: 'B' → Key2 now freq=2
print(cache.get(3))  # Output: 'C' → Key3 remains freq=1 (least frequent)
```

### Add new entry - evicts least frequent (key 3)
```python
cache.set(4, 'D')    # Evicts key3 (lowest freq=1), 
                     # Cache: {1: 'A' (freq=3), 2: 'B' (freq=2), 4: 'D' (freq=1)}
```

### Access key 2 multiple times to increase frequency
```python
cache.get(2)         # Key2 now freq=3
cache.get(2)         # Key2 now freq=4
```

### Add new entry - evicts least frequent (key4) even though recently added
```python
cache.set(5, 'E')    # Evicts key4 (freq=1), 
                     # Cache: {1: 'A' (freq=3), 2: 'B' (freq=4), 5: 'E' (freq=1)}
```

### Remove a key
```python
cache.remove(2)      # Cache: {1: 'A' (freq=3), 5: 'E' (freq=1)}
                     # (min_frequency remains 1)
```

