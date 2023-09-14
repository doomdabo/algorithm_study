#include <iostream>
#include <queue>
#include <string>
using namespace std;
string board[3002];
int dist[3002][3002];
int dx[4] = {-1,0,1,0};
int dy[4] = {0,-1,0,1};
int n,m;
int main(void){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>m;
    queue <pair<int,int>> q;

    for(int i=0;i<n;i++){
        cin>>board[i];
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            dist[i][j]=-1; //거리 초기화
            if(board[i][j] == '2'){ //보드 값이 2이면 식구를의미
                q.push({i,j}); //여기서부터 bfs시작해야함
                dist[i][j] = 0; //거리 0으로 만들어줌
            }

        }
    }
    int ans =-1;
    int chk=0;
    while(!q.empty()){
        //큐가 비어있지 않으면 bfs시작
        pair<int,int> cur = q.front();
        q.pop();
        for(int dir =0;dir<4;dir++){
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];
            if(nx<0||ny<0||nx>=n||ny>=m) continue;
            if(board[nx][ny] == '1'||dist[nx][ny]!=-1) continue; 
            if(board[nx][ny] == '3'||board[nx][ny]=='4'||board[nx][ny]=='5'){
                 ans = dist[cur.first][cur.second] + 1;
                 chk = 1;
                 break; //더이상 진행할 필요 없음
             }
            q.push({nx,ny});
            dist[nx][ny] = dist[cur.first][cur.second] + 1;
        }
        if(chk == 1) break;
    }
    if(ans == -1){
        cout<<"NIE";
        return 0;
    }

    cout<<"TAK\n"<<ans;

}