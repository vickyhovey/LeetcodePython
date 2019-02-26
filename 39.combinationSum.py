class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        result = []
        self.combination(candidates, target, [], result)
        return result
    
    def combination(self, candidates, target, current, result):
        s = sum(current) if current else 0
        if s > target:
            return
        elif s == target:
            result.append(current)
        else:
            for i, v in enumerate(candidates):
                self.combination(candidates[i:], target, current + [v], result)
    
if __name__ == "__main__":
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
