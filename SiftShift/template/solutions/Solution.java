import java.io.*;
import java.util.*;

public class Solution {

    public static int getTotal(int[] arr, int leftPos, int rightPos){
        int sum = 0;
        for(int i = leftPos; i < rightPos; i++){
            sum += arr[i];
        }
        return sum;
    }
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        int total = 0;
        for(int i = 0; i < n; i++){
            nums[i] = sc.nextInt();
            total += nums[i];
        }
        int answer = total;
        int leftPos = 0;
        int rightPos = n - 1;
        while (leftPos <= rightPos) {
            answer += getTotal(nums, leftPos, rightPos);
            leftPos += 1;
            answer += getTotal(nums, leftPos, rightPos);
            rightPos -= 1;
            answer %= 1000;
        }
        System.out.println(answer);
        
        
    }
}