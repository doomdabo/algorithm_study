#include<bits/stdc++.h>
using namespace std;

int n, k;
string num;
deque <char> dq;


int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> n >> k;
	int kk = k;
	cin >> num;
	int l = num.length();
	for (int i = 0; i < n; i++) {
		while (k >0 && !dq.empty() && dq.back() < num[i]) {
			dq.pop_back();
			k--;
		}
		dq.push_back(num[i]);
	
	}
	for (int i = 0; i < dq.size()-k; i++) {
		cout << dq[i];
	}
}