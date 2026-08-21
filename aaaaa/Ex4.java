import java.util.Scanner;

public class Ex4 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] vetor = {4,2,7,1,8,23,8,1,30,92,56,23,30,51,30};

        for (int i = 0; i < vetor.length; i++){

            if (vetor[i] == 30){
                System.out.println("Elemento igual a 30, na posição: " + i);
            }

        }
    }
}
