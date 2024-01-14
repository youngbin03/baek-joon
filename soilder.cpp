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
        vector<vector<int>> min_move(3, vector<int>(3, -1));

        // 초기값 설정
        for (int i = 0; i < 3; ++i) dp[0][i] = ability[0][(i + 1) % 3] + ability[0][(i + 2) % 3];
        int minIndex0 = 0;
        for (int j = 0; j < 3; ++j) {
            if(dp[0][j] < dp[0][minIndex0]) minIndex0 = j;
        }
        min_move[minIndex0][(minIndex0 + 1) % 3] = dp[0][(minIndex0 + 1) % 3]-dp[0][minIndex0];
        min_move[minIndex0][(minIndex0 + 2) % 3] = dp[0][(minIndex0 + 2) % 3]-dp[0][minIndex0];
        
        // 동적 계획법을 이용하여 최소 소멸능력치 계산
        for (int i = 1; i < n; ++i) {
            int minIndex = 0;
            for (int j = 0; j < 3; ++j) {
                int sum = ability[i][(j + 1) % 3] + ability[i][(j + 2) % 3];
                dp[i][j] = min({dp[i-1][0], dp[i-1][1], dp[i-1][2]}) + sum;
                if(dp[i][j] < dp[i][minIndex]) minIndex = j;
            }
            
            //int diff = min({dp[i][(minIndex + 1) % 3]-dp[i][minIndex], dp[i][(minIndex + 2) % 3]-dp[i][minIndex]});
            if(dp[i][(minIndex + 1) % 3] < dp[i][(minIndex + 2) % 3]){ //두 차이 값중  더 작은 값사용
                if((dp[i][(minIndex + 1) % 3]-dp[i][minIndex]) < min_move[minIndex][(minIndex + 1) % 3] || min_move[minIndex][(minIndex + 1) % 3] == -1){
                    min_move[minIndex][(minIndex + 1) % 3] = (dp[i][(minIndex + 1) % 3]-dp[i][minIndex]);
                    if(min_move[minIndex][(minIndex + 2) % 3] == -1) min_move[minIndex][(minIndex + 2) % 3] = (dp[i][(minIndex + 2) % 3]-dp[i][minIndex]);
                }
                else if((dp[i][(minIndex + 2) % 3]-dp[i][minIndex]) < min_move[minIndex][(minIndex + 2) % 3] || min_move[minIndex][(minIndex + 2) % 3] == -1){
                    min_move[minIndex][(minIndex + 2) % 3] = (dp[i][(minIndex + 2) % 3]-dp[i][minIndex]);
                }
            }
            else{
                if((dp[i][(minIndex + 2) % 3]-dp[i][minIndex]) < min_move[minIndex][(minIndex + 2) % 3] || min_move[minIndex][(minIndex + 2) % 3] == -1){
                    min_move[minIndex][(minIndex + 2) % 3] = (dp[i][(minIndex + 2) % 3]-dp[i][minIndex]);
                }
                else if((dp[i][(minIndex + 1) % 3]-dp[i][minIndex]) < min_move[minIndex][(minIndex + 1) % 3] || min_move[minIndex][(minIndex + 1) % 3] == -1){
                    min_move[minIndex][(minIndex + 1) % 3] = (dp[i][(minIndex + 1) % 3]-dp[i][minIndex]);
                }
            }
        }
        
        // 최종 결과 계산
        int result = min({dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]});
        vector<bool> isRowAllMinusOne(3, false);
        if(n<3){ 
            cout << "-1" << endl; 
        }
        else{ 
            int row_count = 0;
            for(int i = 0; i < min_move.size(); ++i){
                bool isAllMinusOne = true;
                for (int value : min_move[i]) {
                    if (value != -1) {
                        isAllMinusOne = false;
                        break;
                    }
                }
                if (isAllMinusOne) {
                    row_count++;
                }
                isRowAllMinusOne[i] = isAllMinusOne;
            }
            if (row_count == 1) {
                if(isRowAllMinusOne[0]){
                    if(min_move[1][0] < min_move[2][0] ? cout << result + min_move[1][0] << endl : cout << result + min_move[2][0] << endl);
                }
                if(isRowAllMinusOne[1]){
                    if(min_move[0][1] < min_move[2][1] ? cout << result + min_move[0][1] << endl : cout << result + min_move[2][1] << endl);
                }
                if(isRowAllMinusOne[2]){
                    if(min_move[0][2] < min_move[1][2] ? cout << result + min_move[0][2] << endl : cout << result + min_move[1][2] << endl);
                }
            } else if (row_count == 2) {
                for(int i = 0; i < 3; i++){
                    if(isRowAllMinusOne[i] == false){
                        cout << min_move[i][(i + 1) % 3] + min_move[i][(i + 2) % 3] + result << endl;
                    }
                }
            }
            else{
                cout << result << endl;
            }
        }
    }

    return 0;
}
