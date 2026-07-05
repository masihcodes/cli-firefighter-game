import json
import random
from pathlib import Path


def get_game_data(filename='maps.json'):
    data_path = Path(__file__).parent / filename

    with open(data_path, 'r', encoding='utf-8') as f:
        all_maps = json.load(f)

    selected_map = random.choice(all_maps)

    print(f"\033[36m🗺️  Loaded Map: {selected_map['name']}\033[0m")

    start_ply_pos = [tuple(item) for item in selected_map["start_ply_pos"]]
    hash_points = [tuple(item) for item in selected_map["hash_points"]]
    p_points = [tuple(item) for item in selected_map["p_points"]]
    e_points = [tuple(item) for item in selected_map["e_points"]]

    return (
        start_ply_pos,
        hash_points,
        p_points,
        e_points,
        selected_map["game_height"],
        selected_map["game_width"],
        selected_map["total_people"]
    )
