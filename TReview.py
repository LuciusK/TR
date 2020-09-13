# rabin-karp
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        d = 256
        q = 9997
        n = len(haystack)
        m = len(needle)
        h = pow(d, m - 1) % q
        p = 0
        t = 0

        if m > n:
            return -1

        for i in range(m):
            p = (d * p + ord(needle[i])) % q
            t = (d * t + ord(haystack[i])) % q
        for s in range(n - m + 1):
            if p == t:
                match = True
                for i in range(m):
                    if needle[i] != haystack[s + i]:
                        match = False
                        break
                if match:
                    return s
            if s < n - m:
                t = (t - h * ord(haystack[s])) % q
                t = (t * d + ord(haystack[s + m])) % q
                t = (t + q) % q
        return -1

# 205
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict.keys():
                if t[i] in dict.values():
                    return False
                dict[s[i]] = t[i]
            else:
                if dict[s[i]] != t[i]:
                    return False
        return True

# 44
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        nrow = len(p) + 1
        ncol = len(s) + 1

        dp = [[False for _ in range(ncol)] for _ in range(nrow)]
        dp[0][0] = True

        if p.startswith("*"):
            dp[1] = [True] * ncol

        for m in range(1, nrow):
            path = False
            for n in range(1, ncol):
                if p[m - 1] == "*":
                    if dp[m - 1][0] == True:
                        dp[m] = [True] * ncol
                    if dp[m - 1][n] == True:
                        path = True
                    if path:
                        dp[m][n] = True
                elif p[m - 1] == "?" or p[m - 1] == s[n - 1]:
                    dp[m][n] = dp[m - 1][n - 1]
        return dp[-1][-1]

# 10
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if not s and len(p) == 1:
            return False
        
        nrow = len(s) + 1
        ncol = len(p) + 1

        dp = [[False for c in range(ncol)] for _ in range(nrow)]
        dp[0][0] = True
        dp[0][1] = False
        for c in range(2, ncol):
            j = c - 1
            if p[j] == "*":
                dp[0][c] = dp[0][c - 2]
        
        for r in range(1, nrow):
            i = r - 1
            for c in range(1, ncol):
                j = c - 1
                if s[i] == p[j] or p[j] == ".":
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == "*":
                    if p[j - 1] == s[i] or p[j - 1] == ".":
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:
                        dp[r][c] = dp[r][c - 2]
        return dp[-1][-1]

# 5
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        
        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True
        
        for j in range(1, size):
            for i in range(0, j):
                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i + 1][j - 1])
                # if s[i] == s[j]:
                #     if j - i < 3:
                #         dp[i][j] = True
                #     else:
                #         dp[i][j] = dp[i + 1][j - 1]
                # else:
                #     dp[i][j] = False
                
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]

    def longestPalindrome1(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        
        max_len = 1
        res = s[0]
        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)

            cur_max_sub = palindrome_odd if odd_len > even_len else palindrome_even
            if max(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub
        return res
    
    def __center_spread(self, s, size, left, right):
        i = left
        j = right
        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j], j - i - 1
        