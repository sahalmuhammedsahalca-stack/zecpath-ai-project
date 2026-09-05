import sys
from typing import Any


class MemoryOptimizer:
    """Provides lightweight memory usage inspection."""

    def estimate_size(
        self,
        data: Any,
    ) -> int:

        return sys.getsizeof(data)

    def compare(
        self,
        before: Any,
        after: Any,
    ):

        before_size = self.estimate_size(before)
        after_size = self.estimate_size(after)

        reduction = before_size - after_size

        return {
            "before_bytes": before_size,
            "after_bytes": after_size,
            "reduction_bytes": reduction,
            "reduced": reduction > 0,
        }