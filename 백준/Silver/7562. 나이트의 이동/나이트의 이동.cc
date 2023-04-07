#include<bits/stdc++.h>
using namespace std;

int dx[]={2,1,-1,-2,-2,-1,1,2};
int dy[]={1,2,2,1,-1,-2,-2,-1};
int vis[301][301];

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
 
  int t;
  cin>>t;
  while(t--){
    int l,sx,sy,ex,ey;
    cin>>l;
    cin>>sx>>sy>>ex>>ey;


    for(int i=0;i<l;i++){
      for(int j=0;j<l;j++){ 
        vis[i][j]=-1;
      }
    }
    queue<pair<int,int>> q;
    q.push({sx,sy});
    vis[sx][sy]=0;
    while(!q.empty()){
      auto cur=q.front();
      q.pop();
      for(int dir=0;dir<8;dir++){
        int nx=cur.first+dx[dir];
        int ny=cur.second+dy[dir];
        if(nx<0||ny<0||nx>=l||ny>=l) continue;
        if(vis[nx][ny]!=-1) continue;
        vis[nx][ny]=vis[cur.first][cur.second]+1;
        q.push({nx,ny});
      }
    }
    cout<<vis[ex][ey]<<"\n";
  }

}