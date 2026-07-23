# Last updated: 23/07/2026, 10:59:26
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            if n in seen:
                return False  # cycle detected
            
            seen.add(n)
            
            # calculate sum of squares of digits
            n = sum(int(digit) ** 2 for digit in str(n))
        
        return True