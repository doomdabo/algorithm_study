#include<bits/stdc++.h>
using namespace std;

int n, m, st, en;
const int INF = 1e9 + 10;
vector<pair<int, int>> board[1005]; //{비용, 정점번호}
int d[1005]; //최단 거리 테이블
int pre[1005]; //경로 탐색 위함
int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n >> m;
	fill(d, d + n + 1, INF);
	while (m--) {
		int a, b, c;
		cin >> a >> b >> c;
		board[a].push_back({ c,b });//비용 first, 정점 second
	}
	
	cin >> st >> en;
	//우선순위 큐 만들기
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	d[st] = 0; //시작점 0에서 시작
	pq.push({ 0,st }); //시작은 {0,st}
	while (!pq.empty()) {
		auto cur = pq.top();
		pq.pop();
		if (cur.first != d[cur.second]) continue;
		for (auto x : board[cur.second]) {//1이랑 연결된거 다봐야지
				if(d[x.second]>d[cur.second]+x.first){
					//비용이 더 적어?그럼 갱신하자
					d[x.second] = d[cur.second] + x.first;
					//갱신했으면 큐에 넣어야지. 앞에는 비용, 뒤에는 정점
					pq.push({ d[x.second], x.second });
					pre[x.second] = cur.second;//4올때 1거쳐서왔지?
			}
		}
	}
	//자 이제 출력해보자. 최소비용은 도착도시 d의 값이겠지
	cout << d[en] << "\n";
	//이제 최소비용 갖는 경로에 포함된 도시의 개수 출력해야하고, 출, 도 다 포함.
	//벡터에 넣고 거꾸로 뺄거야
	vector<int> temp;
	//일단 끝 도시 먼저 넣자
	int t = en;
	while (t != st) { //시작점나올때까지 계쏙 넣어
		temp.push_back(t);
		t = pre[t];
	}
	temp.push_back(st); //시작점도 넣어주자
	reverse(temp.begin(),temp.end());
	cout << temp.size() << endl;
	for (auto a : temp) cout << a << " ";

}