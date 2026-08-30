class TimeMap:
    def __init__(self):
        self.map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))
            
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        arr = self.map[key]
        l = 0
        h = len(arr) - 1
        m = 0
        while l <= h:
            m = (l + h) // 2
            if arr[m][0] == timestamp:
                return arr[m][1]
            elif arr[m][0] > timestamp:
                h = m - 1
            else:
                l = m + 1

        if arr[m][0] > timestamp:
            if m >= 1:
                return arr[m - 1][1]
            else:
                return ""
        return arr[m][1]


