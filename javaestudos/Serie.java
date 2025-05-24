import java.util.ArrayList;
import javaestudos.Episodio;

package javaestudos;

public class Serie {
    String nome;
    ArrayList<Episodio> episodios;

    Serie(String nomeinicial) {
        this.nome = nomeinicial;
        this.episodios = new ArrayList<>();
    }

    void adicionarEpisodio(Episodio episodio) {
        this.episodios.add(episodio);
    }

    void imprimirInfoSerie() {
        System.out.println("-------Dados de Cadastro-------");
        System.out.println("Titulo do Episodio: " + this.nome);
        System.out.println("Lista de Eps: ");
        for(Episodio episodio : this.episodios) {
            episodio.imprimirInfoEpisodio();
        }
    }

    
    public static void main(String[] args) {
        Serie serie1 = new Serie("Peaky Blindes", "50 minutos");
        Serie serie2 = new Serie("Bonda1", "50 minutos");
        Serie serie3 = new Serie("Bonda2", "50 minutos");
        Serie serie4 = new Serie("Bonda3", "50 minutos");
        Serie serie5 = new Serie("Bonda4", "50 minutos");
    
        serie1.mostrarDados();

    }
}