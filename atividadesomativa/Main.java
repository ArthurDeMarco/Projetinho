package atividadesomativa;

import java.util.Scanner;

class Financiamento {

    // Atributos
    double valorImovel;
    int prazoFinanciamento;
    double taxaJurosAnual;

    // Construtor 
    public Financiamento(double valorDesejadoImovel, int prazoFinanciamentoAnos, double taxaJurosAnual) {
        this.valorImovel = valorDesejadoImovel;
        this.prazoFinanciamento = prazoFinanciamentoAnos;
        this.taxaJurosAnual = taxaJurosAnual;
    }

    // Metodos
    double calcularPagamentoMensal() {
        return (this.valorImovel / (this.prazoFinanciamento * 12)) * (1 + (this.taxaJurosAnual / 12));
    }

    double calcularTotalPagamento() {
        return calcularPagamentoMensal() * this.prazoFinanciamento * 12;
    }

}

class InterfaceUsuario {
    Scanner scanner = new Scanner(System.in); 
    // Metodos
    double pedirValorImovel() {
        System.out.println("Digite o valor do imovel: ");
        double valorImovel = scanner.nextDouble();
        return valorImovel;
    }

    int pedirPrazoFinanciamento() {
        System.out.println("Digite o prazo do financiamento: ");
        int prazoFinanciamento = scanner.nextInt();
        return prazoFinanciamento;
    }

    double pedirTaxaJuros() {
        System.out.println("Digite a taxo do financiamento(Por ano): ");
        double taxaJuros = scanner.nextDouble();
        return taxaJuros;
    }
}

public class Main {
    public static void main(String[] args) {
        
        InterfaceUsuario interfaceUsuario = new InterfaceUsuario(); 

        double taxaJuros = interfaceUsuario.pedirTaxaJuros();
        int prazoFinanciamento = interfaceUsuario.pedirPrazoFinanciamento();
        double valorImovel = interfaceUsuario.pedirValorImovel();

        Financiamento novoFinanciamento = new Financiamento(valorImovel, prazoFinanciamento, taxaJuros);

        System.out.printf("Pagamento mensal: %.2f\n", novoFinanciamento.calcularPagamentoMensal());
        System.out.printf("Total do pagamento: %.2f\n", novoFinanciamento.calcularTotalPagamento());

    }
}
