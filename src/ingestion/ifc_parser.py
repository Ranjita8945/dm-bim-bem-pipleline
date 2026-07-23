import ifcopenshell
import ifcopenshell.util.element


def get_space_area(space):
    """Extract area from IFC property sets"""

    psets = ifcopenshell.util.element.get_psets(space)

    # IFC quantity takeoff
    qto = psets.get("Qto_SpaceBaseQuantities", {})

    area = qto.get("NetFloorArea")

    return area


def parse_ifc(file_path):
    model = ifcopenshell.open(file_path)

    spaces = model.by_type("IfcSpace")
    walls = model.by_type("IfcWall")

    print(f"Spaces found: {len(spaces)}")
    print(f"Walls found: {len(walls)}")

    return {
        "spaces": spaces,
        "walls": walls
    }

def get_space_location(space):
    """Extract approximate space location"""

    try:
        placement = space.ObjectPlacement
        coords = placement.RelativePlacement.Location.Coordinates

        x = coords[0] if len(coords) > 0 else 0
        y = coords[1] if len(coords) > 1 else 0
        z = coords[2] if len(coords) > 2 else 0

        return x, y, z

    except Exception:
        return None, None, None