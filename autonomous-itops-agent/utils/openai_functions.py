from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def restart_service(service_name: str):
    print(f"[ACTION] Restarting service: {service_name}")

def flush_cache(service_name: str):
    print(f"[ACTION] Flushing cache for: {service_name}")

# Simulating OpenAI Function Calling
def call_remediation_tool(tool_name, arguments):
    if tool_name == "restart_service":
        restart_service(arguments["service_name"])
    elif tool_name == "flush_cache":
        flush_cache(arguments["service_name"])
    else:
        print(f"[ERROR] Unknown tool: {tool_name}")
