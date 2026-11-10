# Pocket Mall

Pocket Mall is a command-line shopping application written in Python. It provides a small catalog of grocery, home and kitchen, personal care, and snack products, with account, search, cart, and checkout flows backed by local JSON files.

## Features

- Create an account, log in, update a username or address, and log out.
- Browse products by category, search product names, and view product descriptions.
- Add products to a cart, review quantities and totals, remove items, or empty the cart.
- Place a demo order and receive a checkout confirmation in the terminal.
- Store product, account, and cart data in JSON files.

The checkout is a local demonstration; it does not process payments or submit orders to a service. Product images are included in `images/`; the current command-line interface displays product emojis rather than loading those images.

## Requirements

- Python 3. No third-party packages are required; the application uses the Python standard library.

## Setup and usage

1. Clone the repository and change into the project directory.
2. Run the application:

   ```sh
   python main.py
   ```

3. Use the terminal prompts to create an account or log in, then choose actions from the menus. The app reads and updates its JSON files in the current working directory.

## Data and privacy

The committed `users.json` and `cart.json` contain empty starting data. The application stores account passwords and addresses as plain text in `users.json` and writes cart contents to `cart.json`. Use demo information only; do not enter real passwords, addresses, or other sensitive information. Avoid committing changes to these data files after using the app.

## Project structure

```text
.
├── main.py          # Command-line application
├── products.json    # Product catalog grouped by category
├── users.json       # Local account data (starts empty)
├── cart.json        # Local cart data (starts empty)
└── images/          # Product image assets
```
