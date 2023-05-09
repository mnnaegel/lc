# essentially counting number of subarrays with unique characters, such that M=# of unique characters, n = length of string comprised of unique characters with repeats
from collections import defaultdict

def getNumUnique(n,m):
    dp = [0 for i in range(m+1)]
    dp[1] = 1
    for i in range(m+1):
        dp[i] = i + dp[i-1]
    
    # like coins problem see all available 

def generateSample(n,m):
    # 1,2,...m,1,2...m until len(arr) == n
    i = 1
    ln = 0
    sample = []
    while ln < n:
        sample.append(i)
        i += 1
        if i == m+1:
            i = 1
        ln += 1
    return sample

def main():
    n,m,k = map(int, input().split())
    sample = generateSample(n,m);
    # print(sample)
    res = getNumUnique(n,m)
    # print(res)
    if res == k:
        print(*sample)
    else:
        print(-1)
    
if __name__ == "__main__":
    main()