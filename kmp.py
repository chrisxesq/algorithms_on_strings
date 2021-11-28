# python3
import sys
def compute_array(pattern):
    M = len(pattern)
    c_array = [0]*M
    length = 0
    i = 1
    while i < M:
        if pattern[i] == pattern[length]:
            length += 1
            c_array[i] = length
            i += 1
        else:
            if length != 0:
                length = c_array[length-1]
            else:
                c_array[i] = 0
                i += 1
    return c_array
    
def find_pattern(pattern, text):
    c_array = compute_array(pattern)
    M = len(pattern)
    N = len(text)
    i = 0
    j = 0
    result =[]
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == M:
            #print("found:" + str(i-j))
            result.append((i-j))
            j = c_array[j-1]
        elif i < N and pattern[j] != text[i]:
            if j !=0:
                j = c_array[j-1]
            else:
                i += 1
    return result
  if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))
