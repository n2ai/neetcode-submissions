class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashMap = {}
        for val in strs:
            sortedVal = ''.join(sorted(val))
            if sortedVal not in hashMap:
                hashMap[sortedVal] = [val]
            else:
                hashMap[sortedVal].append(val)
        
        for val in hashMap.values():
            ans.append(val)
        
        return ans