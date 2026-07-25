# 🏗️ DM-BIM-BEM Pipeline
### A Fully Automated Graph-Based BIM to Building Energy Modeling Pipeline

## 📌 Overview

The **DM-BIM-BEM Pipeline** is an automated framework that transforms Building Information Models (BIM) into a semantic knowledge graph and prepares them for Building Energy Modeling (BEM).

The project demonstrates how BIM data from IFC files can be converted into a graph database, enriched with intelligent relationships, and used as the foundation for energy analysis and future performance-driven design.

For GitHub projects, the best place is right after the "Overview" section and before the "Features" section. This allows visitors to immediately see what your project looks like.

Here's the structure I recommend:

# 🏗️ DM-BIM-BEM Pipeline

## 📌 Overview

(Project description...)

---

# 📸 Screenshots

### 1. Dashboard
![Dashboard](<screenshots/dashboard.png>)

### 2. neoj_graph
[neoj_graph](<screenshots/neoj_graph.png>)

### 3. output
[output](<screenshots/output.png>)


---

## 🚀 Features

- ✅ IFC model parsing using IfcOpenShell
- ✅ Automatic extraction of Spaces and Walls
- ✅ Graph database integration using Neo4j
- ✅ Semantic relationships between building elements
- ✅ Space adjacency detection
- ✅ Thermal zone generation
- ✅ Interactive graph visualization
- ✅ Modular and scalable architecture
- 🔄 OpenStudio & EnergyPlus integration (In Progress)
- 🔄 Performance feedback loop (Planned)

---

## 🏗️ System Architecture

```
                 Revit / IFC
                      │
                      ▼
            IFC Parser (IfcOpenShell)
                      │
                      ▼
          Building Data Extraction
                      │
                      ▼
           Graph Construction Layer
                  (Neo4j)
                      │
      ┌───────────────┴───────────────┐
      │                               │
      ▼                               ▼
Graph Intelligence            Relationship Builder
      │                               │
      └───────────────┬───────────────┘
                      ▼
              Thermal Zone Creation
                      │
                      ▼
      OpenStudio / EnergyPlus (Upcoming)
                      │
                      ▼
          Building Performance Results
```

---

# 📂 Project Structure

```
dm-bim-bem-pipeline/
│
├── data/
│   ├── sample.ifc
│   └── outputs/
│
├── src/
│   ├── ingestion/
│   │     └── ifc_parser.py
│   │
│   ├── graph/
│   │     └── neo4j_loader.py
│   │
│   ├── visualization/
│   │     └── graph_view.py
│   │
│   ├── utils/
│   │     └── spatial.py
│   │
│   ├── bem/
│   │
│   ├── api/
│   │
│   └── main.py
│
├── dashboard.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Technologies Used

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| BIM Parser | IfcOpenShell |
| Graph Database | Neo4j |
| Graph Queries | Cypher |
| Visualization | PyVis, Streamlit |
| Data Processing | Pandas |
| Future BEM | OpenStudio |
| Future Simulation | EnergyPlus |

---

# 📊 Current Workflow

```
IFC File
   │
   ▼
Parse Building Elements
   │
   ▼
Extract Spaces & Walls
   │
   ▼
Store in Neo4j Graph
   │
   ▼
Generate Relationships
   │
   ▼
Infer Space Adjacency
   │
   ▼
Create Thermal Zones
   │
   ▼
Visualize Building Graph
```

---

# 🧠 Graph Schema

## Nodes

- Space
- Wall
- ThermalZone

## Relationships

- `BOUNDED_BY`
- `ADJACENT_TO`
- `PART_OF`

Example:

```
Living Room
     │
BOUNDED_BY
     │
Outer Wall

Living Room
     │
ADJACENT_TO
     │
Entry Hall

Living Room
     │
PART_OF
     │
Zone_1
```

---

# 🖥️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/dm-bim-bem-pipeline.git
```

Move into the project directory

```bash
cd dm-bim-bem-pipeline
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Run the pipeline

```bash
python -m src.main
```

Generate graph visualization

```bash
python -m src.visualization.graph_view
```

Launch the Streamlit dashboard

```bash
streamlit run dashboard.py
```

---

# 📷 Output

The pipeline generates:

- Parsed IFC model
- Semantic building graph
- Space adjacency graph
- Thermal zone relationships
- Interactive visualization dashboard

---

# 🎯 Future Improvements

- Automatic OpenStudio model generation
- EnergyPlus simulation integration
- Rule-based building validation
- Graph Neural Network (GNN) support
- AI-driven energy optimization
- Multi-building analysis
- REST API
- Cloud deployment
- BIM design recommendation engine

---

# 📚 Applications

- Smart Buildings
- Sustainable Design
- Digital Twins
- Building Energy Analysis
- BIM Automation
- Facility Management
- AEC Research
- Building Performance Optimization

---

# 👩‍💻 Author

**Ranjita Dandgulkar**

Engineering Student | IoT & AI Enthusiast

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.