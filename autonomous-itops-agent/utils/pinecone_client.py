def search_similar_incidents(issue):
    # In real system, this would query Pinecone
    mock_db = {
        "High error rate detected": "Restart service and clear cache",
        "Memory usage exceeded threshold": "Flush Redis cache and restart"
    }
    return mock_db.get(issue, "No historical match found")
