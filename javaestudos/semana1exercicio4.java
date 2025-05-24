package javaestudos;

import java.util.Scanner;

public class semana1exercicio4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o numero que quer fazer a tabuada: ");
        int numero = scanner.nextInt();
        
        for (int i = 1; i <= 10; i++) {
            System.out.println(numero + " x " + i + " = " + (numero * i));

            scanner.close();
        }
    }
}

