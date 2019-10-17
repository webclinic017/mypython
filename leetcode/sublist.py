class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A):
        if not A:
            return 0
        B=len(A)
        C=sum(A)
        combinations = []
        self.dfs(A, 0, [], combinations, B,C)
        n = 0
        return combinations

    def dfs(self, nums, index, combination, combinations, B,C):
        if len(combination) ==B/2:
            combinations.append(list(combination))

        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i +1, combination, combinations, B,C)
            combination.pop()

testlist=[1,2]

k=Solution()
x=k.solve(testlist)
print x



