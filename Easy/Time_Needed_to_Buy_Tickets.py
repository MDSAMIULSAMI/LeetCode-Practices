class Solution1:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        seconds = 0
        idx = 0

        while tickets:
            # print(idx)
            # print(tickets, seconds)
            if tickets[idx] > 1:
                print(tickets, seconds)
                tickets.append(tickets[idx]-1)
                tickets.pop(idx)
                seconds = seconds + 1

            if tickets[idx] == 1:
                print(tickets, seconds)
                tickets.pop(idx)
                seconds = seconds + 1
        return seconds

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        seconds = 0
        idx = 0
        
        while tickets[k] > 0: 
            if tickets[idx] > 0: 
                tickets[idx] -= 1
                seconds += 1 
            idx = (idx + 1) % len(tickets)
        
        return seconds
    
test = Solution()

tickets = [5,1,1,1]
k = 0

print(test.timeRequiredToBuy(tickets, k))

tickets = [2,3,2]
k = 2
print(test.timeRequiredToBuy(tickets, k))
