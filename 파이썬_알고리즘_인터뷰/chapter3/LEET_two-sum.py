from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    print(nums_map)
    for index, num in enumerate(nums_map):
        print(index, num)
        complement = target - num
        if complement in nums_map and index != nums_map[complement]:
            print(f'index: {index}')
            print(nums_map)
            return [index, nums_map[complement]]

print(twoSum([2,2],4))


arr = {"a": 1, "b":2}

for i, v in enumerate(arr):
    print(i,v)