#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

int n, k, m;
vector<int> v;
int p;
int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> n >> k >> m;
	int k2 = k * 2;
	int p = -1;
	for (int i = 0; i < n; i++) {
		int l;
		cin >> l;
		if (l > k && l < k2) {
			//김밥 길이 2k보다 짧고 k보다 큰경우 한쪽만 꼬다리 짜름
			v.push_back(l-k);
		}
		if (k2 < l) {
			v.push_back(l-k2);
		}
	}
	int st = 1, end = 1000000000;
	while (st <= end) {
		int mid = (st + end) / 2;
		int cnt = 0;
		for (int gb : v) {
			cnt += gb / mid;
		}
		if (cnt >= m) { //김밥이 너무 많다. 작은 단위로 잘라서 그런거니까 더 크게 자름
			p = mid;
			st = mid + 1;
		}
		else {//김밥이 너무 적다 더 작게 자르자
			end = mid - 1;
		}
	}
	cout << p << '\n';
	return 0;


}