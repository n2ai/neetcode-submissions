class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = right
        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    
                    currCap = cap
                
                currCap -= w 
            
            return True

        while left <= right:
            cap = (left + right) // 2
            if canShip(cap):
                res = min(res, cap)
                right = cap - 1
            else:
                left = cap + 1
        
        return res