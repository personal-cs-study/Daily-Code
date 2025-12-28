class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int ans = 0;
        // 우측 한계를 미리 설정
        int last_neg = cols - 1;
        for (int i = 0; i < rows; i++) {
            // 모서리 부분 체크: 첫 원소가 음수면 모두 음수
            if (grid[i][0] < 0) {
                ans += cols;
                continue;
            }
            // 모서리 부분 체크: 마지막 원소가 양수면 음수 없음
            if (grid[i][cols-1] > 0) {
                continue;
            }
            // 이진탐색으로 음수가 존재하는지 체크
            int l = 0, r = last_neg;
            while (l <= r) {
                int m = l + (r-l)/2;
                if (grid[i][m] < 0) {
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            }
            ans += (cols - l);
            last_neg = l;
        }
        return ans;
    }
};