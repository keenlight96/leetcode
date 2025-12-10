import math
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped_list = list(zip(position, speed))
        cars_ = sorted(zipped_list, key=lambda x: x[1], reverse=True)
        cars = sorted(cars_, key=lambda x: x[0], reverse=True)
        
        count = 0
        pin_turn = -1
        for car in cars:
            turn = (target - car[0])/ car[1]
            if turn > pin_turn:
                pin_turn = turn
                count += 1

        return count
    
    def carFleet2(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        
        
    
s = Solution()
target = 12
position = [4,4,4,4,4,4]
# position = [10,8,0,5,3]
speed = [1,2,3,4,6,6]
# speed = [2,4,1,1,3]
print(s.carFleet(target, position, speed))