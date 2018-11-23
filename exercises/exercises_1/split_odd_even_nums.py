#!/Users/Rao/anaconda3/bin/python

def split_odds_evens(nums):
    odds = []
    evens = []
    for num in nums:
        if num % 2:
            odds.append(num)
        else:
            evens.append(num)

    return odds, evens

def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    odds, evens = split_odds_evens(nums)
    print(odds)
    print(evens)

if __name__ == '__main__':
  main()
