#!/Users/Rao/anaconda3/bin/python

def intersection(nums1, nums2):
    if not nums1 or not nums2:
      return []

    nums_map = {}
    for num in nums1:
        count = nums_map.get(num, 0)
        nums_map[num] = count + 1
    
    res = []
    for num in nums2:
        count = nums_map.get(num, 0)
        if count != 0:
            res.append(num)
            nums_map[num] = count - 1

    return res

def main():
    nums1 = [1, 2, 2, 1]; nums2 = [2, 2]
    ret = intersection(nums1, nums2)
    print(ret)

    nums1 = []; nums2 = []
    ret = intersection(nums1, nums2)
    print(ret)

if __name__ == '__main__':
    main()
