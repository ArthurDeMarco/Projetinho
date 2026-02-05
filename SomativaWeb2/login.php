<?php
session_start();
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Login</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="formulario">
    <form method="POST" action="backend/login.php">

      <h2>Login</h2>

      <div class="perguntas_form">
        <label for="email_login">Email</label>
        <input type="email" id="email_login" name="email_login" required>
      </div>

      <div class="perguntas_form">
        <label for="senha_login">Senha</label>
        <input type="password" id="senha_login" name="senha_login" required>
      </div>

      <input type="submit" class="submit_form" value="Entrar">

    </form>
  </div>

</body>
</html>
