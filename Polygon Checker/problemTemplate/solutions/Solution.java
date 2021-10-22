import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        for(int t = 0; t < cases; t++){
            
            int n = sc.nextInt();
            sc.nextLine();
            ArrayList<String> points = new ArrayList();
            int total = 0;
            for(int i = 0; i < n; i++){
                String[] cur = sc.nextLine().split(" ");
                points.add(cur[0]);
                points.add(cur[1]);
                // points[i*2+1] = cur[1];
            }
            boolean works = true;
            for(int i = 0; i < points.size(); i++){
                if(Collections.frequency(points, points.get(i)) != 2)
                {
                    works = false;
                    break;
                }
            }
            if(works)
                System.out.println("True");
            else
                System.out.println("False");
        }

        
    }
}