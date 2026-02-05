<?php
session_start();

if (!isset($_SESSION["usuario_id"])) {
    header("Location: ../login.php"); 
    exit;
}
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Área do Usuário</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>

<header>
    <nav class="menu-principal">
      <h2>Pk Chaves</h2>
      <ul>
        <li><a href="../index.html">Início</a></li>
        <li><a href="home.php">Minha Área</a></li>
        <li><a href="logout.php">Sair</a></li>
      </ul>
    </nav>
</header>

<main style="padding:20px;">
    <a href="/SomativaWeb1/backend/servicos_listar.php" 
       style="display:inline-block; padding:10px 20px; background:#111c5f; color:white; 
              border-radius:6px; text-decoration:none; font-weight:bold;">
        Gerenciar Serviços
    </a>
</main>

</body>
</html>
