#!/Users/Rao/anaconda3/bin/python
# Binomial Coefficient
# c(n, r) = c(n-1, r-1) + c(n-1, r)
# c(n, 0) = 1
# c(n, n) = 1
# 5c2 = 4c1 + 4c2
#
#    0  1   2   3   4
#  ___________________
# 0| 1, 0,  0,  0,  0]
# 1| 1, 1,  0,  0,  0]
# 2| 1, 2,  1,  0,  0]
# 3| 1, 3,  3,  1,  0]
# 4| 1, 4,  6,  4,  1]
# 5| 1, 5, 10, 10,  5]
#

#  Time complexity = 
# Space complexity = 
def compute_ncr(n, r):
    if n == r or r == 0:
        return 1
    return compute_ncr(n-1, r-1) + compute_ncr(n-1, r)

#  Time complexity = O(n*r)
# Space complexity = O(n*r)
def compute_ncr_dp(n, r):
    lookup = [[0 for j in range(r + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, r) + 1):
            # diagonal (ncn=1) and first column(nc0 = 1)
            if j == 0 or j == i:
                lookup[i][j] = 1
            else:
                lookup[i][j] = lookup[i - 1][j - 1] + lookup[i - 1][j]

    #for row in lookup:
    #    print(row)
    return lookup[n][r]

# Space optimized version
#  Time complexity = O(n*r)
# Space complexity = O(r)
#def compute_ncr_dp(n, r):

def main():
    print(compute_ncr(50, 25))
    print(compute_ncr_dp(50, 25))

if __name__ == '__main__':
  main()
