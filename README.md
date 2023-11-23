# Shopping Cart Service API

Welcome to the Shopping Cart Service API! This API provides endpoints to manage shopping carts for an e-commerce application.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the Shopping Cart Service API, follow these steps:

### Prerequisites

- Docker installed on your system

### Installation Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/munuhee/shopping-cart-service.git
    ```

2. Navigate to the project directory:

    ```bash
    cd shopping-cart-service
    ```

3. Run the setup script:

    ```bash
    ./bin/setup.sh
    ```

The setup script will build the Docker image for the service and start the Flask app on port 8080.

## Usage

Once the setup is complete, the API will be available at:

- Local: [http://localhost:8080](http://localhost:8080)
- Remote: `http://YOUR_SERVER_IP:8080` (replace `YOUR_SERVER_IP` with your server's IP address)

### Available Endpoints

- `/cart`: Manages shopping carts
  - `GET`: Retrieve all shopping carts
  - `POST`: Create a new shopping cart

- `/carts/<cart_id>`: Manages a specific shopping cart
  - `GET`: Retrieve details of a cart
  - `PUT`: Update a cart
  - `DELETE`: Delete a cart

Refer to `routes.py` for a complete list of available endpoints and their functionalities.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements, bug fixes, or new features.
