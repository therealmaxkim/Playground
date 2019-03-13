'''
Questions
1. What are the input types? Integers? Numbers? Decimals?
2. Can the list be empty?
3. can you get a regular sorted array?

Observations
1. The list is just two sorted lists in ascending order attached together
2. There is a point in the list where the next number suddenly becomes less than previous
3. I only need to find the minimum element, not the index of the element and such
4. No duplicates

Approach
The obvious way is to go through the list from left to right and save what the minimum element isself.
This would require O(n) runtime and O(1) space
There is two runtimes that are faster than O(n). O(1) and O(logn). Constant runtime is impossible because
I need to look at the whole list. But maybe I can look at less than the whole listself. There are two
possible minimum elements - the very first element or the element right after the pivot. That means that
I won't need to look at the whole list, only up to pivot. But pivot could be near the end.

Another approach is binary search. Binary search is O(logn) in a normal sorted array, so maybe I Can
modify it so that it works here. If I use binary search, there are two options: The left and right
elements could be in ascending order, or the left/right could violate ascending order. Using that information,
I need to find a condition on when to move left or right side of the array. What If I compare with the first
element of the array? Because this is a sorted array that was rotated, that means that If I compare the
element I am on and the first element, it has to be either less than or greater than. No duplicates so cant be
equal. This rotated sorted array will guarantee that whatever element I find through binary search will be either
larger or smaller than first element, so if the element I am looknig at is larger, then I look to the right side
and I can basically half the array size in half. If the element I am looking at is smaller, then I look at the left
side.

[3, 4, 5, 1, 2]
 0, 1, 2, 3, 4
 midpoint = 2
 binarySearch(3, 5)
 midpoint = 4
 binarySearch(0, 3)
 midpoint = 1
 binarySearch(2, 3)
 midpoint = 2
 binarySearch(3, 3)
 midpoint = 3
 binarySearch(0, 2)
 midpoint = 1
 binarySearch(1, 2)
 midpoint = 1
 binarySearch(2, 2)
 midpoint = 2
 binarySearch(3, 2)

[4, 5, 6, 1, 2, 3]
 0, 1, 2, 3, 4, 5
 midpoint = 3
 binarySearch(0, 2)
 midpoint = 1
 binarySearch(2, 2)
 midpoint = 2
 binarySearch(3, 2)

[1, 2]
binarySearch(0, 1)
midpoint = 0
binarySearch(1, 1)
midpoint = 1
binarySearch()
'''

class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        def binarySearch(nums, start, end):
            #The end condition is if the start > end
            if start > end:
                return nums[start]
            midpoint = start + ((end - start) // 2)
            #Compare with the first element
            if nums[0] > nums[midpoint]:
                return binarySearch(nums, 0, midpoint-1)
            else:
                return binarySearch(nums, midpoint+1, end)
        #Handle edge cases
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return []
        #Handle edge case where the array is given in normal ascending order without pivot. Modified
        #Binary search will not work -> just return the first element which is the smallest
        if nums[0] < nums[len(nums)-1]:
            return nums[0]
        return binarySearch(nums, 0, len(nums)-1)
