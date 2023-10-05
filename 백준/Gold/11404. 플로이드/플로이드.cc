#include <iostream>
#include <vector>
using namespace std;

int n, m;
int d[105][105];
const int INF = 0x3f3f3f3f;
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> n;
	cin >> m;
	for (int i = 1; i <= n; i++)
		fill(d[i], d[i] + 1 + n, INF);
	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		d[a][b] = min(c, d[a][b]); //시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
	} 

	for (int i = 1; i <= n; i++) {
		d[i][i] = 0; //자기자신 거리는 0
	}
	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (d[i][j] == INF) cout << "0 ";
			else {
				cout << d[i][j] << " ";
			}
		}
		cout << "\n";
	}
}
