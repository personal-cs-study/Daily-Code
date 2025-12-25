# 좌측 절반이 정렬되었을 경우: 목표가 중간값보다 작거나 같으므로
#   목표가 좌측에 존재할 경우: 목표가 좌측보다는 크고 중간보다는 작으므로 우측을 중간-1로 교체
#   아니면: 목표가 우측에 존재하므로 좌측을 중간+1로 교체
# 우측 절반이 정렬되었을 경우: 목표가 중간값보다 크므로
#   목표가 우측에 존재할 경우: 목표가 중간보다는 크고 우측보다는 작으므로 좌측을 중간+1로 교체
#   아니면: 목표가 좌측에 존재하므로 우측을 중간-1로 교체
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target and target <= nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m] <= target and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1