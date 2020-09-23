# 231
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & n - 1 == 0

# 190
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31, -1, -1):
            res |= (((n >> (31 - i)) & 1) << i)
        
        return res

    def reverseBits1(self, n: int) -> int:
        res = 0
        count = 0
        while count < 32:
            res <<= 1
            res |= n & 1
            n >>= 1
            count += 1
        
        return res

# 55
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums == [0]:
            return True
        maxDist = 0
        end_index = len(nums) - 1
        for i, jump in enumerate(nums):
            if maxDist >= i and i + jump > maxDist:#最远距离大过终点index
                maxDist = i + jump
                if maxDist >= end_index:
                    return True
        
        return False

# 455
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort()
        s.sort()

        g_length = len(g)
        s_length = len(s)

        i = 0
        j = 0
        while i < g_length and j < s_length:
            if g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1

        return res

# 148
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next 
        midnext, slow.next = slow.next, None
        left, right = self.sortList(head), self.sortList(midnext)

        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next 
            else:
                h.next, right = right, right.next 
            h = h.next 
        h.next = left if left else right 
        return res.next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        while h:
            h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        while intv < length:
            pre, h = res, res.next 
            while h:
                h1, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                if i:
                    break
                h2, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                c1, c2 = intv, intv - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next 
                pre.next = h1 if c1 else h2

                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2
        return res.next

# 22
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next 
        return latter