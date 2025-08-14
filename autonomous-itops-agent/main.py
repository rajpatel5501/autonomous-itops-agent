from agents.supervisor import SupervisorAgent
from utils.kafka_client import consume_alerts

if __name__ == "__main__":
    supervisor = SupervisorAgent()
    for alert in consume_alerts():
        supervisor.handle_alert(alert)
