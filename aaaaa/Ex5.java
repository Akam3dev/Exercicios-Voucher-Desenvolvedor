import java.util.Scanner;

public class Ex5{

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int[] logica = {101, 105, 203, 182, 310, 701, 802};
        int[] linguagem = {101, 203, 310, 402, 801};

        for (int i = 0; i < logica.length; i++){

            for (int j = 0; j < linguagem.length; j++){
                if (logica[i] == linguagem[j]){
                    System.out.println("Aluno nas duas matérias: " + logica[i]);
                }
            }

        }


    }

}
