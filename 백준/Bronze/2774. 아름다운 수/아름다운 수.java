// import static org.junit.jupiter.api.Assertions.assertEquals;

// import org.junit.jupiter.api.Test;

import java.io.*;
import java.util.*;
public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    int T = Integer.parseInt(br.readLine());
  
    //StringTokenizer st = new StringTokenizer(s);
    //int a = Integer.parseInt(st.ne1xtToken());
    //int b = Integer.parseInt(st.nextToken());
    for(int i=0;i<T;i++){
      String x = br.readLine(); // 일단 문자열로 입력받아서 자릿수 구하기
      int x_len = x.length();
      int[] arr = new int[11];

      for(int j=0;j<x_len;j++){
        arr[x.charAt(j)-'0']++;
      }
      int ans=0;
      for(int k=0;k<11;k++){
        if(arr[k]>0){
          ans++;
        }
      }
      System.out.println(ans);
    }
    
  }

  // @Test
  // void addition() {
  //     assertEquals(2, 1 + 1);
  // }
}