# I Transitively Defeat a Pro

🏆 **"I Transitively Defeat a Pro" – Claim Your Victory Over the Pros!** 🏆

Ever dreamed of saying you defeated a Dota 2 pro? With *I Transitively Defeat a Pro*, now you can! 🚀

This Python tool builds a web of transitive victories: if a pro loses to a player, and you defeat that player, you’re connected in a chain of champions leading back to the pro. By analyzing match histories through the OpenDota API, our tool constructs a **graph of players who can proudly say they "transitively defeated" the pros**!

### 🔥 Features:
- **Dynamic Graph Creation**: Track paths of defeat right back to your favorite pro players.
- **Depth Control**: Specify how far back you want to trace victories.
- **Perfect for Dota 2 Fans**: Get bragging rights by proving your place in the pro-defeating hierarchy!

---

## How It Works

1. **Graph Construction**: The tool begins with a pro player’s recent matches where they lost, identifies the players on the winning team, and builds a graph of these "defeaters."
2. **Transitive Defeat**: For each player in the graph, it continues to retrieve matches and identify players who have defeated them, creating chains of transitive defeat up to a specified depth.
3. **Breadth-First Search (BFS)**: A BFS algorithm is used with OpenDota's API to retrieve match details, enabling efficient exploration of defeat chains.

## Example

```python
# Replace with actual pro player's ID and API key (if available)
pro_player_id = 123456789
api_key = 'YOUR_API_KEY'

# Generate graph of players who transitively defeated the pro
defeated_graph = transitively_defeat_pro(pro_player_id, depth_limit=10, api_key=api_key)

# Display results
for player, defeaters in defeated_graph.items():
    print(f"Player {player} is defeated by: {defeaters}")