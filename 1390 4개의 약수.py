class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            # 약수를 담는 리스트
            divisor = []
            # num^(1/2) 범위 내에서
            for i in range(1, floor(sqrt(num))+1):
                if num % i == 0:
                    # 제곱수 방지
                    if (num // i) != i:
                        divisor.append(num // i)
                        divisor.append(i)
                    else:
                        divisor.append(i)
                # 약수가 4보다 많으면 건너뛰기
                if len(divisor) > 4:
                    break
            print(divisor)
            if len(divisor) == 4:
                ans += sum(divisor)
        return ans