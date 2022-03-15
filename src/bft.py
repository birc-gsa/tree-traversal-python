"""A module for breadth-first traversal of trees."""

from collections import deque
from typing import Iterable
from tree import T


def bf_order(t: T | None) -> Iterable[int]:
    """Breadth-first traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(bf_order(tree))
    [2, 1, 4, 3, 5]
    """
    # When we have a tree on the stack we need to traverse it,
    # when we have an int it is a value we should emit
    queue: deque[T | int] = deque([t] if t else [])
    while queue:
        v = queue.pop()
        if isinstance(v, int):
            yield v
        else:
            yield v.val
            if v.right:
                queue.append(v.right)
            if v.left:
                queue.append(v.left)
