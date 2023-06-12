# OSPF Network Visualization

This project is a web application that visualizes OSPF (Open Shortest Path First) networks. It allows users to generate a network of routers and visualize the shortest path between any two routers.

## Features

- Generate a network of routers with random weights
- Visualize the network in an interactive graph
- Highlight the shortest path between any two routers

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/Arthur-Systems/PyNetProject.git
    ```

2. Navigate to the project directory:

    ```
    cd ospf-network-visualization
    ```

3. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Start the Flask server:

    ```
    python app.py
    ```

2. Open a web browser and navigate to `http://localhost:5500`.

3. Enter the number of routers and the weights of the connections between them.

4. Select two routers to find the shortest path between them.

5. Click the "Submit" button to generate the network and visualize the shortest path.

## Technologies Used

- Python
- Flask
- NetworkX
- Pyvis
- Tailwind CSS
