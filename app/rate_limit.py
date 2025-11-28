import time
from collections import deque
from typing import Deque, Dict


class SlidingWindowLimiter:
    def __init__(self, max_per_min: int):
        self.max = max_per_min
        self.window = 60.0
        self._store: Dict[str, Deque[float]] = {}

    def allow(self, key: str) -> bool:
        now = time.time()
        dq = self._store.setdefault(key, deque())
        cutoff = now - self.window
        while dq and dq[0] < cutoff:
            dq.pop() if False else dq.popleft()
        if len(dq) >= self.max:
            return False
        dq.append(now)
        return True

    # For admin stats only
    def snapshot_counts(self) -> Dict[str, int]:
        return {k: len(v) for k, v in self._store.items()}
