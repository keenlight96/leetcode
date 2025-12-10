from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    prefix = 1
    suffix = [1]
    products = []
        
    for i in range(len(nums) - 1, 0, -1):
        suffix.append(suffix[-1] * nums[i])
    
    products.append(suffix[-1])
    for i in range(0, len(nums) - 1):
        prefix = prefix * nums[i]
        products.append(prefix * suffix[len(suffix) - 2 - i])
        
    return products

nums = [1,2,3,4]
print(productExceptSelf(nums))