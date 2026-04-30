class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            val = mid * mid

            print(mid)

            if val == x:
                return mid
            elif val > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return right
            