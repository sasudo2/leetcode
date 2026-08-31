class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion depth
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Prune: since sorted, no point continuing further
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])  # i+1: each number used once
                path.pop()

        backtrack(0, target)
        return result
