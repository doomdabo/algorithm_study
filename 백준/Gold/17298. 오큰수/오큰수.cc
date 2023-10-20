#include<bits/stdc++.h>
using namespace std;
int n;
int arr[1000001];
int ans[1000001];
stack<int> s;
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	for (int i = n - 1; i >= 0; i--) {
		while (!s.empty() && s.top() <= arr[i]) {
			//stack에 뭐가 있는데 원하는게 아니면 계속 pop
			s.pop();
		}
		if (s.empty()) {
			//원하는게 결국 없었어?
			ans[i] = -1; //답은 -1
		}
		else {
			//원하는게 나왔어?
			ans[i] = s.top();
		}
		s.push(arr[i]);
	}
	for (int i = 0; i < n; i++) {
		cout << ans[i] << " ";
	}
}