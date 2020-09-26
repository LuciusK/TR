# 81
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return True
            
            if nums[mid] == nums[l]:
                l += 1
            elif nums[mid] == nums[r]:
                r -= 1
            elif nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

# 153
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

# 51
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        if n == 0:
            return res
        
        col = set()
        slave = set()
        master = set()
        stack = []

        self.__backtracking(0, n, col, slave, master, stack, res)
        return res
    
    def __backtracking(self, row, n, col, slave, master, stack, res):
        if row == n:
            board = self.__convert2board(stack, n)
            res.append(board)
            return
        
        for i in range(n):
            if i not in col and row + i not in slave and row - i not in master:
                stack.append(i)
                col.add(i)
                slave.add(row+i)
                master.add(row-i)

                self.__backtracking(row+1, n, col, slave, master, stack, res)

                master.remove(row-i)
                slave.remove(row+i)
                col.remove(i)
                stack.pop()
    
    def __convert2board(self, stack, n):
        return ["." * stack[i] + "Q" + "." * (n - stack[i] - 1) for i in range(n)]
        
    def solveNQueens1(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])
        result = []
        DFS([], [], [])
        return [['.' * i  + 'Q' + '.' * (n-i-1) for i in sol] for sol in result]

# 52
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return 
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count

    def DFS(self, n, row, cols, lfs, rfs):
        if row >= n:
            self.count += 1
            return 
        
        bits = (~(cols | lfs | rfs)) & ((1 << n) - 1) # 得到当前所有的空位

        while bits:
            p = bits & -bits # 取到最低位的1
            bits = bits & (bits - 1) # 表示在p位置上放入皇后
            self.DFS(n, row + 1, cols | p, (lfs | p) << 1, (rfs | p) >> 1)
            # 不需要revert  cols, lfs, rfs 的状态

# 45
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        maxPosition = 0#能力最大范围
        steps = 0
        for i in range(len(nums)-1):#不取最后一位是因为不让下面i==end的条件成立，也就是不让steps再加1
            maxPosition = max(maxPosition, nums[i] + i)
            if i == end:#到了倒数第二个位置之后，因为非空限制，肯定能到最后一个位置
                end = maxPosition#倘若到了倒数第二位都没有更新end，那也不用再更新了，因为max一定大于等于最后一位
                steps += 1
        return steps

# 69
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left = 1
        right = x // 2#一般来说大于4的数，其二分之一的平方都小于他本身

        while left < right:
            mid = (left + right + 1) >> 1#使用右中位数会防止进入死循环
            square = mid * mid

            if square > x:#一步步紧逼目标数，直到取得square稍微小于等于目标数的数
                right = mid - 1
            else:
                left = mid
        return left
    
    def mySqrt1(self, x: int) -> int:#可以使用牛顿迭代法的原因是平方根是x²-a的解
        if x < 0:
            raise Exception('不能输入负数')
        if x == 0:
            return 0
        
        cur = 1
        while True:#迭代公式为x = x - f(x)/f'(x)
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)