from utils.openai_functions import call_remediation_tool

class RemediationAgent:
    def remediate(self, service_name, solution):
        print(f"[RemediationAgent] Executing remediation for {service_name}: {solution}")
        
        if "restart" in solution.lower():
            call_remediation_tool("restart_service", {"service_name": service_name})
        if "flush" in solution.lower():
            call_remediation_tool("flush_cache", {"service_name": service_name})
