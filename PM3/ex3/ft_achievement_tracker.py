def ft_achievement_tracker() -> None:
    """Function that tracks achievements from different players"""
    print("=== Achievement Tracker System ===\n")
    alice_achievements = {'first_kill', 'level_10',
                          'treasure_hunter', 'speed_demon'}
    bob_achievements = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie_achievements = {'level_10', 'treasure_hunter', 'boss_slayer',
                            'speed_demon', 'perfectionist'}
    all_achievements = alice_achievements.union(bob_achievements,
                                                charlie_achievements)
    common_to_all = alice_achievements.intersection(bob_achievements,
                                                    charlie_achievements)
    alice_only = alice_achievements.difference(bob_achievements,
                                               charlie_achievements)
    bob_only = bob_achievements.difference(alice_achievements,
                                           charlie_achievements)
    charlie_only = charlie_achievements.difference(alice_achievements,
                                                   bob_achievements)
    rare_achievements = alice_only.union(bob_only, charlie_only)
    print(
        f"Player alice achievements: {alice_achievements}\n"
        f"Player bob achievements: {bob_achievements}\n"
        f"Player charlie achievements: {charlie_achievements}\n"
        "\n=== Achievement Analytics ===\n"
        f"All unique achievements: {all_achievements}\n"
        f"Total unique achievements: {len(all_achievements)}\n"
        f"\nCommon to all players: {common_to_all}\n"
        f"Rare achievements (1 player): {rare_achievements}\n"
        "\nAlice vs Bob common: "
        f"{alice_achievements.intersection(bob_achievements)}\n"
        f"Alice unique: {alice_achievements.difference(bob_achievements)}\n"
        f"Bob unique: {bob_achievements.difference(alice_achievements)}"
    )


if __name__ == "__main__":
    ft_achievement_tracker()
