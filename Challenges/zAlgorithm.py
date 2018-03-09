#!/usr/bin/py
# Head ends here
def zAlgorithm(s):
    z = {}
    l = 0
    r = 0
    n = len(s)
    for k in range(1,n):
        if k > r:
            l = r = k
            while r < n and s[r] == s[r-l]:
                r+=1
            z[k] = r -l
            r-=1
        else:
            k1 = k-l
            if z[k1] < r-k+1:
                z[k] = z[k1]
            else:
                while r < n and s[r] == s[r-l]:
                    r+=1
                z[k] = r-l
                r-=1
        k+=1
    return z

def stringSimilarity(a):
    answer = 0
    for i in range(len(a)):
        pat  = a[i:]
        text = pat+'$'+a
        if pat[0] == a[0]:
            z = zAlgorithm(text)
            answer = answer + z[len(pat)+1]
    return answer

# Tail starts here
if __name__ == '__main__':
    t = int(input())
    for i in range(0,t):
        a=input()
        print(stringSimilarity(a))

#Input
#2
#ababaa
#aa

