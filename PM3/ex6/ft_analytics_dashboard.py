from typing import Any


def ft_analytics_dashboard() -> None:
    """Demonstrates List, Dict, and Set comprehensions for data analysis."""
    game_data: list[dict[str, Any]] = [
        {"name": "alice", "score": 2300, "region": "north",
         "achievements": ["first_kill", "boss_slayer"], "active": True},
        {"name": "bob", "score": 1800, "region": "east",
            "achievements": ["first_kill"], "active": True},
        {"name": "charlie", "score": 2150, "region": "north",
            "achievements": ["first_kill", "level_10"], "active": True},
        {"name": "diana", "score": 2050, "region": "south",
            "achievements": ["level_10", "collector"], "active": False}
    ]
    h_scores: list[str] = [gamer["name"] for gamer in game_data
                           if gamer["score"] > 2000]
    d_scores: list[int] = [gamer["score"] * 2 for gamer in game_data]
    a_player: list[str] = [gamer["name"] for gamer in game_data
                           if gamer["active"]]
    p_scores: dict[str, int] = {gamer["name"]: gamer["score"]
                                for gamer in game_data
                                if gamer["active"]}
    score_cat: list[str] = [("high" if gamer["score"] > 2200
                            else "medium" if gamer["score"] > 2000
                            else "low") for gamer in game_data]
    cat_count: dict[str, int] = {cat: score_cat.count(cat)
                                 for cat in ["high", "medium", "low"]
                                 if cat in score_cat}
    p_ach_count: dict[str, int] = {gamer["name"]: len(gamer["achievements"])
                                   for gamer in game_data}
    uniq_p: set[str] = {gamer["name"] for gamer in game_data}
    uniq_ach: set[str] = {ach for g in game_data for ach in g["achievements"]}
    active_reg: set[str] = {g["region"] for g in game_data if g["active"]}
    avg_score: float = sum(g["score"] for g in game_data) / len(uniq_p)
    top_p: dict[str, Any] = max(game_data, key=lambda g: g["score"])
    print(
        "=== Game Analytics Dashboard ===\n"
        "\n=== List Comprehension Examples ===\n"
        f"High scorers (>2000): {h_scores}\n"
        f"Scores doubled: {d_scores}\n"
        f"Active players: {a_player}\n"
        "\n=== Dict Comprehension Examples ===\n"
        f"Player scores: {p_scores}\n"
        f"Score categories: {cat_count}\n"
        f"Achievement counts: {p_ach_count}\n"
        "\n=== Set Comprehension Examples ===\n"
        f"Unique players: {uniq_p}\n"
        f"Unique achievements: {uniq_ach}\n"
        f"Active regions: {active_reg}\n"
        "\n=== Combined Analysis ===\n"
        f"Total players: {len(uniq_p)}\n"
        f"Total unique achievements: {len(uniq_ach)}\n"
        f"Average score: {avg_score:.1f}\n"
        f"Top performer: {top_p['name']} ({top_p['score']} points, "
        f"{len(top_p['achievements'])} achievements)"
    )


if __name__ == "__main__":
    ft_analytics_dashboard()
