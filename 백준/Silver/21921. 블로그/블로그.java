import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        String[] arr = br.readLine().split(" ");
        //n일동안 블로그를 썼고, x일동안 가장 많이 들어온 방문자수, 기간 구하기
        int max_sum = 0; //x개의 합 저장할 변수
        int cnt = 1;
        for(int i=0;i<x;i++){//맨처음 x개의 합 저장
            max_sum+=Integer.parseInt(arr[i]);

        }
        int temp = max_sum;
        for(int i=x;i<n;i++){
            temp = temp + Integer.parseInt(arr[i]) - Integer.parseInt(arr[i-x]);
            if(temp==max_sum){
                cnt++;
            }
            else if(temp>max_sum){
                max_sum = temp;
                cnt = 1;
            }
        }
        if(max_sum==0){
            bw.write("SAD");
        }
        else{
            bw.write(max_sum+"\n"+cnt);
        }
        bw.flush();


    }

}
