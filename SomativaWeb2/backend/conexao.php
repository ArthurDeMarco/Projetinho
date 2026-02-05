<?php 
$servidor = "localhost";
$usuario = "root";
$senha = "";
$banco = "pkchaves";

$conn = mysqli_connect($servidor, $usuario, $senha, $banco);

if (!$conn) {
    die("Falha na conexao: " . mysqli_connect_error());
}

?>