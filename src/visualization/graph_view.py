from pyvis.network import Network
from neo4j import GraphDatabase
from src.config import *

# Connect to Neo4j
driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

# Create interactive network
net = Network(
    height="750px",
    width="100%",
    bgcolor="#0f172a",
    font_color="white",
    directed=True
)

# Add physics for nice layout
net.barnes_hut()

with driver.session() as session:

    # Get all nodes
    node_query = """
    MATCH (n)
    RETURN id(n) AS id, labels(n) AS labels, n.name AS name
    """

    nodes = session.run(node_query)

    for node in nodes:
        node_id = node["id"]
        labels = node["labels"]
        name = node["name"]

        label = labels[0] if labels else "Node"

        # Color by type
        if label == "Space":
            color = "#22c55e"      # green
            shape = "dot"
            size = 30

        elif label == "Wall":
            color = "#a855f7"      # purple
            shape = "box"
            size = 20

        elif label == "ThermalZone":
            color = "#f59e0b"      # orange
            shape = "ellipse"
            size = 35

        else:
            color = "#64748b"
            shape = "dot"
            size = 20

        net.add_node(
            node_id,
            label=name,
            title=f"{label}: {name}",
            color=color,
            shape=shape,
            size=size
        )

    # Get all relationships
    edge_query = """
    MATCH (a)-[r]->(b)
    RETURN id(a) AS source,
           id(b) AS target,
           type(r) AS rel
    """

    edges = session.run(edge_query)

    for edge in edges:

        color = {
            "ADJACENT_TO": "#38bdf8",
            "BOUNDED_BY": "#94a3b8",
            "PART_OF": "#f59e0b"
        }.get(edge["rel"], "#ffffff")

        net.add_edge(
            edge["source"],
            edge["target"],
            label=edge["rel"],
            color=color,
            arrows="to"
        )

# Save HTML
output_file = "data/outputs/building_graph.html"
net.save_graph(output_file)

print(f"Interactive graph saved to: {output_file}")

driver.close()