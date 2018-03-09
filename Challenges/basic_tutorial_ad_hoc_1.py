import sys

def main():
    f = sys.argv[1]
    open_file = open(f,'r')
    write_file = open(f+'_output','w')
    status = 0
    while status==0:
        line = open_file.readline()
        line = int(line)
        if line != 42:
            write_file.write(str(line)+'\n')
        else:
            status = 1
    open_file.close()
    write_file.close()

if __name__ == '__main__':
    main()