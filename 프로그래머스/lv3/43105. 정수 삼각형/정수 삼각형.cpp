#include <string>
#include <vector>
int dp[501][501];
using namespace std;
int solution(vector<vector<int>> triangle) {
    int answer = -1;
    dp[0][0]=triangle[0][0];
    for(int i=1;i<triangle.size();i++){
        for(int j=0;j<i+1;j++){
            if(j==0){
                dp[i][j] = dp[i-1][j] + triangle[i][j];
            }
            if(i==j){
                dp[i][j] = dp[i-1][j-1] + triangle[i][j];                
            }
            else{
                dp[i][j] = max(dp[i-1][j-1]+triangle[i][j], dp[i-1][j] + triangle[i][j]);
            }
        }
    }
    for(int i=0;i<triangle.size();i++){
        if(dp[triangle.size()-1][i]>answer){
            answer = dp[triangle.size()-1][i];
        }
    }
    return answer;
}