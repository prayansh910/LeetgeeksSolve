class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]

        def backtrack(start,path,rem):
            if rem==0:
                result.append(path[:])
                return
            if rem<0:
                return

            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i,path,rem-candidates[i])
                path.pop()

        backtrack(0,[],target)
        return result
        