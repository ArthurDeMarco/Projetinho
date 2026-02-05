<?php 
require_once "conexao.php";

if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $nome = $_POST['nome_usuario'];
    $email = $_POST['gmail_usuario'];
    $telefone = $_POST['telefone_usuario'];
    $senha = $_POST['senha_usuario'];
    $confirmar = $_POST['confirmar_senha']; 

    // Verificação das senhas
    if ($senha !== $confirmar) {
        echo "<script>alert('As senhas não coincidem!'); window.history.back();</script>";
        exit();
    }

    // Criptografar senha
    $senhaHash = password_hash($senha, PASSWORD_DEFAULT);

    $sql = "INSERT INTO usuarios (nome, email, telefone, senha) VALUES (?, ?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ssss", $nome, $email, $telefone, $senhaHash);

    if ($stmt->execute()) {
        echo "<script>alert('Cadastro realizado com sucesso!'); window.location.href='../login.php';</script>";
    } else {
        echo "Erro ao cadastrar: " . $conn->error;
    }

    $stmt->close();
    $conn->close();
}
?>
