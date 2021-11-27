# python3
import sys


def build_suffix_array(text):
  n = len(text)
  arr=[ [i,text[i:]] for i in range(n)]
  suffix_arr = sorted(arr, key=lambda elem:elem[1])
  ans=[]
  for i in range(n):
    ans.append((suffix_arr[i][0]+n)%n)
  return ans


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
