class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count = 0

        for x in arr1:
            left = 0
            right = len(arr2)

            while left < right:
                mid = (left + right) // 2

                if arr2[mid] < x - d:
                    left = mid + 1
                else:
                    right = mid

            if left == len(arr2) or arr2[left] > x + d:
                count += 1

        return count   