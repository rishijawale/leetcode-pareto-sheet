class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums = sorted(nums)
        # i = 0
        # j = len(nums)-1

        # while i < j:
        #     current_sum = nums[i] + nums[j]

        #     if current_sum == target:
        #         return [i, j]

        #     elif current_sum < target:
        #         i += 1

        #     else:
        #         j -= 1


        # nums = sorted(nums)
        # i = 0
        # j = len(nums)-1

        # while i < j:
        #     current_sum = nums[i]+ nums[j]    

        #     if current_sum == target:
        #         return [i,j]   

        #     elif current_sum > target:
        #         j-=1

        #     else:
        #         i+=1

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):

                # if i == j:
                #     return [i, j+1]

                if nums[i] + nums[j] == target:
                    return [i, j]

                
            
                

                




    
   