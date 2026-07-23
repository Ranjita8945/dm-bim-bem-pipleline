from neo4j import GraphDatabase
from src.config import *


class Neo4jLoader:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            NEO4J_URI,
            auth=(NEO4J_USER, NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()

    # -----------------------------
    # Create Space node
    # -----------------------------
    def create_space(self, name, area=None, x=None, y=None, z=None):
        query = """
        MERGE (s:Space {name: $name})
        SET s.area = $area,
            s.x = $x,
            s.y = $y,
            s.z = $z
        """
        with self.driver.session() as session:
            session.run(
                query,
                name=name,
                area=area,
                x=x,
                y=y,
                z=z
            )

    # -----------------------------
    # Create Wall node
    # -----------------------------
    def create_wall(self, name):
        query = """
        MERGE (w:Wall {name: $name})
        """
        with self.driver.session() as session:
            session.run(query, name=name)

    # -----------------------------
    # Create BOUNDED_BY relationship
    # -----------------------------
    def create_bounded_by(self, space_name, wall_name):
        query = """
        MATCH (s:Space {name: $space_name})
        MATCH (w:Wall {name: $wall_name})
        MERGE (s)-[:BOUNDED_BY]->(w)
        """
        with self.driver.session() as session:
            session.run(
                query,
                space_name=space_name,
                wall_name=wall_name
            )

    # -----------------------------
    # Create ADJACENT_TO relationship
    # -----------------------------
    def create_adjacency(self, space1, space2):
        query = """
        MATCH (a:Space {name: $space1})
        MATCH (b:Space {name: $space2})
        MERGE (a)-[:ADJACENT_TO]-(b)
        """
        with self.driver.session() as session:
            session.run(query, space1=space1, space2=space2)