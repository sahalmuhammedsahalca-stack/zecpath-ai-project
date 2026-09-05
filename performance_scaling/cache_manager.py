import time


class CacheManager:
    """Simple in-memory cache with TTL expiration."""

    def __init__(
        self,
        ttl_seconds: int = 300,
    ):

        if ttl_seconds <= 0:
            raise ValueError(
                "ttl_seconds must be greater than zero"
            )

        self.ttl_seconds = ttl_seconds
        self._cache = {}

    def set(
        self,
        key,
        value,
    ):

        self._cache[key] = {
            "value": value,
            "created_at": time.time(),
        }

    def get(self, key):

        item = self._cache.get(key)

        if item is None:
            return None

        if (
            time.time() - item["created_at"]
            > self.ttl_seconds
        ):
            del self._cache[key]
            return None

        return item["value"]

    def delete(self, key):

        self._cache.pop(
            key,
            None,
        )

    def clear(self):

        self._cache.clear()

    def size(self):

        return len(self._cache)