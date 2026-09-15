"""Exercise 1: Menu filtering.

Load data/menu.json and print every AVAILABLE item under $10.00,
sorted by price, cheapest first.

Expected output shape:
    Green Tea            $3.25
    Iced Coffee          $4.25
    ...

Requirements:
  - use an f-string for the output
  - type-hint every function you write
"""

import json
from pathlib import Path

MENU_PATH = Path(__file__).parent / "data" / "menu.json"


def load_menu() -> list[dict]:
    """Read the menu file and return it as a list of dictionaries."""
    with MENU_PATH.open() as f:
        return json.load(f)


def available_under(menu: list[dict], limit: float) -> list[dict]:
    """Return available items priced below `limit`, sorted cheapest first."""
    filtered_items = [] #new list var

    for item in menu: #loop through menu
        if item["available"] and item["price"] < limit: #if both available an price is less than limit
            filtered_items.append(item) #add to list

    filtered_items = sorted(
        filtered_items,
        key=lambda item: item["price"] #sort by price
    )

    return filtered_items #return sorted list


def main() -> None:
    menu = load_menu()
    for item in available_under(menu, 10.00):
        print(f"{item['name']:<20} ${item['price']:.2f}")


if __name__ == "__main__":
    main()
