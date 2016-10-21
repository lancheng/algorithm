# encoding: utf-8
import heapq
class Solution:
    def find_mid_number(self, l):
        h_q = []

        length = len(l)

        mid = length / 2 + 1

        for i in l:
            if len(h_q) < mid:
                heapq.heappush(h_q, i)
            elif i > (h_q[0]):
                heapq.heappushpop(h_q, i)

        return h_q[0]


if __name__ == '__main__':
    print Solution().find_mid_number(map(int, raw_input().split()))
