from agents.diagnostic import DiagnosticAgent
from agents.remediation import RemediationAgent

class SupervisorAgent:
    def __init__(self):
        self.diagnostic_agent = DiagnosticAgent()
        self.remediation_agent = RemediationAgent()

    def handle_alert(self, alert):
        print(f"\n[SupervisorAgent] Received alert for {alert['service']}: {alert['issue']}")
        solution = self.diagnostic_agent.diagnose(alert)
        if solution and solution != "No historical match found":
            self.remediation_agent.remediate(alert["service"], solution)
        else:
            print("[SupervisorAgent] No auto-remediation found. Escalating to human.")
