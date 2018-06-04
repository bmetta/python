#!/Users/Rao/anaconda3/bin/python
import time

# using for loop
def flatten_forloop(l):
    if not l:
        return []

    flat_list = []
    for item in l:
        if type(item) is list:
            flat_list.extend(flatten_forloop(item))
        else:
            flat_list.append(item)
    return flat_list

# using list slicing
def flatten(l):
    if not l:
        return []

    if type(l[0]) is list:
        return flatten(l[0]) + flatten(l[1:])

    return [l[0]] + flatten(l[1:])

def main():
    print(flatten([[1,1],2,[1,1]]))
    print(flatten([1,[4,[6]]]))

    start = time.time()
    print(flatten_forloop([0, 1, 2, [3, 4, [5, 6, [7, 8]]]]))
    print("time to run %s ms" % (time.time() * 1000 - start * 1000))
    start = time.time()
    print(flatten([0, 1, 2, [3, 4, [5, 6, [7, 8]]]]))
    print("time to run %s ms" % (time.time() * 1000 - start * 1000))

if __name__ == '__main__':
  main()
