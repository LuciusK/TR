# 394
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)            
            else:
                res += c
        return res

class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)

# 211
class WordDictionary(object):
    class Node:
        def __init__(self):
            self.is_word = False
            self.next = dict()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = WordDictionary.Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur_node = self.root
        for alpha in word:
            if alpha not in cur_node.next:
                cur_node.next[alpha] = WordDictionary.Node()
            cur_node = cur_node.next[alpha]
        if not cur_node.is_word:
            cur_node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        # 注意：这里要设置辅助函数
        return self.match(self.root, word, 0)

    def match(self, node, word, index):
        if index == len(word):
            return node.is_word
        alpha = word[index]
        if alpha == '.':
            for next in node.next:
                if self.match(node.next[next], word, index + 1):
                    return True
            # 注意：这里要返回
            return False
        else:
            # 注意：这里要使用 else
            if alpha not in node.next:
                return False
            # 注意：这里要使用 return 返回
            return self.match(node.next[alpha], word, index + 1)

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