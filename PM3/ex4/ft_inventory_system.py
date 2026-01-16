import sys


def ft_inventory_system() -> None:
    """Function that takes items and adds them to the inventory"""
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        try:
            item, qty = arg.split(':')
            inventory.update({item: int(qty)})
        except ValueError:
            print(f"Skipping invalid format {arg}")
            continue
    total_items: int = sum(inventory.values())
    unique_items: int = len(inventory)
    sorted_items: list[tuple[str, int]] = sorted(inventory.items(),
                                                 key=lambda x: x[1],
                                                 reverse=True)
    print(
        "=== Inventory System Analysis ===\n"
        f"Total items in inventory: {total_items}\n"
        f"Unique item types: {unique_items}\n"
        "\n=== Current Inventory ==="
    )
    for items, qtys in sorted_items:
        percentage: float = ((qtys / total_items) * 100
                             if total_items > 0 else 0)
        unit: str = "unit" if qtys == 1 else "units"
        print(f"{items}: {qtys} {unit} ({percentage:.1f}%)")
    if sorted_items:
        most_item, most_qty = sorted_items[0]
        least_item, least_qty = sorted_items[-1]
        most_unit = "units" if most_qty > 1 else "unit"
        least_unit = "units" if least_qty > 1 else "unit"
        print(
            "\n=== Inventory Statistics ===\n"
            f"Most abundant: {most_item} ({most_qty} {most_unit})\n"
            f"Least abundant: {least_item} ({least_qty} {least_unit})\n"
        )
        moderate: dict[str, int] = {}
        scarce: dict[str, int] = {}
        for name, rarity in sorted_items:
            if (rarity >= 5):
                moderate.update({name: rarity})
            else:
                scarce.update({name: rarity})
        print(
            "=== Item Categories ===\n"
            f"Moderate: {moderate}\n"
            f"Scarce: {scarce}\n"
        )
        restock_needed: list[str] = []
        for itemr, qtt in sorted_items:
            if (qtt < 2):
                if itemr not in restock_needed:
                    restock_needed.append(itemr)
        print(
            "=== Management Suggestions ===\n"
            f"Restock needed: {restock_needed}\n"
        )
    check_item: str = 'sword'
    is_in: bool = check_item in inventory
    print(
        "=== Dictionary Properties Demo ===\n"
        f"Dictionary keys: {list(inventory.keys())}\n"
        f"Dictionary values: {list(inventory.values())}\n"
        f"Sample lookup - '{check_item}' in inventory: {is_in}"
    )


if __name__ == "__main__":
    ft_inventory_system()
