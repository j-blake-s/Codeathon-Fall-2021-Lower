package TheMonkGame;
import java.util.Scanner;
public class sol {

    final static String TOZAN = "T";
    final static String SEPPO = "S";
    final static String EMPTY = "~";
    final static String WIN = "#";

    static boolean check(String[] slice, int goal, String token) {
        int sum = 0;

        for (String s : slice) {
            if (s.equals(token)) sum++;
            else if (s.equals(EMPTY));
            else return false;
        }

        if (sum == goal-1) return true;
        else return false;
    }

    static String[][] markBoard(int M,int N,int K, String[][] board) {

        //$ Vert Check
        for (int i = 0; i < M-K+1; i++) {
            for (int j = 0; j < N; j++) {
                String[] slice = new String[K];
                int x = -1;
                int y = -1;
                for (int k = 0; k < K; k++) {
                    slice[k] = board[i+k][j]; //& Build the slice
                    if (slice[k].equals(EMPTY)) {
                        x = j;
                        y = i+k;
                    }
                }
                
                if (check(slice,K,TOZAN) || check(slice,K,SEPPO)) board[y][x] = WIN;
            }
        }

        //$ Zont Check
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N-K+1; j++) {
                String[] slice = new String[K];
                int x = -1;
                int y = -1;
                for (int k = 0; k < K; k++) {
                    slice[k] = board[i][j+k]; //& Build the slice
                    if (slice[k].equals(EMPTY)) {
                        x = j+k;
                        y = i;
                    }
                }
                
                if (check(slice,K,TOZAN) || check(slice,K,SEPPO)) board[y][x] = WIN;
            }
        }

        //$ Right Diag Check
        for (int i = 0; i < M-K+1; i++) {
            for (int j = 0; j < N-K+1; j++) {
                String[] slice = new String[K];
                int x = -1;
                int y = -1;
                for (int k = 0; k < K; k++) {
                    slice[k] = board[i+k][j+k]; //& Build the slice
                    if (slice[k].equals(EMPTY)) {
                        x = j+k;
                        y = i+k;
                    }
                }
                
                if (check(slice,K,TOZAN) || check(slice,K,SEPPO)) board[y][x] = WIN;
            }
        }




        //$ Left Diag Check
        for (int i = 0; i < M-K+1; i++) {
            for (int j = N-1; j >= K-1; j--) {
                String[] slice = new String[K];
                int x = -1;
                int y = -1;
                for (int k = 0; k < K; k++) {
                    slice[k] = board[i+k][j-k]; //& Build the slice
                    if (slice[k].equals(EMPTY)) {
                        x = j-k;
                        y = i+k;
                    }
                }
                
                if (check(slice,K,TOZAN) || check(slice,K,SEPPO)) board[y][x] = WIN;
            }
        }

        
        return board;
    }

    static int solve(int M,int N,int K, String[][] board) {



        int sum = 0;



        //$ Vert Check
        for (int i = 0; i < M-K+1; i++) {
            for (int j = 0; j < N; j++) {
                String[] slice = new String[K];
                int x = -1;
                int y = -1;
                for (int k = 0; k < K; k++) {
                    slice[k] = board[i+k][j]; //& Build the slice
                    if (slice[k].equals(EMPTY)) {
                        x = j;
                        y = i+k;
                    }
                }
                
                if (check(slice,K,TOZAN) || check(slice,K,SEPPO)) {board[y][x] = WIN; sum += 1;}
            }
        }

        //$ Zont Check
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N-K+1; j++) {
                String[] slice = new String[K];
                int x = -1;
                int y = -1;
                for (int k = 0; k < K; k++) {
                    slice[k] = board[i][j+k]; //& Build the slice
                    if (slice[k].equals(EMPTY)) {
                        x = j+k;
                        y = i;
                    }
                }
                
                if (check(slice,K,TOZAN) || check(slice,K,SEPPO)) {board[y][x] = WIN; sum += 1;}
            }
        }

        //$ Right Diag Check
        for (int i = 0; i < M-K+1; i++) {
            for (int j = 0; j < N-K+1; j++) {
                String[] slice = new String[K];
                int x = -1;
                int y = -1;
                for (int k = 0; k < K; k++) {
                    slice[k] = board[i+k][j+k]; //& Build the slice
                    if (slice[k].equals(EMPTY)) {
                        x = j+k;
                        y = i+k;
                    }
                }
                
                if (check(slice,K,TOZAN) || check(slice,K,SEPPO)) {board[y][x] = WIN; sum += 1;}
            }
        }




        //$ Left Diag Check
        for (int i = 0; i < M-K+1; i++) {
            for (int j = N-1; j >= K-1; j--) {
                String[] slice = new String[K];
                int x = -1;
                int y = -1;
                for (int k = 0; k < K; k++) {
                    slice[k] = board[i+k][j-k]; //& Build the slice
                    if (slice[k].equals(EMPTY)) {
                        x = j-k;
                        y = i+k;
                    }
                }
                
                if (check(slice,K,TOZAN) || check(slice,K,SEPPO)) {board[y][x] = WIN; sum += 1;}
            }
        }

        
        return sum;
    }

    static void printBoard(String[][] board) {
        for (String[] row : board) {
            String buffer = "";
            for (String e : row) {
                System.out.print(buffer+e);
                buffer = " ";
            }
            System.out.println();
        }
    }
    public static void main(String [] args) {
        Scanner scanner = new Scanner(System.in);

        int M,N,K;
        M = scanner.nextInt();
        N = scanner.nextInt();
        K = scanner.nextInt();
        scanner.nextLine();

        String[][] board = new String[M][N];
        for (int i = 0; i < M; i++) {
            String[] line = scanner.nextLine().split(" ");
            for (int j = 0; j < N; j++) {
                board[i][j] = line[j];
            }
        }

        System.out.println(solve(M,N,K,board));
        scanner.close();

    }
}