import java.util.Scanner;

public class Ex1{
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        int qnt_pares = 0;
        int qnt_impares = 0;

        int[] vetor = new int[6];

        for (int i = 0; i < vetor.length; i++){
            System.out.println("Digite o valor da posição: " + i);
            System.out.print(": ");

            vetor[i] = sc.nextInt();

        }

        for (int i = 0; i < vetor.length; i++){

            if (i % 2 == 0){
                qnt_pares += 1;
            }

            else{
                qnt_impares += 1;
            }

        }

        System.out.println("Quantidade de numeros pares: " + qnt_pares);

        System.out.println("Numeros pares: ");

        for (int i = 0; i < vetor.length; i++){

            if (i % 2 == 0 ){
                System.out.print(i + " ");
            }

        }

        System.out.println("Quantidade de numeros impares: " + qnt_impares);

        System.out.println("Numeros impares: ");

        for (int i = 0; i < vetor.length; i++){
            if (i % 2 != 0){
                System.out.print(i + " ");
            }
        }

        System.out.print("\n");

    }
}