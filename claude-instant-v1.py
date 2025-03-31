#! /usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

anthropic.claude-instant-v1
===========================
Um modelo rápido e econômico, mas ainda assim muito capaz,
que pode lidar com uma variedade de tarefas, incluindo diálogo
casual, análise de texto, sumarização e resposta a perguntas de documentos.

------------------------------------------------------
| Detalhes          | Descrição                      |
|-------------------|--------------------------------|
| Vendido por       | Anthropic                      |
| Categorias        | Geração de texto, Conversa     |
| Última versão     | v1.2                           |
| ID do Modelo      | anthropic.claude-instant-v1    |
| Modalidade        | TEXT                           |
| Máximo de tokens  | 100k                           |
| Idiomas           | Inglês e vários outros idiomas |
| Tipo de deploy    | Serverless                     |
------------------------------------------------------
"""
import boto3
import json

prompt_data = """
Atua como um Shakespeare e escreva um poema sobre IA Generativa.
Este poema deve ter apenas um parágrafo de 200 palavras.
Ademais, sempre responda em português do Brasil (pt-BR).
"""

bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")


"""
O seguinte JSON é um exemplo de payload para o modelo anthropic.claude-instant-v1.
Siga esse JSON, assim:

{
  "modelId": "anthropic.claude-instant-v1",
  "contentType": "application/json",
  "accept": "*/*",
  "body": "{\"prompt\":\"\\n\\nHuman: Hello world\\n\\nAssistant:\",\"max_tokens_to_sample\":300,\"temperature\":0.5,\"top_k\":250,\"top_p\":1,\"stop_sequences\":[\"\\n\\nHuman:\"],\"anthropic_version\":\"bedrock-2023-05-31\"}"
}
"""

payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens_to_sample": 512,
    "temperature": 0.8,
    "prompt": f"\n\nHuman: {prompt_data}\n\nAssistant:",
}

body = json.dumps(payload)
model_id = "anthropic.claude-instant-v1"
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json",
)

response_body = json.loads(response.get("body").read())
response_text = response_body.get("completion")
print(response_text)
