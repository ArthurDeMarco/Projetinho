package javaestudos;

public class Retangulo {

    float altura;

    float comprimento;

    Retangulo(float alturainicial, float comprimentoinicial){
        this.altura = alturainicial;
        this.comprimento  = comprimentoinicial;
    }

    float calcular_perimetro(){
        return (2 * altura) + (2 * comprimento);
    }

    float calcular_area(){
        return altura * comprimento;
    }
     
    public static void main(String[] args){
        System.out.println("vamo calcular retangulo bla bla bla");
    
        Retangulo ret1 = new Retangulo(5.2f, 12.5f);
        
        System.out.println(ret1.calcular_perimetro());

        Retangulo ret2 = new Retangulo(10.3f, 4.1f);
        System.out.println(ret2.calcular_perimetro());
    }
}

