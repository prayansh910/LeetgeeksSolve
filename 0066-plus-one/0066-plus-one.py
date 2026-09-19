class Solution(object):
    def plusOne(self, digits):
        input_int=int("".join(map(str,digits)))
        sum1=input_int+1
        final_list=[int(x) for x in (str(sum1))]
        return final_list