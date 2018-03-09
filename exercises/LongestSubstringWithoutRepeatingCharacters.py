import sys

class Solution(object):
    def __init__(self,s):
        self.s = s
    
    def getString(self):
        return self.s
    
    def lengthOfLongestSubstring(self):
        s = self.getString()
        new_s = ''
        for i in range(len(s)):
            if i ==0:
                new_s = new_s+s[i]
            elif s[i] not in new_s: 
                new_s = new_s+s[i]
        return (new_s,len(new_s))

def main():
    string = sys.argv[1]
    s1 = Solution(string)
    print ('sting supplied:',s1.getString())
    new_s,new_l = s1.lengthOfLongestSubstring()
    print ('Absolute string length:',new_l)
    print ('new string length:',new_s)

if __name__ == '__main__':
    main()