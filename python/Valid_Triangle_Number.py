class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        idx = len(nums)-1
        possible = 0
        while idx > 1:
            f_idx = 0
            b_idx = idx - 1
            while f_idx < b_idx:
                if self.checkIfTriangle(nums[f_idx], nums[b_idx], nums[idx]):
                    # print("{} {} {}".format(f_idx, b_idx, idx))
                    possible += (b_idx - f_idx) 
                    b_idx -= 1
                else:
                    f_idx += 1
            idx -= 1
        return possible   
    def checkIfTriangle(self, a, b, c):
        if a + b > c:
            return True
        else:
            False
