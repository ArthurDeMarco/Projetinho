<?php
session_start();
require_once "conexao.php";

if (!isset($_SESSION["usuario_id"])) {
    session_destroy();
    header("Location: ../login.php");
    exit;
}

if (!isset($_GET["id"])) {
    die("ID não informado!");
}

$id = $_GET["id"];

$sql = "DELETE FROM servicos WHERE id = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("i", $id);

if ($stmt->execute()) {
    echo "<script>alert('Serviço excluído!'); window.location='servicos_listar.php';</script>";
} else {
    echo "Erro ao excluir: " . $conn->error;
}

?>

