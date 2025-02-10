class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        i = 0
        while i * i <= x:
            if (i + 1) * (i + 1) > x:
                return i
            i += 1
