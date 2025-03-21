class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # STRATEGY
        # Start at the end of each array, sort from largest to smallest

        p1, p2 = m - 1, n - 1  # pointer to the next element to evaluate in each array
        i = m + n - 1  # pointer to the next available slot in the combined array

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1

        while p2 >= 0:
            nums1[i] = nums2[p2]
            p2 -= 1
            i -= 1
