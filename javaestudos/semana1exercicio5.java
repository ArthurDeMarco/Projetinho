package javaestudos;

import java.util.Scanner;

public class semana1exercicio5 {
 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o ano e vou verificar se ele e bissexto ou nao: ");
        int ano = scanner.nextInt();

        if ((ano % 4 == 0 && ano % 100 != 0 ) || (ano % 400 == 0)) {
            System.out.println("O ano escolhido e bissexto");
        } else {
            System.out.print("O ano escolhido nao e bissexto");
        }

        scanner.close();
    }
}
