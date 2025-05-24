package javaestudos;

import java.util.Scanner;

public class semana1exercicio2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite um valor: ");
        int numero = scanner.nextInt();

        if (numero > 0) {
            System.out.println("O numero e positivo");
        } else if (numero < 0) {
            System.out.println("O numero e negativo");
        } else {
            System.out.println("O numero e zero");
        }
        scanner.close();
    }
}

