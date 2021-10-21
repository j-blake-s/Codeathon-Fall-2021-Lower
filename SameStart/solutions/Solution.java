import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int xDim = sc.nextInt();
        int yDim = sc.nextInt();
        //eat the new line
        sc.nextLine();
        String[] board1 = new String[yDim];
        for (int i = 0; i < yDim; i++) {
            board1[i] = sc.nextLine();
        }
        sc.nextLine();
        String[] board2 = new String[yDim];
        for (int i = 0; i < yDim; i++) {
            board2[i] = sc.nextLine();
        }
        int answer = 0;
        for (int y = 0; y < yDim; y++) {
            for (int x = 0; x < xDim; x++) {
                if(board1[y].charAt(x) == board2[y].charAt(x) && 
                board1[y].charAt(x) == '.')
                {
                    answer += 1;
                }

            }
        }
        System.out.println(answer);
    }
}