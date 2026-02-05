<?php
session_start();
require_once "conexao.php";

if (!isset($_SESSION["usuario_id"])) {
    session_destroy();
    header("Location: ../login.php");
    exit;
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $descricao = $_POST["descricao"];
    $preco = $_POST["preco"];
    $status = $_POST["status"];
    

    $usuario_id = $_SESSION["usuario_id"]; 

    $sql = "INSERT INTO servicos (descricao, valor, status, usuario_id) VALUES (?, ?, ?, ?)";
    $stmt = $conn->prepare($sql);
    
    $stmt->bind_param("sdsi", $descricao, $preco, $status, $usuario_id);

    if ($stmt->execute()) {
        echo "<script>alert('Serviço adicionado!'); window.location='servicos_listar.php';</script>";
    } else {
        echo "Erro ao adicionar: " . $conn->error;
    }
}
require_once "../includes/header.php"; 
?>


<div class="formulario"> <h1>Adicionar Serviço</h1>

    <form method="POST" action="servicos_adicionar.php"> 
        <label>Descrição:</label><br>
        <input type="text" name="descricao" required><br><br>

        <label>Preço:</label><br>
        <input type="number" step="0.01" name="preco" required><br><br>

        <label>Status:</label><br>
        <select name="status">
            <option value="pendente">Pendente</option>
            <option value="concluido">Concluído</option>
        </select><br><br>

        <input type="submit" class="submit_form" value="Salvar">
    </form>
</div>

<br>
<a href="servicos_listar.php">⬅ Voltar</a>
<?php
require_once "../includes/footer.php"; 
?>