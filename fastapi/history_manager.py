search_history = []

def add_to_history(search_request: dict):
    search_history.append(search_request)
    if len(search_history) > 100:  # Limit history to last 100 searches
        search_history.pop(0)

def get_search_history():
    return search_history
