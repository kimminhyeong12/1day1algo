import java.io.BufferedReader;
import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bufferedReader.readLine());
        int[] count = new int[10001];
        for (int i = 0;i<n;i++){
            count[Integer.parseInt(bufferedReader.readLine())] +=1;
        }
        StringBuilder sb = new StringBuilder();
        for (int i=0;i<10001;i++){
            while (count[i]>0){
                sb.append(i).append("\n");
                count[i] -= 1;
            }
        }
        System.out.print(sb);





    }
}