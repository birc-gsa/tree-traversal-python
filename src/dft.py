"""A module for depth-first (in-order) traversal of trees."""

from typing import Iterable
from tree import T


def in_order(t: T | None) -> Iterable[int]:
    """In-order traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(in_order(tree))
    [1, 2, 3, 4, 5]
    """
    # When we have a tree on the stack we need to traverse it,
    # when we have an int it is a value we should emit
    stack: list[T | int] = [t] if t else []
    while stack:
        v = stack.pop()
        if isinstance(v, int):
            yield v
        else:
            if v.right:
                stack.append(v.right)
            stack.append(v.val)
            if v.left:
                stack.append(v.left)
