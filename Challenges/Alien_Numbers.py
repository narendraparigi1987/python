import sys
import re

def process(num,src,tgt):
    n = 0
    for c in num:
        n = n*len(src)+src.find(c)
    res=''
    while n:
        res = tgt[n%len(tgt)]+res
        n/=len(tgt)
    return res

def main():
    f = sys.argv[1]
    open_file = open(f,'r')
    #lines = open_file.readlines()[1:]
    lines = open_file.readlines()
    firstline = lines.pop(0)
    write_file = open(f+'_output','w')
    for i, line in enumerate(lines):
        (num, src, tgt) = line.split(' ')
        res = process(num.strip(), src.strip(), tgt.strip())
        write_file.write('Case #{}: {}\n'.format(i+1,res))
    open_file.close()
    write_file.close()

if __name__ == '__main__':
    main()