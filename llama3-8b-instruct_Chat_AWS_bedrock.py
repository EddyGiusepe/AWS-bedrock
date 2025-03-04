#! /usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

llama3-8b-instruct-v1:0
=======================
O Meta Llama 3 é um grande modelo de linguagem (LLM) acessível e aberto, projetado para
desenvolvedores, pesquisadores e empresas criarem, experimentarem e escalarem suas ideias
de IA generativa com responsabilidade. Parte de um sistema fundamental, ele serve como
base para a inovação na comunidade global. Ideal para recursos e recursos computacionais
limitados, dispositivos periféricos e tempos de treinamento mais rápidos.

| Detalhes          | Descrição                              |
|-------------------|----------------------------------------|
| Vendido por       | Meta                                   |
| Categorias        | Resumo de texto                        |
|                   | classificação de texto                 |
|                   | análise de sentimentos                 |
| Última versão     | v1                                     |
| Data lançamento   | Thu, 18 Apr 2024 08:00:00 GMT          |
| ID do Modelo      | meta.llama3-8b-instruct-v1:0           |
| Modalidade        | TEXT                                   |
| Máx. tokens       | 8k                                     |
| Idioma            | Inglês                                 |
| Tipo implantação  | Serverless                             |
"""
import boto3
import json

prompt_data = """
Atua como um Shakespeare e escreva um poema sobre IA Generativa.
Este poema deve ter apenas um parágrafo de 200 palavras.
Ademais, sempre responda em português do Brasil (pt-BR).
"""

bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

payload = {
    "prompt": "[INST]" + prompt_data + "[/INST]",
    "max_gen_len": 512,
    "temperature": 0.5,
    "top_p": 0.9,
}


body = json.dumps(payload)
model_id = "meta.llama3-8b-instruct-v1:0"

response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json",
)

response_body = json.loads(response.get("body").read())
repsonse_text = response_body["generation"]
print(repsonse_text)
