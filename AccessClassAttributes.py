class InventoryTag:
    def __init__(self):
        self.item_id = 0
        self.quantity_remaining = 0

red_sweater = InventoryTag()
red_sweater.item_id = int(input())
red_sweater.quantity_remaining = int(input())

InventoryTag.item_id = red_sweater.item_id
InventoryTag.quantity_remaining = red_sweater.quantity_remaining

print(f'ID: {InventoryTag.item_id}')
print(f'Qty: {InventoryTag.quantity_remaining}')
