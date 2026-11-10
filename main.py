#importing required modules
import json

# Constants ---
USERS_FILE = 'users.json'
PRODUCTS_FILE = 'products.json'
CART_FILE = 'cart.json'

PRODUCT_EMOJIS = {
    "Aashirvaad Atta - 10kg": "🌾",
    "Tata Salt - 1kg": "🧂",
    "Fortune Sunlite Refined Sunflower Oil - 5L": "🛢️🌻",
    "Daawat Basmati Rice - 5kg": "🍚",
    "Amul Gold Milk - 1L": "🥛",
    "Prestige Pressure Cooker - 5L": "🍲✨",
    "Pigeon Induction": "🔥⚡",
    "Cello Opalware Dinner Set - 20 Pieces": "🍽️",
    "Lifebuoy Soap - Pack of 4": "🧼",
    "Clinic Plus Shampoo - 650ml": "🧴💧",
    "Colgate MaxFresh Toothpaste - 150g": "🦷✨",
    "Britannia Good Day Cashew Cookies - 200g": "🍪🌰",
    "Haldiram's Aloo Bhujia - 1kg": "🍜🔥",
    "Maggi 2-Minute Noodles - Pack of 12": "🍜⏱️",
    "Santoor Sandalwood and Turmeric Soap": "🧼🌿",
    "Vatika Health Shampoo": "🧴🌿",
    "Meswak Toothpaste": "🦷🌿",
    "Cadbury Dairy Milk Chocolate": "🍫",
    "Pulse Candy": "🍬",
    "Parle Melody Chocolaty Toffee": "🍬🍫",
    "Parle-G Biscuits": "🍪"
}

def display_large_emoji(emoji, width=40):
    if emoji:
        print("\n")
        print(f"{emoji.center(width)}")
        print("\n")

def save_user_cart(current_user, user_cart, all_carts):
    all_carts[current_user['username']] = user_cart
    with open(CART_FILE, 'w') as f:
        json.dump(all_carts, f, indent=4)

# Load initial data ---
try:
    with open(USERS_FILE, 'r') as f:
        users = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    users = []

try:
    with open(PRODUCTS_FILE, 'r') as f:
        products = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    products = {}

try:
    with open(CART_FILE, 'r') as f:
        all_carts = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    all_carts = {}





# Product Browsing Function ---
def browse_products(product_list_to_browse, current_user, user_cart, all_carts, is_search_results=False, selected_category_name=None):
    
    if not product_list_to_browse:
        print("No products to display.")
        return False # Stay in shopping area

    i = 0
    while i < len(product_list_to_browse):
        print('\n' * 20) # Clear screen for each new product

        item = product_list_to_browse[i]
        product = item['product']
        category_for_display = item['category'] if is_search_results else selected_category_name

        current_emoji = PRODUCT_EMOJIS.get(product["name"], "")
        display_large_emoji(current_emoji)
        print(f'Product Name: {product["name"]}, Price: ₹{product["price"]}, Category: {category_for_display}')

        action = input('\n(c) Add to Cart | (n) Next | (p) Previous | (v) View Details | (b) Back | (m) Main Menu\nChoose an option: ').lower()
        if action == 'c':
            while True:
                try:
                    quantity_str = input(f'How many {product["name"]}(s) do you want to add to cart? ')
                    quantity = int(quantity_str)
                    if quantity <= 0:
                        print("Quantity must be a positive number.")
                    else:
                        product_name = product["name"]
                        user_cart[product_name] = user_cart.get(product_name, 0) + quantity
                        print(f'{quantity} {product["name"]}(s) added to cart.')
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif action == 'n':
            if i < len(product_list_to_browse) - 1: i += 1
            else: print("You are at the last product in this list.")
        elif action == 'p':
            if i > 0: i -= 1
            else: print("You are at the first product in this list.")
        elif action == 'v':
            print(f'\n--- Details for {product["name"]} ---\n{product.get("description", "No description available.")}\n------------------------------')
        elif action == 'b':
            save_user_cart(current_user, user_cart, all_carts)
            return False # Back to category selection
        elif action == 'm':
            save_user_cart(current_user, user_cart, all_carts)
            return True
        else:
            print("Invalid option. Please choose again.")
    
    # Save cart changes before exiting the browsing loop
    save_user_cart(current_user, user_cart, all_carts)
    return False # Continue in shopping area context

# Main Program Loop ---
current_user = None
for user in users:
    if user.get('logged_in'):
        current_user = user
        break

while True:
    if not current_user:
        # Account System ---
        action = input('Do you want to (1) Sign Up, (2) Log In, or (3) Exit? Enter 1, 2 or 3: ')
        if action == '1':
            username = input('Create a username: ')
            password = input('Create a password: ')
            address = input('Enter your address: ')
            if any(u['username'] == username for u in users):
                print('Username already exists. Please choose another one.')
                continue
            users.append({'username': username, 'password': password, 'address': address, 'logged_in': False})
            with open(USERS_FILE, 'w') as f:
                json.dump(users, f, indent=4)
            print('Sign Up successful! You can now log in.')
        elif action == '2':
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            user_found = None
            for user in users:
                if user['username'] == username and user['password'] == password:
                    user['logged_in'] = True
                    user_found = user
                    break
            if user_found:
                with open(USERS_FILE, 'w') as f:
                    json.dump(users, f, indent=4)
                current_user = user_found
                print(f'Welcome back, {username}!')
            else:
                print('Invalid username or password. Please try again.')
        elif action == '3':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid option. Please enter 1, 2 or 3.')
    else:
        # Main Menu ---
        username = current_user.get('username', 'Customer')
        user_cart = all_carts.get(username, {})
        print(f'\nWelcome to Pocket Mall, {username}!')
        
        print('\nMain Menu:')
        print('1. Shopping area')
        print('2. View Cart')
        print('3. Edit Profile')
        print('4. Logout')
        print('5. Exit')
        choice = input('Choose an option (1-5): ')

        if choice == '1':
            # Shopping Area ---
            if not products:
                print("No products available.")
            else:
                back_to_main_menu = False
                while not back_to_main_menu: # Category selection loop

                    print("\n--- Shopping Area ---")
                    category_list = list(products.keys())
                    for i, category_name in enumerate(category_list):
                        print(f"{i + 1}. Browse {category_name}")
                    print(f"(s) Search for a Product")
                    print(f"(m) Back to Main Menu")

                    category_choice = input("Choose an option (number, 's', or 'm'): ")
                    if category_choice.lower() == 's':
                        query = input("Enter product name to search: ")
                        found_products = []
                        if products:
                            for category, product_list in products.items():
                                for product in product_list:
                                    if query.lower() in product['name'].lower():
                                        found_products.append({'product': product, 'category': category})
                        
                        if not found_products:
                            print(f"No products found matching '{query}'.")
                        else:
                            main_menu_requested = browse_products(found_products, current_user, user_cart, all_carts, is_search_results=True)
                            if main_menu_requested:
                                back_to_main_menu = True
                    elif category_choice.lower() == 'm':
                        back_to_main_menu = True
                    else:
                        try:
                            category_index = int(category_choice) - 1
                            if 0 <= category_index < len(category_list):
                                selected_category_name = category_list[category_index]
                                products_in_category = products[selected_category_name]
                                
                                browsable_products = [{'product': p, 'category': selected_category_name} for p in products_in_category]
                                
                                main_menu_requested = browse_products(browsable_products, current_user, user_cart, all_carts, selected_category_name=selected_category_name)
                                if main_menu_requested:
                                    back_to_main_menu = True
                            else:
                                print("Invalid option. Please choose again.")
                        except ValueError:
                            print("Invalid input. Please enter a number for category, 's' for search, or 'm' for main menu.")

        elif choice == '2':
            # View Cart ---
                        cart_active = True
                        while cart_active:

                            if not user_cart:
                                print("\nYour cart is empty.")
                                cart_active = False # No items, so exit cart view
                            else:
                                print("\nYour Cart:")
                                total_price = 0
                                cart_items = list(user_cart.items())
                                all_products_flat = [p for category_products in products.values() for p in category_products]
                                
                                for i, (product_name, quantity) in enumerate(cart_items, 1):
                                    product_details = next((p for p in all_products_flat if p['name'] == product_name), None)
                                    if product_details:
                                        price = product_details['price']
                                        total_price += price * quantity
                                        print(f'{i}. {product_name}: {quantity} x ₹{price} = ₹{quantity * price}')
                                print(f'\nTotal Price: ₹{total_price}')
                                
                                action = input('\n(d) Delete item | (e) Empty cart | (p) Place Order | (m) Main Menu\nChoose an option: ').lower()
                                if action == 'd':
                                    try:
                                        item_number = int(input("Enter the number of the item to delete: "))
                                        if 1 <= item_number <= len(cart_items):
                                            item_to_delete = cart_items[item_number - 1][0]
                                            del user_cart[item_to_delete]
                                            print(f"{item_to_delete} has been removed from your cart.")
                                        else:
                                            print("Invalid item number.")
                                    except ValueError:
                                        print("Invalid input. Please enter a number.")
                                elif action == 'e':
                                    user_cart.clear()
                                    print("Your cart has been emptied.")
                                    cart_active = False # Exit cart view after emptying
                                elif action == 'p':
                                    # Place Order ---
                                    if not user_cart:
                                        print("Your cart is empty. Nothing to order.")
                                    else:
                                        address = current_user.get('address')
                                        print("Placing your order...")
                                        if address:
                                            print(f"Your order has been placed successfully!\nYour package will be delivered to {address} soon.")
                                        else:
                                            print("Your order has been placed successfully!\n(No delivery address on file — please add your address in your account.)")
                                        user_cart.clear()
                                        cart_active = False # Exit cart view after placing order
                                elif action == 'm':
                                    cart_active = False # Exit cart view
                                else:
                                    print("Invalid option. Please choose again.")
                            
                            # Save cart changes before exiting the cart_active loop
                            all_carts[username] = user_cart
                            with open(CART_FILE, 'w') as f:
                                json.dump(all_carts, f, indent=4)
        
        elif choice == '3':
            # Edit Profile ---

            print("What would you like to edit?")
            print("1. Username")
            print("2. Address")
            edit_choice = input("Choose an option (1-2): ")
            
            user_to_edit = None
            user_index = -1
            for idx, user in enumerate(users):
                if user['username'] == current_user['username']:
                    user_to_edit = user
                    user_index = idx
                    break
            
            if user_to_edit:
                if edit_choice == '1':
                    new_username = input("Enter your new username: ")
                    if any(u['username'] == new_username for u in users if u['username'] != current_user['username']):
                        print("Username already exists. Please choose another one.")
                    else:
                        old_username = current_user['username']
                        user_to_edit['username'] = new_username
                        current_user['username'] = new_username # Update current_user in session
                        
                        # Update all_carts with new username
                        if old_username in all_carts:
                            all_carts[new_username] = all_carts.pop(old_username)
                        
                        # Update the user in the main users list
                        users[user_index] = user_to_edit
                        
                        with open(USERS_FILE, 'w') as f:
                            json.dump(users, f, indent=4)
                        with open(CART_FILE, 'w') as f:
                            json.dump(all_carts, f, indent=4)
                        print("Username updated successfully.")
                elif edit_choice == '2':
                    new_address = input("Enter your new address: ")
                    user_to_edit['address'] = new_address
                    current_user['address'] = new_address # Update current_user in session
                    with open(USERS_FILE, 'w') as f:
                        json.dump(users, f, indent=4)
                    print("Address updated successfully.")
                else:
                    print("Invalid option.")
            else:
                print("Could not find your user profile to edit.")

        elif choice == '4':
            # Logout ---
            print('Logging out...')
            for user in users:
                if user.get('logged_in'):
                    user['logged_in'] = False
                    break
            with open(USERS_FILE, 'w') as f:
                json.dump(users, f, indent=4)
            current_user = None

        elif choice == '5':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid option. Please choose again.')
