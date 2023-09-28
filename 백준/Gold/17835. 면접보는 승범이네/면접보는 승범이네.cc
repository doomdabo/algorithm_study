#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int n, m, k;
vector<pair<int, ll>> graph[100005];
const ll INF = 1e18;
priority_queue<pair<ll, ll>, vector<pair<ll, ll>>, greater<pair<ll, ll>>> pq;
ll d[100005];
int ks[100005];
int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> n >> m >> k;
	while (m--) {
		int u, v;
		ll c;
		cin >> u >> v >> c;
		graph[v].push_back({ c,u });
	}
	fill(d, d + n + 3, INF);
	while (k--) {
		int i;
		cin >> i;
		d[i] = 0;
		pq.push({ 0,i });
	}

	while (!pq.empty()) {
		auto cur = pq.top();
		pq.pop();
		if (d[cur.second] != cur.first) continue;
		for (auto nxt : graph[cur.second]) {
			if (d[nxt.second] > d[cur.second] + nxt.first) {
				d[nxt.second] = d[cur.second] + nxt.first;
				pq.push({ d[nxt.second],nxt.second });
			}
		}
	}
	int idx = -1;
	ll maxnum = -1;
	for (int i = 1; i <= n; i++) {
		if (maxnum < d[i]) {
			idx = i;
			maxnum = d[i];
		}
	}
	cout << idx << "\n" << maxnum;
	return 0;
}