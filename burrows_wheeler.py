# python3
import sys

def BWT(text):
    n = len(text)
    arr=[ [i,text[i:]] for i in range(n)]
    suffix_arr = sorted(arr, key=lambda elem:elem[1])
    ans=''
    for i in range(n):
        ans +=(text[(suffix_arr[i][0]-1+n)%n])
    return ans
if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
