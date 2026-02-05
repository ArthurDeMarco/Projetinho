<?php
session_start();
require_once "conexao.php";

if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $email = $_POST["email_login"];
    $senha = $_POST["senha_login"];

    $sql = $conn->prepare("SELECT * FROM usuarios WHERE email = ?");
    $sql->bind_param("s", $email);
    $sql->execute();
    $resultado = $sql->get_result();

    if ($resultado->num_rows === 1) {
        $usuario = $resultado->fetch_assoc(); 

        if (password_verify($senha, $usuario["senha"])) {

            $_SESSION["usuario_id"] = $usuario["id"]; 
            $_SESSION["ip"] = $_SERVER["REMOTE_ADDR"]; 
            $_SESSION["user_agent"] = $_SERVER["HTTP_USER_AGENT"]; 

            header("Location: /SomativaWeb1/backend/home.php");
            exit;
        }
    }

    echo "<script>alert('Email ou senha incorretos!'); window.location='../login.php';</script>";
}
?>