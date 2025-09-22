# Project configuration settings

DATA_PATHS = {
    'raw_events': 'data/raw/wsl_events_all_part*.csv',
    'raw_matches': 'data/raw/wsl_matches_all.csv',
    'processed': 'data/processed/',
    'reports': 'reports/'
}

MODEL_PARAMS = {
    'pitch_length': 105,
    'pitch_width': 68,
    'grid_size': 10
}

TEAM_NAMES = [
    'Arsenal WFC', 'Chelsea FCW', 'Manchester City WFC',
    'Liverpool WFC', 'Tottenham Hotspur Women', 'Everton LFC'
]
