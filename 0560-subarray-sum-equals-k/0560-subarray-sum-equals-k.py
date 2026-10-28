class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum = {0: 1}
        current_sum = count = 0

        for num in nums:
            current_sum += num

            rem = current_sum - k
            if rem in prefix_sum:
                count += prefix_sum[rem]

            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return count