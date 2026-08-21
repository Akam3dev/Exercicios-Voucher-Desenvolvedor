import java.util.Scanner;

public class Ex2 {

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        int[] vetor = new int[7];

        for (int i = 0; i < vetor.length; i++){
            System.out.println("Digite o numero na posição: " + i);
            System.out.print(": ");
            vetor[i] = sc.nextInt();
        }

        System.out.println("Números multiplos de 2: ");

        for (int i = 0; i < vetor.length; i++){
            if (i % 2 == 0){
                System.out.print(i + " ");
            }
        }

        System.out.println("\nNúmeros multiplos de 3: ");

        for (int i = 0; i < vetor.length; i++){
            if (i % 3 == 0){
                System.out.print(i + " ");
            }
        }

        System.out.println("\nNúmeros multiplos de 2 e de 3: ");

        for (int i = 0; i < vetor.length; i++){
            if (i % 2 == 0 && i % 3 == 0){
                System.out.print(i + " ");
            }
        }

        System.out.println("");


    }

}
