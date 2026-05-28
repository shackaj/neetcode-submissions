class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            item_to_check = nums[i]
            if item_to_check in seen:
                return True
            else:
                seen.add(item_to_check)

        
        return False