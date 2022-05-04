import java.util.ArrayList;
import java.util.Random;
public class MatrixMul {
    int dimension;
    int[][] result;
    int[][] a;
    int[][] b;
    Random rand= new Random();
    public MatrixMul(int dimension){
        this.dimension=dimension;
        populate();
    }
    public void populate(){
        a=new int[dimension][dimension];
        b=new int[dimension][dimension];
        result=new int[dimension][dimension];

        for (int x=0;x<dimension;x++){
            for (int y=0;y<dimension;y++){
                a[x][y]=rand.nextInt(1000);
                b[x][y]=rand.nextInt(1000);
            }
        }
    }
    public void see(){
        for (int[] arr:a) {
            System.out.println();
            for (int i:arr) {
                System.out.print(i+" ");
            }
        }
        System.out.println();
        for (int[] arr:b) {
            System.out.println();
            for (int i:arr) {
                System.out.print(i+" ");
            }
        }
    }

    public void multiply() {
        for (int z = 0; z < dimension; z++) {
            for (int x = 0; x < dimension; x++) {
                int res = 0;
                for (int y = 0; y < dimension; y++) {
                    res +=a[x][y] * b[y][z];
                }
                result[x][z]=res;
            }
        }
    }

    public void getResult() {
        System.out.println();
        for (int[] arr:result) {
            System.out.println();
            for (int i:arr) {
                System.out.print(i+" ");
            }
        }
    }
}
