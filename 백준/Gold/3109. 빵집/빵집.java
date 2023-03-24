import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static char[][] board;
	static int n, m,cnt,check;
	static int[] dx = { -1, 0, 1 };
	//최대 수가 보장되는 이유: 연결할 수 있는 가장~ 위로 붙여서 파이프를 설치하다보면 
	//아래에서 파이프를 연결할 수 있는 공간이 더 많이 생기기 때문이다.
	//결국 이는 놓을 수 있는 파이프라인의 최대 개수가 된다.
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		board = new char[n][m];
		for (int i = 0; i < n; i++) {
			String s = br.readLine();
			for (int j = 0; j < m; j++) {
				board[i][j] = s.charAt(j);
			}
		}

		for(int i =0;i<n;i++) {
			check =0;// 한번 dfs 진행 후 초기화를 해줘야함
			dfs(i,0); //(0,0),(1,0), ... (n,0)에서 bfs 시작
		}
		System.out.println(cnt);
	}
	//BFS를 못사용 하는 이유는 처음 지점부터 끝 지점까지 연결한 파이프는 한 줄이다.
	//따라서 오위, 오, 오아 세 지점 탐색해야하는데 오른쪽 위 지점 연결해서 쭉 이어가다 파이프 연결했으면
	//오른쪽, 오른쪽 아래 지점을 탐색할 수 없으므로! 모든 파이프 지점에서 추가 탐색을 그만두게 해야한다.
	//https://maivve.tistory.com/240
    private static void dfs(int st, int e) {
        if(e==m-1) {
        	cnt++;
        	check=1;
        	return;
        }
        for (int i = 0; i < 3; i++) { //오른쪽위, 오른쪽, 오른쪽 아래 순서로 탐색
            int nx = st + dx[i];
            int ny = e + 1;
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if(board[nx][ny]=='x') continue;
            board[nx][ny]='x';
            dfs(nx,ny);
            if(check==1) return;

        }

    }

}
