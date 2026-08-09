class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        temp=x
        rem=0 
        rev=0
        while(x!=0):
            rem=x%10
            rev=rev*10+rem
            x=x//10 #decimal boy
        
        if temp==rev:
            return True
        else:
            return False
        