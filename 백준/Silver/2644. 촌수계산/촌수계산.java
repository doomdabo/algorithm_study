import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
    public static boolean[] vis;
    public static int res =-1;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine()); //전체 사람수
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken()); //촌수 계산할사람 1
        int b = Integer.parseInt(st.nextToken()); //촌수 계산할사람 2
        int m = Integer.parseInt(br.readLine()); //부모 자식들 간의 관계의 개수
        for(int i=0;i<=n;i++){
            arr.add(new ArrayList<>());
        }
        for(int i = 0;i < m;i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arr.get(x).add(y);
            arr.get(y).add(x);
        }
        vis = new boolean[n+1];
        DFS(a,b,0);
        System.out.println(res);
    }
    public static void DFS(int st,int ed, int cnt){
        if(st == ed){
            res = cnt;
            return;
        }
        vis[st]=true;
        for(int i=0;i<arr.get(st).size();i++){
            int nxt = arr.get(st).get(i);
            if(!vis[nxt]){
                DFS(nxt,ed,cnt+1);
            }
        }
    }
}
