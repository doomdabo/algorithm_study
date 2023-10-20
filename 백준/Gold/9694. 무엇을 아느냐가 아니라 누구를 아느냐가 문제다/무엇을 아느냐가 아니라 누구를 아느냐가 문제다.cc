#include <bits/stdc++.h>
using namespace std;

int T, n, m;
int pre[21];
int d[21];
vector<pair<int, int>> board[21];
const int INF = 1e9 + 10;
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> n >> m;
		//비용first, 정점second

		for (int i = 0; i < 21; i++) {
			pre[i] = -1;
			d[i] = INF;
			board[i].clear();

		}
		while (n--) {
			int a, b, c;
			cin >> a >> b >> c;
			board[a].push_back({ c,b });
			board[b].push_back({ c,a });
		}

		//0에서 시작, m-1에서 끝
		int st = 0;
		priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;		d[st] = 0;//자기 자신과의 거리는 0
		pq.push({ 0,st });
		while (!pq.empty()) {
			pair<int, int> cur = pq.top();

			pq.pop();
			if (cur.first > d[cur.second]) continue;
			for (auto x : board[cur.second]) {//1이랑 연결된거 다봐야지
				if (d[x.second] > d[cur.second] + x.first) {
					//비용이 더 적어?그럼 갱신하자
					d[x.second] = d[cur.second] + x.first;
					//갱신했으면 큐에 넣어야지. 앞에는 비용, 뒤에는 정점
					pq.push({ d[x.second], x.second });
					pre[x.second] = cur.second;//4올때 1거쳐서왔지?
				}
			}
		}
		
		cout << "Case #" << tc << ": ";

		if (d[m - 1] == INF) {
			cout << -1 ;		
		}
		else {
			vector<int> tmp;
			tmp.clear();
			int t = m-1;
			while (t != st) {
				tmp.push_back(t);
				t = pre[t];
			}
			tmp.push_back(st);
			reverse(tmp.begin(), tmp.end());

			for (auto aa : tmp) {
				cout << aa << " ";
			}
		}
		cout << '\n';
	}
}