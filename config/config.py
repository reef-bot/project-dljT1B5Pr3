import json

# Load bot configuration
with open('prefix.json', 'r') as f:
    data = json.load(f)
    bot_prefix = data['prefix']