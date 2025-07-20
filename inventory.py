import sqlite3

conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
''')
conn.commit()

def add_item(name, qty):
    cursor.execute('INSERT INTO inventory (item_name, quantity) VALUES (?, ?)', (name, qty))
    conn.commit()

def update_stock(name, qty):
    cursor.execute('UPDATE inventory SET quantity = ? WHERE item_name = ?', (qty, name))
    conn.commit()

def check_inventory():
    cursor.execute('SELECT * FROM inventory')
    rows = cursor.fetchall()
    print("\nCurrent Inventory:")
    for row in rows:
        print(f"{row[1]} - {row[2]} units")

def menu():
    while True:
        print("\n1. Add Item\n2. Update Stock\n3. View Inventory\n4. Exit")
        choice = input("Choose option: ")
        if choice == '1':
            name = input("Item name: ")
            qty = int(input("Quantity: "))
            add_item(name, qty)
        elif choice == '2':
            name = input("Item name: ")
            qty = int(input("New quantity: "))
            update_stock(name, qty)
        elif choice == '3':
            check_inventory()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

menu()
conn.close()
