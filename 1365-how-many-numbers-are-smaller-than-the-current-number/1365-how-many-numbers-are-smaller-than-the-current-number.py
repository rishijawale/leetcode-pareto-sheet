class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # small = []
        
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i] > nums[j]:
        #             count+=1
        #     small.append(count)   

        # return small


        sorted_nums = sorted(nums)
        dictionary = {}

        for index, number in enumerate(sorted_nums):


            if number not in dictionary:

                dictionary[number] = index

        answer = []
        for number in nums:
            answer.append(dictionary[number])

        return answer



