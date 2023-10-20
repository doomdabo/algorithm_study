#include <bits/stdc++.h>
using namespace std;
int n;
vector<pair<int, int>> v;
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> n;
	int m = n;
	while (m--) {
		int d, t;
		cin >> d >> t;
		v.push_back({ t,d });
	}
	sort(v.begin(), v.end());
	reverse(v.begin(), v.end());
	
	int time = v[0].first;
	for (int i = 0; i < n; i++) {
		int end = v[i].first;//13,10,8
		int st = v[i].second;//1,3,2

		if (time >= end) {
			//마감일이 시작일보다 이른 경우 13,13
			time = end - st;//12로 갱신. 다음은 10이랑 비교
		}
		else {
			time = time - st;//time이 7인데 end가 8이면
			//time에 7-2 저장
		}
	}
	cout << time;
}