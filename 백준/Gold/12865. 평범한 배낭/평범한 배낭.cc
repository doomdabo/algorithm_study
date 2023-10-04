#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int n, k;
int w[101], v[101];
int dp[101][100002];
int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);

	cin >> n >> k;
	for (int i = 1; i <= n; i++ ) {
		cin >> w[i] >> v[i];
	}
	for (int limit = 1; limit <= k; limit++) {
		for (int row = 1; row <= n; row++) {
			if (w[row] > limit) { //만약 짐 무게가 더 큰 경우 가방에 못넣음
				dp[row][limit] = dp[row - 1][limit];
			}
			else {
				//짐 무게가 더 작은경우 가방에 넣을 수 있음
				//이때, 해당 짐을 넣을 지, 아니면 해당 짐을 넣지 않은 이전의 상태가 최대인지 고려해야함
				dp[row][limit] = max(dp[row - 1][limit],v[row] + dp[row - 1][limit - w[row]]);
			}
		}
	}

	cout << dp[n][k];
	
}