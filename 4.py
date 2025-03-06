class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        new_lst = sorted(nums1 + nums2)

        if len(new_lst) % 2 == 1:
            return new_lst[len(new_lst) // 2]
        else:
            return float(new_lst[len(new_lst) // 2] + new_lst[len(new_lst) // 2 - 1]) / 2

print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
