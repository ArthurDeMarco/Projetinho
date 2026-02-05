<?php
session_start();
require_once "conexao.php";


if (!isset($_SESSION["usuario_id"]) || $_SERVER["REMOTE_ADDR"] !== $_SESSION["ip"] || $_SERVER["HTTP_USER_AGENT"] !== $_SESSION["user_agent"]) {
    session_destroy();
    header("Location: ../login.php");
    exit;
}

$usuario_id = $_SESSION["usuario_id"];


$sql = "SELECT * FROM servicos WHERE usuario_id = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("i", $usuario_id);
$stmt->execute();
$result = $stmt->get_result();


require_once "../includes/header.php"; 
?>

<h1>Meus Serviços</h1>

<a href="servicos_adicionar.php">Adicionar Novo Serviço</a><br><br>
<a href="home.php">⬅ Voltar</a><br><br>

<table border="1" cellpadding="10">
    <tr>
        <th>ID</th>
        <th>Descrição</th>
        <th>Preço</th>
        <th>Status</th>
        <th>Ações</th>
    </tr>

    <?php while ($row = $result->fetch_assoc()) { ?>
    <tr>
        <td><?= $row["id"] ?></td>
        
        <td><?= htmlspecialchars($row["descricao"]) ?></td>
        
        <td>R$ <?= number_format($row["valor"], 2, ',', '.') ?></td>
        
        <td><?= htmlspecialchars($row["status"]) ?></td>
        
        <td>
            <a href="servicos_editar.php?id=<?= $row["id"] ?>">✏ Editar</a> |
            <a href="servicos_excluir.php?id=<?= $row["id"] ?>" onclick="return confirm('Tem certeza que deseja excluir?');">🗑 Excluir</a>
        </td>
    </tr>
    <?php } ?>

</table>

<?php
require_once "../includes/footer.php"; 
?>