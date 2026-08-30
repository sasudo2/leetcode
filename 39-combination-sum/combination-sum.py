class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        outputs = []
        for x in candidates:
            new_target = target - x
            if new_target < 0:
                continue
            elif new_target == 0:
                outputs.append([x])
            else:
                new_candidates = []
                for k in candidates:
                    if k <= new_target:
                        new_candidates.append(k)

                combinations = self.combinationSum( new_candidates, new_target)

                for combination in combinations:
                    if combination:
                        combination.append(x)
                        outputs.append(combination)
        outputs = [list(t) for t in set(tuple(sorted(output)) for output in outputs)]
        return outputs
