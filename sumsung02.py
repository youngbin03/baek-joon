#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t) {
        int n;
        cin >> n;

        vector<vector<int>> ability(n, vector<int>(3));

        //i번째 사람의 능력치 a,b,c
        for (int i = 0; i < n; ++i) {
            cin >> ability[i][0] >> ability[i][1] >> ability[i][2];
        }

        // dp 배열 초기화
        vector<vector<int>> dp(n, vector<int>(3, -1));
        vector<int> df(3,-1);
        vector<int> df2(3,-1);

        // 초기값 설정
        for (int i = 0; i < 3; ++i) dp[0][i] = ability[0][(i + 1) % 3] + ability[0][(i + 2) % 3];
        int minIndex0 = 0;
        for (int j = 0; j < 3; ++j) {
            if(dp[0][j] < dp[0][minIndex0]) minIndex0 = j;
        }
        int diff0 = min({dp[0][(minIndex0 + 1) % 3]-dp[0][minIndex0], dp[0][(minIndex0 + 2) % 3]-dp[0][minIndex0]});
        df[minIndex0] = diff0;
        // 동적 계획법을 이용하여 최소 소멸능력치 계산
        for (int i = 1; i < n; ++i) {
            int minIndex = 0;
            for (int j = 0; j < 3; ++j) {
                int sum = ability[i][(j + 1) % 3] + ability[i][(j + 2) % 3];
                dp[i][j] = min({dp[i-1][0], dp[i-1][1], dp[i-1][2]}) + sum;
                if(dp[i][j] < dp[i][minIndex]) minIndex = j;
            }
            int diff = min({dp[i][(minIndex + 1) % 3]-dp[i][minIndex], dp[i][(minIndex + 2) % 3]-dp[i][minIndex]});
            if(diff < df[minIndex] || df[minIndex] == -1){ 
                df[minIndex] = diff;
            }
            else if (diff < df2[minIndex] || df2[minIndex] == -1){
                df2[minIndex] = diff;
            }
        }

        // 최종 결과 계산
        int result = min({dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]});
        if(n<3){ 
            cout << "-1" << endl; 
        }
        else{ 
            int count = std::count(df.begin(), df.end(), -1);
            if (count == 1) {
                sort(df.begin(), df.end());
                int secondSmallest = df[1];
                cout << result + secondSmallest << endl;
            } else if (count == 2) {
                auto max1 = std::max_element(df.begin(), df.end());
                auto max2 = std::max_element(df2.begin(), df2.end());
                cout << result + *max1 + *max2 << endl;
            }
            else{
                cout << result << endl;
            }
        }
    }

    return 0;
}
