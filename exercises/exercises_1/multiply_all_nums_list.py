#!/Users/Rao/anaconda3/bin/python

from functools import reduce

def multiply(n):
    if not n:
        return 0;

    #prod = 1
    #for i in range(1, n):
    #    prod = prod * i
    #return prod

    prod = reduce(lambda acc, item: acc * item, range(1, n))
    return prod

def main():
    print(multiply(5))
    print(multiply(10))

if __name__ == '__main__':
  main()
