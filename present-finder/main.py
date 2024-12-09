# Sample data structure representing different stores and their prices
STORE_DATA = {
    "emag": {
        "lego_star_wars": {"price": 399.99, "in_stock": True, "shipping": 15},
        "playstation_5": {"price": 2499.99, "in_stock": False, "shipping": 0},
        "airpods": {"price": 899.99, "in_stock": True, "shipping": 15},
        "samsung_tablet": {"price": 1299.99, "in_stock": True, "shipping": 20},
        "board_game": {"price": 149.99, "in_stock": True, "shipping": 12}
    },
    "altex": {
        "lego_star_wars": {"price": 389.99, "in_stock": False, "shipping": 20},
        "playstation_5": {"price": 2599.99, "in_stock": True, "shipping": 0},
        "airpods": {"price": 879.99, "in_stock": True, "shipping": 15},
        "samsung_tablet": {"price": 1399.99, "in_stock": True, "shipping": 0},
        "board_game": {"price": 159.99, "in_stock": True, "shipping": 15}
    },
    "cel": {
        "lego_star_wars": {"price": 409.99, "in_stock": True, "shipping": 12},
        "playstation_5": {"price": 2549.99, "in_stock": True, "shipping": 0},
        "airpods": {"price": 929.99, "in_stock": False, "shipping": 12},
        "samsung_tablet": {"price": 1349.99, "in_stock": True, "shipping": 15},
        "board_game": {"price": 144.99, "in_stock": True, "shipping": 15}
    }
}

PRODUCT_NAMES = {
    "lego_star_wars": "LEGO Star Wars Set",
    "playstation_5": "PlayStation 5 Console",
    "airpods": "Apple AirPods",
    "samsung_tablet": "Samsung Galaxy Tab",
    "board_game": "Monopoly Board Game"
}

def search_product():
    """Search for a product and compare prices"""
    try:
        # Show available products
        print("\nAvailable products:")
        for i, (key, name) in enumerate(PRODUCT_NAMES.items(), 1):
            print(f"{i}. {name}")

        # Get product choice
        choice = int(input("\nEnter product number: "))
        if not 1 <= choice <= len(PRODUCT_NAMES):
            raise ValueError("Invalid product number!")

        # Get product key
        product_key = list(PRODUCT_NAMES.keys())[choice - 1]
        product_name = PRODUCT_NAMES[product_key]

        print(f"\n🎁 Price comparison for {product_name}:")
        print("-" * 50)

        best_price = float('inf')
        best_store = None
        available_stores = []

        # Compare prices across stores
        for store, products in STORE_DATA.items():
            if product_key in products:
                product_info = products[product_key]
                total_price = product_info["price"] + product_info["shipping"]
                
                if product_info["in_stock"]:
                    available_stores.append((store, total_price))
                    if total_price < best_price:
                        best_price = total_price
                        best_store = store

                # Display store information
                status = "✓ In Stock" if product_info["in_stock"] else "✗ Out of Stock"
                print(f"\n{store.upper()}:")
                print(f"Price: {product_info['price']} RON")
                print(f"Shipping: {product_info['shipping']} RON")
                print(f"Total: {total_price} RON")
                print(f"Status: {status}")

        if best_store:
            print(f"\n🏆 Best deal: {best_store.upper()} - {best_price} RON")
        else:
            print("\n❌ Product not available in any store!")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def compare_with_budget():
    """Find products within a budget"""
    try:
        budget = float(input("\nEnter your budget (RON): "))
        if budget <= 0:
            raise ValueError("Budget must be positive!")

        print(f"\n🎁 Products within {budget} RON (including shipping):")
        print("-" * 50)

        found_products = False
        for product_key, product_name in PRODUCT_NAMES.items():
            affordable_stores = []

            for store, products in STORE_DATA.items():
                if product_key in products:
                    product_info = products[product_key]
                    total_price = product_info["price"] + product_info["shipping"]

                    if total_price <= budget and product_info["in_stock"]:
                        affordable_stores.append((store, total_price))

            if affordable_stores:
                found_products = True
                print(f"\n{product_name}:")
                for store, total_price in sorted(affordable_stores, key=lambda x: x[1]):
                    print(f"  {store.upper()}: {total_price} RON")

        if not found_products:
            print("\nNo products found within your budget!")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    while True:
        print("\n🎄 Christmas Present Price Finder 🎄")
        print("\n1. Search specific product")
        print("2. Find products within budget")
        print("3. Exit")

        try:
            choice = input("\nEnter your choice (1-3): ")

            if choice == "1":
                search_product()
            elif choice == "2":
                compare_with_budget()
            elif choice == "3":
                print("\nHappy shopping! 🎅")
                break
            else:
                print("Please enter a number between 1 and 3!")

        except KeyboardInterrupt:
            print("\nExiting program...")
            break

if __name__ == "__main__":
    main()