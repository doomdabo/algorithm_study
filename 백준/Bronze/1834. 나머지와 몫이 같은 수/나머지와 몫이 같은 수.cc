#include<bits/stdc++.h>
using namespace std;

int main(void) {
	long long sum = 0;
	long long n;
	cin >> n;
	for (int i = 1; i < n; i++) {
		sum += n * i + i;
	}
	cout << sum;
}