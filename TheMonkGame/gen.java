package TheMonkGame;


import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
public class gen {

    final static String TOZAN = "T";
    final static String SEPPO = "S";
    final static String EMPTY = "~";
    final static String WIN = "#";

    final static int BOUND = 20;
    final static boolean DEBUG = false;
    static Random gen = new Random(0);
    static int numTests = 30;

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
    static int min(int a,int b) { if (a>b) return b; return a;}

    static String[][] addVert(int M, int N ,int K ,String[][] board) {
        
        int x = gen.nextInt(N);
        int y = gen.nextInt(M-K+1);
        
        String token;
        switch (gen.nextInt(2)) {
            case 0:
                token = TOZAN;
                break;
            case 1:
                token = SEPPO;
                break;
            default:
                token = EMPTY;
        }

        for (int k = 0; k < K;k++) board[y+k][x] = token;

        return board;
    }

    static String[][] addZont(int M, int N, int K,  String[][] board) {
        
        int x = gen.nextInt(N-K+1);
        int y = gen.nextInt(M);
        
        String token;
        switch (gen.nextInt(2)) {
            case 0:
                token = TOZAN;
                break;
            case 1:
                token = SEPPO;
                break;
            default:
                token = EMPTY;
        }

        for (int k = 0; k < K;k++) board[y][x+k] = token;

        return board;
    }

    static String[][] addRightDiag(int M, int N, int K,  String[][] board) {
        
        int x = gen.nextInt(N-K+1);
        int y = gen.nextInt(M-K+1);
        
        String token;
        switch (gen.nextInt(2)) {
            case 0:
                token = TOZAN;
                break;
            case 1:
                token = SEPPO;
                break;
            default:
                token = EMPTY;
        }

        for (int k = 0; k < K;k++) board[y+k][x+k] = token;

        return board;
    }

    static String[][] addLeftDiag(int M, int N, int K,  String[][] board) {
        
        int x = gen.nextInt(N-K+1)+K-1;
        int y = gen.nextInt(M-K+1);
        
        String token;
        switch (gen.nextInt(2)) {
            case 0:
                token = TOZAN;
                break;
            case 1:
                token = SEPPO;
                break;
            default:
                token = EMPTY;
        }

        for (int k = 0; k < K;k++) board[y+k][x-k] = token;

        return board;
    }

    static boolean check(String[] slice, String token) {
        for (String s : slice) {
            if (s.equals(token));
            else return false;
        }

        return true;
    }

    static String[][] makeHoles(int M,int N,int K, String[][] board) {
        



        //$ Vert Check
        for (int i = 0; i < M-K+1; i++) {
            for (int j = 0; j < N; j++) {
                String[] slice = new String[K];
                for (int k = 0; k < K; k++) slice[k] = board[i+k][j]; //& Build the slice
                if (check(slice,TOZAN) || check(slice,SEPPO)) {
                    int idx = gen.nextInt(K);
                    board[i+idx][j] = EMPTY;
                }
            }
        }

        //$ Zont Check
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N-K+1; j++) {
                String[] slice = new String[K];
                for (int k = 0; k < K; k++) slice[k] = board[i][j+k]; //& Build the slice
                if (check(slice,TOZAN) || check(slice,SEPPO)) {
                    int idx = gen.nextInt(K);
                    board[i][j+idx] = EMPTY;
                }
            }
        }

        //$ Right Diag Check
        for (int i = 0; i < M-K+1; i++) {
            for (int j = 0; j < N-K+1; j++) {
                String[] slice = new String[K];
                for (int k = 0; k < K; k++) slice[k] = board[i+k][j+k]; //& Build the slice
                if (check(slice,TOZAN) || check(slice,SEPPO)) {
                    int idx = gen.nextInt(K);
                    board[i+idx][j+idx] = EMPTY;
                }
            }
        }




        //$ Left Diag Check
        for (int i = 0; i < M-K+1; i++) {
            for (int j = N-1; j >= K-1; j--) {
                String[] slice = new String[K];
                for (int k = 0; k < K; k++) slice[k] = board[i+k][j-k]; //& Build the slice
                if (check(slice,TOZAN) || check(slice,SEPPO)) {
                    int idx = gen.nextInt(K);
                    board[i+idx][j-idx] = EMPTY;
                }
            }
        }


        return board;
    }

    static String[][] rand_board(int M,int N,int K) {
        String[][] board = new String[M][N];
        for (int i = 0; i < M; i++) for (int j = 0; j < N;j++) board[i][j] = EMPTY;

        int generations = 2*((M * N) /  K);

        
        for (int n = 0; n < generations;n++) {
            switch(gen.nextInt(4)) {
                case 0: 
                    board = addVert(M,N,K,board); 
                    break;
                case 1:
                    board = addZont(M,N,K,board);
                    break;
                case 2:
                    board = addLeftDiag(M,N,K,board);
                    break;
                case 3:
                    board = addRightDiag(M,N,K,board);
                    break;
            }
        }

        return makeHoles(M,N,K,board);
    }
    
    static void test_gen() {
        String fpi = "TheMonkGame/input/input";
        String fpo = "TheMonkGame/output/output";
        String fpbug = "TheMonkGame/debug/debug";
        for (int test = 0;test<numTests;test++) {
            String fin = fpi + test + ".txt";
            String fout = fpo + test + ".txt";
            String fbug = fpbug + test + ".txt";

            
            int M,N,K;

            M = N = (test+5);
            //N = gen.nextInt(BOUND-2)+3;
            K = gen.nextInt(min(M,N)/2);
            if (K<3) K = 3;

            String[][] board = rand_board(M,N,K);

            try {
                FileWriter fwin = new FileWriter(fin);
                fwin.write(M + " " + N + " " + K + "\n");
                for (int i = 0; i < M; i++) {
                    String buffer = "";
                    for (int j = 0; j < N;j++) {
                        fwin.write(buffer + board[i][j]);
                        buffer = " ";
                    }
                    fwin.write("\n");
                }
                fwin.close();
            } catch (IOException ioe) {}

            try {
                FileWriter fwout = new FileWriter(fout);
                fwout.write(""+sol.solve(M,N,K,board));
                fwout.close();
            } catch(IOException ioe) {} 

            if (DEBUG) {
                try {
                    FileWriter fwbug = new FileWriter(fbug);
                    board = sol.markBoard(M, N, K, board);
                    for (int i = 0; i < M; i++) {
                        String buffer = "";
                        for (int j = 0; j < N;j++) {
                            fwbug.write(buffer + board[i][j]);
                            buffer = " ";
                        }
                        fwbug.write("\n");
                    }
                    fwbug.close();
                } catch (IOException ioe) {} 
            }
        }
    }
    
    
    
    public static void main(String[] args) {
        test_gen();
    }
}