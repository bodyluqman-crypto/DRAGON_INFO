from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "🐉 Dragon Free Fire API - LIVE",
        "status": "Active", 
        "version": "2.0",
        "developer": "DRAGON",
        "hosting": "Vercel",
        "endpoints": {
            "/": "API Information",
            "/player/<id>": "Get player information",
            "/health": "Health check"
        }
    })

@app.route('/player/<player_id>')
def get_player(player_id):
    ranks = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Heroic"]
    
    player_data = {
        'player_id': player_id,
        'username': f'Player_{player_id}',
        'level': random.randint(1, 100),
        'rank': random.choice(ranks),
        'kills': random.randint(0, 10000),
        'matches': random.randint(0, 5000),
        'win_rate': round(random.uniform(0, 100), 2),
        'region': 'global',
        'last_updated': datetime.now().isoformat()
    }
    
    return jsonify({
        "api": "Dragon Free Fire API",
        "developer": "DRAGON", 
        "data": player_data
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy 🟢",
        "server": "Vercel",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
