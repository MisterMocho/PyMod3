def ft_achievement_tracker() -> None:
    """Function that tracks achievements from different players"""
    print("=== Achievement Tracker System ===\n")
    alice_achieved: set[str] = {'first_kill', 'level_10',
                                'treasure_hunter', 'speed_demon'}
    bob_achieved: set[str] = {'first_kill', 'level_10',
                              'boss_slayer', 'collector'}
    charlie_achieved: set[str] = {'level_10', 'treasure_hunter', 'boss_slayer',
                                  'speed_demon', 'perfectionist'}
    all_achievements: set[str] = alice_achieved.union(bob_achieved,
                                                      charlie_achieved)
    common_to_all: set[str] = alice_achieved.intersection(bob_achieved,
                                                          charlie_achieved)
    alice_only: set[str] = alice_achieved.difference(bob_achieved,
                                                     charlie_achieved)
    bob_only: set[str] = bob_achieved.difference(alice_achieved,
                                                 charlie_achieved)
    charlie_only: set[str] = charlie_achieved.difference(alice_achieved,
                                                         bob_achieved)
    rare_achievements: set[str] = alice_only.union(bob_only, charlie_only)
    print(
        f"Player alice achievements: {alice_achieved}\n"
        f"Player bob achievements: {bob_achieved}\n"
        f"Player charlie achievements: {charlie_achieved}\n"
        "\n=== Achievement Analytics ===\n"
        f"All unique achievements: {all_achievements}\n"
        f"Total unique achievements: {len(all_achievements)}\n"
        f"\nCommon to all players: {common_to_all}\n"
        f"Rare achievements (1 player): {rare_achievements}\n"
        "\nAlice vs Bob common: "
        f"{alice_achieved.intersection(bob_achieved)}\n"
        f"Alice unique: {alice_achieved.difference(bob_achieved)}\n"
        f"Bob unique: {bob_achieved.difference(alice_achieved)}"
    )


if __name__ == "__main__":
    ft_achievement_tracker()
