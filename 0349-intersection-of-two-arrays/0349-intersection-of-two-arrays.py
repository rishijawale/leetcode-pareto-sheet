class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        

        setA = set(nums1)
        result = set()

        for x in nums2:
            if x in setA:
                result.add(x)

        return list(result)