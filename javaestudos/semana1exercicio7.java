package javaestudos;

import java.util.Scanner;

public class semana1exercicio7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Escreva a temperatura em C e vamos passar para F"); 
        double celcius = scanner.nextDouble();

        double f = celcius * 1.8 + 32;

        if (f < 32) {
            System.out.println("A temperatua e: " + f + "e esta baixa!");
        } else if (f >= 32 && f <= 80) {
            System.out.println("A temperatua e: " + f + "e esta moderada!");         
        } else {
            System.out.println("A temperatua e: " + f + "e esta alta");
        }
         scanner.close();

    }

}
