from src.ingestion.ifc_parser import (
    parse_ifc,
    get_space_area,
    get_space_location
)

from src.graph.neo4j_loader import Neo4jLoader
from src.utils.spatial import are_adjacent


def main():
    print("=== DM-BIM-BEM Pipeline ===")

    # -----------------------------------
    # Parse IFC file
    # -----------------------------------
    data = parse_ifc("data/sample.ifc")

    # -----------------------------------
    # Connect to Neo4j
    # -----------------------------------
    loader = Neo4jLoader()

    # Store space information for adjacency checks
    space_data = []

    # -----------------------------------
    # Create Space nodes
    # -----------------------------------
    for space in data["spaces"]:

        space_name = space.Name or f"Space_{space.id()}"

        # Extract area
        space_area = get_space_area(space)

        # Extract location
        x, y, z = get_space_location(space)

        print(f"\nCreating Space: {space_name}")
        print(f"  Area: {space_area}")
        print(f"  Location: ({x}, {y}, {z})")

        # Create node in Neo4j
        loader.create_space(
            space_name,
            space_area,
            x,
            y,
            z
        )

        # Save for adjacency inference
        space_data.append({
            "name": space_name,
            "coords": (x, y, z)
        })

    # -----------------------------------
    # Create Wall nodes
    # -----------------------------------
    wall_names = []

    for wall in data["walls"]:

        wall_name = wall.Name or f"Wall_{wall.id()}"

        print(f"Creating Wall: {wall_name}")

        loader.create_wall(wall_name)

        wall_names.append(wall_name)

    # -----------------------------------
    # Create BOUNDED_BY relationships
    # -----------------------------------
    print("\nCreating BOUNDED_BY relationships...")

    for space in space_data:
        for wall_name in wall_names:

            loader.create_bounded_by(
                space["name"],
                wall_name
            )

    # -----------------------------------
    # Create ADJACENT_TO relationships
    # -----------------------------------
    print("Creating ADJACENT_TO relationships...")

    for i in range(len(space_data)):
        for j in range(i + 1, len(space_data)):

            s1 = space_data[i]
            s2 = space_data[j]

            if are_adjacent(
                s1["coords"],
                s2["coords"],
                threshold=5.0
            ):

                print(
                    f"Adjacent: {s1['name']} <-> {s2['name']}"
                )

                loader.create_adjacency(
                    s1["name"],
                    s2["name"]
                )

    # -----------------------------------
    # Close Neo4j connection
    # -----------------------------------
    loader.close()

    print("\nPipeline completed successfully.")
    print(f"Spaces loaded: {len(space_data)}")
    print(f"Walls loaded: {len(wall_names)}")


if __name__ == "__main__":
    main()