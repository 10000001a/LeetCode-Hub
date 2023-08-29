class RecentCounter:
    requests= []

    #  1 2 3 4 5 6 7 8

    def __init__(self):
        # print('init')
        self.requests.clear()
        return
        
    def ping(self, t: int) -> int:
        # print('t: ', t)
        self.requests.append(t)

        min = t - 3000
        max = t

        # print('min: ', self.b_search_index(min))
        # print('max: ', self.b_search_index(max))

        return self.b_search_index(max) - self.b_search_index(min) + 1

    def b_search_index(self, t: int) -> int:
        # print('requests: ', self.requests)
        start, end = 0, len(self.requests) - 1

        if t <= self.requests[start]:
            return start
        
        if t >= self.requests[end]:
            return end

        while end - start > 1:
            half = (start + end) // 2

            if t < self.requests[half]:
                end = half
            elif t > self.requests[half]:
                start = half
            else:
                return half
        
        return end





# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)