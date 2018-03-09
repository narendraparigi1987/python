import sys

def sumoflists(l1,l2):
    sum = []
    carry = 0
    for i in range(len(l1)):
        '''
        divmod returns tuple first value with quotient and second value with remainder
        '''
        carry,val = divmod((int(l1[i])+int(l2[i])+int(carry)),10)
        if i == len(l1)-1:
            sum.append((int(l1[i])+int(l2[i])+int(carry)))
        else:
            sum.append(val)
    return '->'.join([str(sum[i]) for i in range(len(sum))])

def main():
    list_list = [[]]
    in_put = sys.argv[1]
    for i in in_put.split('+'):
        for j in i.split('('):
            for p in j.split(')'):
                if len(p)>=2:
                    list_list.append(p.split('->'))
    result = sumoflists(list_list[1],list_list[2])
    print ('sum of two numbers {} is {}'.format(in_put,result))

if __name__ =='__main__':
    main()