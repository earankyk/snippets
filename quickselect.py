#!/usr/bin/env python
import random

def quickselect(nums:list[int], k:int) -> int:
    """Function to return the kth smallest number in a list"""
    pivot = random.randint(0, len(nums))
    nums[0], nums[pivot] = nums[pivot], nums[0]
    start = 0
    end = len(nums)
    while True:
        while start < len(nums) and nums[start] <= nums[pivot]:
            start += 1
        while end > 0 and nums[end] >= nums[pivot]:
            end -= 1
        if start >= end:
            break
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
