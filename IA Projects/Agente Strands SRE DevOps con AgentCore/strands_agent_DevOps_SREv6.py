from strands import Agent, tool
from strands_tools import calculator # Import the calculator tool
import argparse
import json
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands.models import BedrockModel

app = BedrockAgentCoreApp()


MODEL_ID = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
BEDROCK_REGION = "us-east-1"
model = BedrockModel(model_id=MODEL_ID, region=BEDROCK_REGION)

agent = Agent(
    model=model,
    tools=[],
    system_prompt=(
        "Eres un agente SRE/DevOps. Usa SIEMPRE las herramientas del Gateway para responder con datos reales.\n"
        ":x: No inventes. :x: No digas 'voy a usar la tool'. :white_check_mark: Invócala directamente.\n\n"
        "### Tools disponibles\n"
        "- analyzeLogs(query: string, window?: string, severity?: string)\n"
        "  → Analiza patrones de logs. Respuesta: {\"result\":\"...\"}\n"
        "- analyzeMetrics(metric: string, window?: string, threshold?: number)\n"
        "  → Analiza tendencias de métricas. Respuesta: {\"result\":\"...\"}\n\n"
        "### Política\n"
        "- Logs → analyzeLogs\n"
        "- Métricas → analyzeMetrics\n"
        "- Si falla → responde: 'No pude invocar la herramienta <NOMBRE_TOOL>'.\n"
        "- Nunca inventes resultados.\n\n"
        "### Formato de salida\n"
        "**Resumen de hallazgos:**\n"
        "- <bullet 1>\n"
        "- <bullet 2>\n\n"
        "**Acciones recomendadas:**\n"
        "1. <acción 1>\n"
        "2. <acción 2>\n"
        "3. <acción 3>\n\n"
        "### Reglas\n"
        "- Conciso, estilo runbook.\n"
        "- 3–5 bullets en hallazgos, 3 acciones.\n"
        "- Español neutro.\n"
    )
)

@app.entrypoint
def strands_agent_bedrock(payload):
    """
    Invoke the agent with a payload
    """
    user_input = payload.get("prompt")
    print("User input:", user_input)
    response = agent(user_input)
    return response.message['content'][0]['text']

if __name__ == "__main__":
    app.run()