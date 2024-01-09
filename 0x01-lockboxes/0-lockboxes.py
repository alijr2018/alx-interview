#!/usr/bin/python3
"""
0-lockboxes.py
"""
from collections import deque


def canUnlockAll(boxes):
    if not boxes or len(boxes) == 0:
        return False

    opened_boxes = set()
    opened_boxes.add(0)

    queue = deque([0])
    while queue:
        current_box = queue.popleft()

        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                queue.append(key)

        return len(opened_boxes) == len(boxes)