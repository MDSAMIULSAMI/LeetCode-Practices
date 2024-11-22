class RecentCounter1:

    def __init__(self):
        self.store = []

    def ping(self, t: int) -> int:
        counter = 1
        self.store.append(t)

        for ping in self.store:
            if ping in range(t-3000, t):
                counter = counter + 1
        return counter
        
class RecentCounter:

    def __init__(self):
        self.store = []

    def ping(self, t: int) -> int:
        self.store.append(t)
        while self.store[0] < t - 3000:
            self.store.pop(0)
        return len(self.store)

# Your RecentCounter object will be instantiated and called as such:
recentCounter = RecentCounter()
print(recentCounter.ping(1))
print(recentCounter.ping(100))
print(recentCounter.ping(3001))
print(recentCounter.ping(3002))