package javaestudos;

import java.util.Scanner;

public class semana1exercicio6 {
 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o numero e vou verificar se ele e primo ou nao: ");
        int numero = scanner.nextInt();
        boolean ePrimo = true;

        if (numero <= 1) {
            ePrimo = false;
        } else {
            for (int  i = 2; i < numero; i++) {
                if (numero % i == 0) {
                    ePrimo = false;
                    break;
                }
            }
        }

        if (ePrimo) {
            System.out.println("O numero e primo! ");
        } else {
            System.out.println("O numero nao e primo! ");
        }

        scanner.close();
    }
}
