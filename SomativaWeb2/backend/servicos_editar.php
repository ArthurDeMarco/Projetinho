<?php
session_start();
require_once "conexao.php";

if (!isset($_SESSION["usuario_id"])) {
    session_destroy();
    header("Location: ../login.php");
    exit;
}

if (!isset($_GET["id"])) {
    die("ID do serviço não informado!");
}

$id = $_GET["id"];

// Buscar dados atuais
$sql = "SELECT * FROM servicos WHERE id = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("i", $id);
$stmt->execute();
$servico = $stmt->get_result()->fetch_assoc();

if (!$servico) {
    die("Serviço não encontrado!");
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $descricao = $_POST["descricao"];
    $preco = $_POST["preco"];
    $status = $_POST["status"];

    // Usando a correção de Autorização + Colunas Corretas
    $usuario_id = $_SESSION["usuario_id"];
    $sql = "UPDATE servicos SET descricao = ?, valor = ?, status = ? WHERE id = ? AND usuario_id = ?"; 
    $stmt = $conn->prepare($sql);

    // Tipos: descricao(s), preco/valor(d), status(s), id(i), usuario_id(i)
    $stmt->bind_param("sdsii", $descricao, $preco, $status, $id, $usuario_id);

    if ($stmt->execute()) {
        echo "<script>alert('Serviço atualizado!'); window.location='servicos_listar.php';</script>";
    } else {
        echo "Erro ao atualizar: " . $conn->error;
    }
}

require_once "../includes/header.php"; 
?>

<h1>Editar Serviço</h1>

<div class="formulario"> <h1>Editar Serviço #<?= htmlspecialchars($id) ?></h1>

    <a href="servicos_listar.php">⬅ Voltar para Meus Serviços</a><br><br>

    <form method="POST" action="servicos_editar.php?id=<?= htmlspecialchars($id) ?>"> 

        <label>Descrição:</label><br>
        <input type="text" name="descricao" value="<?= htmlspecialchars($servico["descricao"]) ?>" required><br><br>

        <label>Preço:</label><br>
        <input type="number" step="0.01" name="preco" value="<?= htmlspecialchars($servico["valor"]) ?>" required><br><br>

        <label>Status:</label><br>
        <select name="status">
            <option value="pendente" <?= ($servico["status"] == "pendente") ? "selected" : "" ?>>Pendente</option>
            <option value="concluido" <?= ($servico["status"] == "concluido") ? "selected" : "" ?>>Concluído</option>
        </select><br><br>

        <input type="submit" class="submit_form" value="Salvar Alterações">
    </form>
</div>
<?php
require_once "../includes/footer.php"; 
?>