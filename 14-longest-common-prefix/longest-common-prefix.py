class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pointer = 0
        prefix = ""
        check_max = min([x for x in map(lambda y: len(y), strs)])
        joined = tuple(zip(strs[:-1], strs[1:]))
        while pointer < check_max and all(x[pointer] == y[pointer] for x, y in joined):
            prefix += strs[0][pointer]
            pointer += 1
        
        return prefix
