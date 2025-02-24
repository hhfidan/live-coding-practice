class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        carry=1
        for i in range(len(digits)):
            digits[i] += carry
            if digits[i] == 10:
                digits[i] = 0
                carry=1
            else:
                carry=0
        if carry ==1:
            digits.append(carry)
            
        digits.reverse()
        return digits
