package javaestudos;

public class Usuario {
    String nome_usuario;
    String email;
    String senha;

    Usuario(String nomeinicial, String emailinicial, String senhainicial){
        this.nome_usuario = nomeinicial;
        this.email = emailinicial;
        this.senha = senhainicial;
    }

    void mostrarDados(){
        System.out.println("-------Dados de Cadastro-------");
        System.out.println("Nome de usuario: " + this.nome_usuario);
        System.out.println("Email do Usuario; " + this.email);
    }

    boolean verificarSenha(String senhaFornecida){
        return this.senha.equals(senhaFornecida);
    }
 
    public static void main(String[] args) {
        Usuario usuario = new Usuario("Joao", "joao@exemplo.com", "senhaSegura123");
    

    usuario.mostrarDados();

    boolean senhaCorreta = usuario.verificarSenha("senhaSegura123");
    System.out.println("Senha fornecida esta correta? " + senhaCorreta);

    boolean senhaIncorreta = usuario.verificarSenha("senhaSegura123");
    System.out.println("Senha fornecida esta correta? " + senhaIncorreta);

    }
}




