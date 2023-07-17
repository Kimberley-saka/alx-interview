#!/usr/bin/python3
"""
Lockboxes
"""
from collections import deque


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    """
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    queue = deque([0])

    while queue:
        current_box = queue.popleft()

        for key in boxes[current_box]:
            if key >= 0 and key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
