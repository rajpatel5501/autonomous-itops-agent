import time

def consume_alerts():
    alerts = [
        {"service": "nginx", "issue": "High error rate detected"},
        {"service": "redis", "issue": "Memory usage exceeded threshold"}
    ]
    for alert in alerts:
        yield alert
        time.sleep(2)  # Simulate time gap
