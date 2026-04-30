class Solution:
    def mergeSort(self, leftArr, rightArr):
            result = []
            i = j = 0
            while i < len(leftArr) and j < len(rightArr):
                if leftArr[i] < rightArr[j]:
                    result.append(leftArr[i])
                    i += 1
                else:
                    result.append(rightArr[j])
                    j += 1
            
            result.extend(leftArr[i:])
            result.extend(rightArr[j:])

            return result

    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2
        leftArr = self.sortArray(nums[:mid])
        rightArr = self.sortArray(nums[mid:])

        return self.mergeSort(leftArr, rightArr)
        
        
