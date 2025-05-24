package javaestudos;

import java.util.Locale;
import java.util.Scanner; 


public class semana1exercicio1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.of("pt", "BR"));
        System.out.println("Digite o primeiro valor: ");
        float x = scanner.nextFloat();
        System.out.println("Digite o segundo valor: ");
        float y = scanner.nextFloat();
        System.out.println("Digite o valot do terceiro valor: ");
        float z = scanner.nextFloat();

        float media = (x + y + z)/3;

        System.out.println("Media e igual: " + media);

        scanner.close();

    }
}
