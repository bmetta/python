#!/Users/Rao/anaconda3/bin/python
# [1, 0, 5, 0, 0, 2, 0, 4, 3, 0, 6]
#  i                             j
#     i
# [1, 6, 5, 0, 0, 2, 0, 4, 3, 0, 0]
#        i                    j
#           i              j
# [1, 6, 5, 3, 0, 2, 0, 4, 0, 0, 0]
#              i        j
# [1, 6, 5, 3, 4, 2, 0, 0, 0, 0, 0]
#                 i  j

def move_zeros_listend(nums):
    i = 0;
    j = len(nums) - 1
    while (i < j):
        if (nums[i] != 0):
            i = i + 1
        if (nums[j] == 0):
            j = j - 1

        if (i < j and nums[i] == 0 and nums[j] != 0):
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            j = j - 1
    print(i, j)

def main():
    nums = [1, 0, 5, 0, 0, 2, 0, 4, 3, 0, 6]
    move_zeros_listend(nums)
    print(nums)

    nums = [1, 5, 2, 4, 3, 0, 0, 0, 0, 0]
    move_zeros_listend(nums)
    print(nums)

if __name__ == '__main__':
  main()
