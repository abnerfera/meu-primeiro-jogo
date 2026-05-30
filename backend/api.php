<?php
// Isso permite que o Python acesse sua API sem bloqueios de segurança (CORS)
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");

// Um array simples que vamos transformar em JSON
$resposta = [
    "status" => "sucesso",
    "mensagem" => "ÉEEEE CARAI PEGOU PORRAAAAAAA."
];

echo json_encode($resposta);
?>