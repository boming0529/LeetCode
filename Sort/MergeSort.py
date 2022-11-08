


class Algorithm(object):
    def __merge(self, left, right):
        ans = []
        while left and right:
            ans.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        return ans+left if len(left) else ans+right

    def splitArray(self, array):
        if len(array) < 2: return array
        mid = len(array) // 2
        LHS, RLS = array[:mid], array[mid:]
        return self.__merge(self.splitArray(LHS), self.splitArray(RLS))




A = [1,1,4,7,9,9,8,9]
# find otherwise
# if len(A) < 2: return A[0]

al = Algorithm()
sortArray = al.splitArray(A)
print(sortArray)
fast, slow, diff = 1, 0, 0
for _ in range(len(A)//2 + 1):
    if sortArray[fast+diff] == sortArray[slow+diff]:
        sortArray.pop(diff)
        sortArray.pop(diff)
    else:
        diff += 1


print(sortArray)


