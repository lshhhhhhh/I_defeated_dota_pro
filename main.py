from collections import deque, defaultdict
import requests
import time


def fetch_matches(player_id, limit=10, api_key=None):
    """
    Fetches recent matches for a player where they lost, limited to the specified number.
    """
    url = f"https://api.opendota.com/api/players/{player_id}/matches"
    params = {
        'limit': limit,
        'api_key': api_key,
        'win': 0  # Only fetch matches where the player lost
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return []


def fetch_match_details(match_id, api_key=None):
    """
    Fetches detailed information for a specific match, including all players and the winning team.
    """
    url = f"https://api.opendota.com/api/matches/{match_id}"
    params = {'api_key': api_key} if api_key else {}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None


def get_opponents_in_match(match_details):
    """
    Finds all opponents on the winning team who defeated the specified player.
    """
    # Determine the winning team directly from match_details
    winning_team = match_details['radiant_win']
    # Collect account IDs of players on the winning team
    opponents = [
        p['account_id'] for p in match_details['players']
        if (p['player_slot'] < 128) == winning_team and 'account_id' in p
    ]
    return opponents

def transitively_defeat_pro(pro_player_id, depth_limit=10, api_key=None):
    """
    Constructs a graph of players who transitively defeated the pro player up to a given depth limit.
    """
    graph = defaultdict(list)  # Store edges: {defeated_player: [defeaters]}
    visited = set()  # Track visited players to avoid cycles
    queue = deque([(pro_player_id, 0)])  # Queue stores (player_id, depth)

    while queue:
        player_id, depth = queue.popleft()

        # Stop if depth limit is reached
        if depth >= depth_limit:
            continue

        # Fetch matches where the current player lost
        matches = fetch_matches(player_id, api_key=api_key)
        for match in matches:
            match_details = fetch_match_details(match['match_id'], api_key=api_key)
            if not match_details:
                continue  # Skip if match details could not be fetched

            # Find all players who defeated the current player in this match
            opponents = get_opponents_in_match(match_details)
            for opponent in opponents:
                if opponent not in visited:
                    visited.add(opponent)
                    graph[player_id].append(opponent)
                    queue.append((opponent, depth + 1))

            # Small delay to avoid hitting API rate limits
            time.sleep(0.5)

    return graph




graph=transitively_defeat_pro("pro_id",1,"api_key")
print(graph)
