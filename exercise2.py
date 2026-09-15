"""Exercise 2: A Cart class.

Implement Cart so the example at the bottom of this file behaves correctly.

  add_item(item, qty=1)  add an item; if it is already in the cart,
                         increase the quantity instead of adding a second line
  remove_item(item_id)   remove that item entirely
  clear()                empty the cart
  total()                sum of price * qty across all lines, rounded to 2dp
  __repr__()             something readable, e.g. <Cart 3 items, $27.75>

Store each line as a dictionary:
    {"item_id": 1, "name": "Tonkotsu Ramen", "price": 16.50, "qty": 2}
"""

from exercise1 import load_menu # what are we importing here? Food for thought.


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
        for line in self.lines: #find the line in the cart that matches the item being added. If there, incr quantity. If not, add a new line to the cart.
            if line["item_id"] == item["id"]:
                line["qty"] += qty
                return
        self.lines.append({ #if not found, add a new line to the cart.
            "item_id": item["id"],
            "name": item["name"],
            "price": item["price"],
            "qty": qty,
        })

    def remove_item(self, item_id: int) -> None:
        self.lines = [ #go through the cart and only keep the lines that do not match the item_id being removed.
            line for line in self.lines
            if line["item_id"] != item_id
        ]

    def clear(self) -> None:
        self.lines.clear() #clear the cart by removing all lines.

    def total(self) -> float:
        total = 0.0 #calculate the total by going through each line in the cart and multiplying the price by the quantity, then adding it to the total.
        for line in self.lines:
            total += line["price"] * line["qty"]

        return round(total, 2) #round once at end out of loop.

    def __repr__(self) -> str:
        return f"<Cart {len(self.lines)} items, ${self.total():.2f}>" #return "Cart <#of lines> items, $<total price to 2 decimal places>"


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]
    ramen = menu[0]

    cart = Cart()
    cart.add_item(gyoza, 2)
    cart.add_item(gyoza, 1)      # should become qty 3, NOT a second line
    cart.add_item(ramen, 1)

    print(cart)                  # <Cart 2 items, $40.50>
    print(len(cart.lines))       # 2
    print(cart.total())          # 40.5
