# -*- coding:utf-8 -*- 

def solution(A):
    # Using SortMerge (Top-Down DP) 
    # Time Complexity : O(n log(n))
    # Space Complexity : O(n)

    def merge(left, right):
        ans = []
        while left and right:
            if left[0] < right[0]:
                ele = left.pop(0)
                if ele > 0:
                    ans.append(ele)
            else:
                ele = right.pop(0)
                if ele > 0:
                    ans.append(ele)

        return ans + left if len(left) > 0 else ans + right
    
    def sortMerge(Arr):
        if len(Arr) < 2:
            return Arr
        
        mid = len(Arr) // 2
        return merge(sortMerge(Arr[:mid]), sortMerge(Arr[mid:]))



    sortArr = sortMerge(A)
    print(sortArr)
    smallest = 1
    for item in sortArr:
        print(item)
        if item == smallest:
            smallest+= 1
        elif item < smallest:
            continue
        else:
            break
    return smallest
