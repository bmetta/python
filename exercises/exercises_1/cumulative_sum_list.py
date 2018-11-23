#!/Users/Rao/anaconda3/bin/python

def cumulative_sum(nums):
    sum_nums = []
    cum = 0
    for num in nums:
        cum = cum + num
        sum_nums.append(cum)

    return sum_nums

def main():
    nums = [10, 20, 30, 40, 50, 60]
    cum_sum = cumulative_sum(nums)
    print(cum_sum)

    nums = [4, 10, 15, 18, 20]
    cum_sum = cumulative_sum(nums)
    print(cum_sum)

if __name__ == '__main__':
  main()
