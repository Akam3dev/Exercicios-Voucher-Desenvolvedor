import java.util.Scanner;

public class Ex3 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[] codigos = {1, 2, 3, 4, 5};
        int[] estoques = {22, 13, 20, 14, 10};

        int codigo_cliente = 0;
        int codigo_produto = 0;
        int quantidade = 0;

        boolean codigo_valido = false;

        do {
            System.out.print("Digite o código do cliente (0 para parar): ");
            codigo_cliente = sc.nextInt();

            if (codigo_cliente == 0) {
                break;
            }

            System.out.print("Digite o código do produto: ");
            codigo_produto = sc.nextInt();

            System.out.print("Digite a quantidade: ");
            quantidade = sc.nextInt();

            codigo_valido = false;

            for (int i = 0; i < codigos.length; i++) {

                if (codigo_produto == codigos[i]) {

                    codigo_valido = true;

                    if (quantidade <= estoques[i]) {

                        estoques[i] -= quantidade;

                        System.out.println(
                            "Pedido atendido. Obrigado e volte sempre!"
                        );

                    } else {

                        System.out.println(
                            "Não temos estoque suficiente desta mercadoria."
                        );

                    }

                    break;
                }
            }

            if (!codigo_valido) {
                System.out.println("Código inexistente.");
            }

        } while (codigo_cliente != 0);

        System.out.println("\n--- ESTOQUE ATUALIZADO ---");

        for (int i = 0; i < codigos.length; i++) {

            System.out.println(
                "Código: " + codigos[i] +
                " | Estoque: " + estoques[i]
            );

        }

    }
}
