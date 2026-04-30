## map will look like this:
#{key : {timestamp: value}}
class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
           self.hashMap[key] = []
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hashMap:
            return ''
        searchObject = self.hashMap[key]
        l = 0
        r = len(searchObject) - 1

        while l <= r:
            m = (l + r) // 2
            
            if searchObject[m][0] == timestamp:
                return searchObject[m][1]
            elif searchObject[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1
        if searchObject[r][0] > timestamp:
            return ''
        return searchObject[r][1]

        
        return val

