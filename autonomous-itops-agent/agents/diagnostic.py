from utils.pinecone_client import search_similar_incidents

class DiagnosticAgent:
    def diagnose(self, alert):
        print(f"[DiagnosticAgent] Analyzing issue: {alert['issue']}")
        historical_solution = search_similar_incidents(alert["issue"])
        return historical_solution
