import json
from pathlib import Path


def create_level(name, height, width, start, exit_pos, people, interior_walls):
    walls = set()

    for r in range(height):
        walls.add((r, 0))
        walls.add((r, width - 1))
    for c in range(width):
        walls.add((0, c))
        walls.add((height - 1, c))

    for wall in interior_walls:
        walls.add(wall)

    walls.discard(start)
    walls.discard(exit_pos)
    for p in people:
        walls.discard(p)

    return {
        "name": name,
        "game_height": height,
        "game_width": width,
        "start_ply_pos": [list(start)],
        "e_points": [list(exit_pos)],
        "p_points": [list(p) for p in people],
        "total_people": len(people),
        "hash_points": [list(w) for w in sorted(walls)]
    }


def generate_all_maps():
    maps = [
        create_level(
            name="1. Training Room", height=7, width=10,
            start=(1, 1), exit_pos=(1, 8),
            people=[(1, 4), (3, 3), (5, 7), (5, 3)],
            interior_walls=[(2, 3), (2, 4), (4, 3), (4, 4)]
        ),
        create_level(
            name="2. Office Corridor", height=10, width=15,
            start=(1, 1), exit_pos=(8, 13),
            people=[(2, 5), (5, 2), (7, 10), (3, 12), (8, 5)],
            interior_walls=[(2, 7), (3, 7), (4, 7), (5, 7),
                            (6, 7), (7, 7), (3, 3), (3, 4), (7, 3), (7, 4)]
        ),
        create_level(
            name="3. The Big Warehouse", height=14, width=20,
            start=(1, 1), exit_pos=(12, 18),
            people=[(2, 2), (4, 7), (6, 15), (8, 3), (9, 17), (11, 6)],
            interior_walls=[(3, 3), (3, 4), (3, 5), (3, 6), (6, 8), (7, 8), (8, 8),
                            (9, 8), (5, 13), (6, 13), (7, 13), (10, 4), (10, 5), (10, 6), (10, 7)]
        ),
        create_level(
            name="4. The Maze", height=9, width=13,
            start=(1, 1), exit_pos=(7, 11),
            people=[(1, 11), (7, 1), (4, 6), (3, 9)],
            interior_walls=[(1, 3), (2, 3), (3, 3), (5, 3), (6, 3), (7, 3), (2, 6),
                            (3, 6), (4, 6), (5, 6), (6, 6), (2, 9), (3, 9), (4, 9), (5, 9), (7, 9)]
        ),
        create_level(
            name="5. Chemistry Lab", height=11, width=11,
            start=(5, 5), exit_pos=(1, 9),
            people=[(1, 1), (9, 1), (9, 9), (2, 5), (8, 5)],
            interior_walls=[(3, 3), (3, 4), (3, 6), (3, 7), (7, 3),
                            (7, 4), (7, 6), (7, 7), (4, 3), (6, 3), (4, 7), (6, 7)]
        ),
        create_level(
            name="6. City Hospital", height=12, width=18,
            start=(1, 1), exit_pos=(10, 16),
            people=[(2, 8), (5, 15), (9, 2), (10, 9), (5, 6), (3, 13)],
            interior_walls=[(4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 9), (4, 10), (4, 11), (4, 13), (4, 14), (
                4, 15), (8, 2), (8, 3), (8, 4), (8, 6), (8, 7), (8, 8), (8, 10), (8, 11), (8, 12), (8, 14), (8, 15), (8, 16)]
        ),
        create_level(
            name="7. Underground Parking", height=10, width=16,
            start=(1, 1), exit_pos=(8, 1),
            people=[(1, 14), (4, 8), (8, 14), (5, 3)],
            interior_walls=[(2, 3), (2, 4), (2, 7), (2, 8), (2, 11), (2, 12), (5, 3), (5, 4), (
                5, 7), (5, 8), (5, 11), (5, 12), (7, 3), (7, 4), (7, 7), (7, 8), (7, 11), (7, 12)]
        ),
        create_level(
            name="8. Grand Hotel", height=13, width=15,
            start=(6, 1), exit_pos=(6, 13),
            people=[(1, 2), (1, 12), (11, 2), (11, 12), (6, 7)],
            interior_walls=[(3, 1), (3, 2), (3, 3), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 11), (3, 12), (
                3, 13), (9, 1), (9, 2), (9, 3), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 11), (9, 12), (9, 13)]
        ),
        create_level(
            name="9. Shopping Mall", height=11, width=22,
            start=(5, 1), exit_pos=(5, 20),
            people=[(1, 10), (9, 10), (2, 18), (8, 3),
                    (5, 10), (2, 5), (8, 16)],
            interior_walls=[(2, 8), (3, 8), (4, 8), (6, 8), (7, 8), (8, 8),
                            (2, 13), (3, 13), (4, 13), (6, 13), (7, 13), (8, 13)]
        ),
        create_level(
            name="10. The Inferno Challenge", height=15, width=20,
            start=(1, 1), exit_pos=(13, 18),
            people=[(1, 18), (13, 1), (7, 10), (3, 10),
                    (11, 10), (7, 3), (7, 16), (4, 15)],
            interior_walls=[
                (2, 2), (2, 4), (2, 6), (2, 8), (2, 11), (2, 13), (2, 15), (2, 17),
                (4, 2), (4, 4), (4, 6), (4, 8), (4, 11), (4, 13), (4, 15), (4, 17),
                (6, 5), (6, 6), (6, 7), (6, 8), (6, 11), (6, 12), (6, 13), (6, 14),
                (8, 5), (8, 6), (8, 7), (8, 8), (8, 11), (8, 12), (8, 13), (8, 14),
                (10, 2), (10, 4), (10, 6), (10, 8), (10,
                                                     11), (10, 13), (10, 15), (10, 17),
                (12, 2), (12, 4), (12, 6), (12, 8), (12,
                                                     11), (12, 13), (12, 15), (12, 17)
            ]
        )
    ]

    save_path = Path(__file__).parent / 'maps.json'
    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(maps, f, indent=4)
    print(
        f"✅ {len(maps)} maps successfully generated and in the 'maps.json' file saved.")


if __name__ == "__main__":
    generate_all_maps()
