from collections import defaultdict, deque


class TimeMap:

    def __init__(self):
        self.d = defaultdict(dict)
        """ 
        d: {
            key1: {
                time: [ts1, ts2, ...],
                ts1: value1,
                ts2: value2,
                ...
            },
            ...
        }
        """
    
    def search(self, arr: deque, num: int):
        l = 0
        r = len(arr) - 1
        m = (l + r) // 2
        while l <= r:
            if arr[m] == num:
                return (True, m)
            elif arr[m] > num:
                r = m - 1
            else:
                l = m + 1
            m = (l + r) // 2
        return (False, m)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.d[key]:
            # Add timestamp by ascending order
            if timestamp > self.d[key]["time"][-1]:
                self.d[key]["time"].append(timestamp)
            elif timestamp < self.d[key]["time"][0]:
                self.d[key]["time"].appendleft(timestamp)
            else:
                isExist, idx = self.search(self.d[key]["time"], timestamp)
                if not isExist:
                    self.d[key]["time"].insert(idx + 1, timestamp)
                
            self.d[key] |= {
                timestamp: value
            }
        else:
            self.d[key] = {
                "time": deque([timestamp]),
                timestamp: value
            }

    def get(self, key: str, timestamp: int) -> str:
        if not self.d[key] or self.d[key]["time"][0] > timestamp:
            return ""
        else:
            isExist, idx = self.search(self.d[key]["time"], timestamp)
            ts = self.d[key]["time"][idx]
            return self.d[key][ts]

class TimeMap2:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value , timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.dic.get(key , [])
        l , r = 0 , len(values) - 1
        while l <= r :
            mid = (l + r) >> 1
            if values[mid][1] <= timestamp:
                l = mid + 1
                res = values[mid][0]
            else:
                r = mid - 1
        return res

timeMap = TimeMap2()
timeMap.set("foo", "bar", 1)  # store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap.get("foo", 1))         # return "bar"
print(timeMap.get("foo", 3))       # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4) # store the key "foo" and value "bar2" along with timestamp = 4.
print(timeMap.get("foo", 4))    # return "bar2"
print(timeMap.get("foo", 5))         # return "bar2"