#!/Users/Rao/anaconda3/bin/python
import time

def create_list_forloop(n):
    if n == 0:
        return []

    nums = []
    start = time.time()
    for i in range(n):
        nums.append(i)
    print("For loop execution time % sec" % (time.time() - start))

def create_list_listcomprehension(n):
    if n == 0:
        return []

    start = time.time()
    nums = [i for i in range(n)]
    print("list comprehension execution time % sec" % (time.time() - start))

def create_list_mapfunction(n):
    if n == 0:
        return []

    start = time.time()
    #nums = [x for x in map(lambda x: x, range(n))]
    #nums = list(map(lambda x: x, range(n)));
    nums = map(lambda x: x, list(range(n)))
    print("map function execution time % sec" % (time.time() - start))

def main():
    create_list_forloop(1000000)
    create_list_listcomprehension(1000000)
    create_list_mapfunction(1000000)

if __name__ == '__main__':
  main()
