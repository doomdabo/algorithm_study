#include<bits/stdc++.h>
using namespace std;

int dx[8] = { -1, -1, 0, 1, 1, 1, 0, -1 };
int dy[8] = { 0, 1, 1, 1, 0, -1, -1, -1 };
int n, m, k;
struct fireball {
	int r;
	int c;
	int m;//질량
	int s;//속력
	int d;//방향
};
vector<fireball> board[55][55];
vector<fireball> fb;
void move() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			board[i][j].clear();
		}
	}
	for (int i = 0; i < fb.size(); i++) {
		fireball cur = fb[i];
		int x = cur.r;
		int y = cur.c;
		int nx = x + dx[cur.d] * cur.s;
		int ny = y + dy[cur.d] * cur.s;
		while (nx < 0) nx +=n; // 주의!! if문 만으로는 안된다
		while (ny < 0) ny += n;
		while (nx > n-1) nx -= n;
		while (ny > n-1) ny -= n;
		board[nx][ny].push_back({ nx,ny,cur.m,cur.s,cur.d });

	}

}
void split() {
	vector<fireball> temp;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (board[i][j].size() == 0) continue;
			if (board[i][j].size() == 1) temp.push_back(board[i][j][0]);
			if (board[i][j].size() > 1) {
				//같은칸에 2개 이상의 파이어볼 있다?
				//모두 하나로 합친다
				int new_m = 0, new_s = 0;//질량,속력
				int odd = 0, even = 0, check = 0;
				int dir1[4] = { 0,2,4,6 };
				int dir2[4] = { 1,3,5,7 };
				for (int ball = 0; ball < board[i][j].size(); ball++) {
					new_m += board[i][j][ball].m;
					new_s += board[i][j][ball].s;
					//모든 파이어 볼의 방향 체크
					if (board[i][j][ball].d % 2 == 0) even++;
					else odd++;

				}
				if (even == board[i][j].size() || odd == board[i][j].size()) {
					check = 1;
				}
				new_m = new_m / 5;
				new_s = new_s / board[i][j].size();
				if (new_m != 0) {
					for (int idx = 0; idx < 4; idx++) {
						if (check == 1)
							temp.push_back({ i,j,new_m,new_s,dir1[idx] });
						else
							temp.push_back({ i,j,new_m,new_s,dir2[idx] });

					}
				}
			}
		}
	}
	fb = temp; //완전히 fireball을 업데이트해줌
}
int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	//입력받기
	cin >> n >> m >> k;
	while (m--) {
		int r, c, m, s, d;;
		cin >> r >> c >> m >> s >> d;
		fb.push_back({ r - 1,c - 1,m,s,d });
	}
	//이동, 합치고 나누기
	while (k--) {
		move();
		split();
	}
	//남아있는 파이어볼 질량의 합?
	int ans = 0;
	for (int i = 0; i < fb.size(); i++) {
		ans += fb[i].m;
	}
	cout << ans;
}