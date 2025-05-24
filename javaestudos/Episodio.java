package javaestudos;

public class Episodio {
    String titulo;
    String duracao;

    Episodio(String tituloinicial, String duracaoinicial){
        this.titulo = tituloinicial;
        this.duracao = duracaoinicial;
    }

    void mostrarDados(){
        System.out.println("-------Dados de Cadastro-------");
        System.out.println("Titulo do Episodio: " + this.titulo);
        System.out.println("Duracao do Episodio: " + this.duracao);
    }

    
    public static void main(String[] args) {
        Episodio episodio1 = new Episodio("Peaky Blindes", "50 minutos");
        Episodio episodio2 = new Episodio("Bonda1", "50 minutos");
        Episodio episodio3 = new Episodio("Bonda2", "50 minutos");
        Episodio episodio4 = new Episodio("Bonda3", "50 minutos");
        Episodio episodio5 = new Episodio("Bonda4", "50 minutos");
    
        episodio1.mostrarDados();

    }
}