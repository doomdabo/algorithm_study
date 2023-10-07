#include<bits/stdc++.h>
using namespace std;

int main(void) {
	int h, w, n, m;
	cin >> h >> w >> n >> m;
	/*
	한명씩 앉을 수 있는 테이블이 행마다 w개씩 h행에 걸쳐 있다.
	:행의 개수 h개 열의 개수 w개
	모든 참가자 세로로 n칸 or 가로로 m칸 이상 비우고 앉아야함
	다른 모든 참가자와 세로줄 번호의 차 n보다 크거나 
	가로줄 번호의 차 m보다 큰 곳에만 앉을 수 있음
	
	*/
	int a = ceil(h / (double)(n+1));
	int b = ceil(w / (double)(m + 1));

	cout << a * b;

}