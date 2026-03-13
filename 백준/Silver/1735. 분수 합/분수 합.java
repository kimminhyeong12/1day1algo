import java.util.*;
public class Main {
    public static int getGcd(int a, int b) {
        if (b == 0){
            return a;
        }
        return getGcd(b, a % b);
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] fraction = new int[4];
        for (int i = 0; i < 4; i++) {
            fraction[i] = scanner.nextInt();
        }
        int mother = fraction[1] * fraction[3];
        int son = fraction[0] * fraction[3] + fraction[1] * fraction[2];
        System.out.println((son/getGcd(son,mother))+" "+(mother/getGcd(son,mother)));


    }
}
