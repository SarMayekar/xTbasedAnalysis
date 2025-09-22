# WSL xT Based Analysis (2018-2021)

A comprehensive analysis of Women's Super League (WSL) data using xT (Expected Threat) model to evaluate player and team performance through spatial threat modeling and decision efficiency metrics.

## 📊 Project Overview

This project implements a complete Expected Threat (xT) framework for analyzing FA Women's Super League data from 2018–2021 seasons. The analysis covers data acquisition, xT model construction, decision efficiency evaluation, game state integration, and comprehensive visualization.

### Key Features
- **xT Model**: Spatial threat quantification across 96 pitch zones  
- **Decision Efficiency**: Comparison of actual vs. optimal player decisions  
- **Game State Analysis**: Performance under winning/drawing/losing conditions  
- **Interactive Dashboards**: Team and player performance visualizations  
- **Pressure Performance**: Identification of player archetypes under match pressure  

## 📁 Project Structure
xTbasedAnalysis/<br>
├── data/<br>
│ ├── raw/ # Raw data files<br>
│ │ ├── wsl_events_all_part*.csv # Split event data (4 parts)<br>
│ │ ├── wsl_matches_all.csv # Match metadata<br>
│ │ └── job-16061275-result.jsonl # StatsBomb data<br>
│ └── processed/ # Processed and derived data<br>
│ ├── dashboard_*.csv # Summary dashboards<br>
│ ├── player_.csv # Player analysis data<br>
│ ├── team_.csv # Team analysis data<br>
│ └── transition_matrix.npy # xT model data<br>
├── notebooks/ # Analysis workflow<br>
│ ├── 1. Data Acquisition & Game State.ipynb<br>
│ ├── 2. xT Model Construction.ipynb<br>
│ ├── 3. Decision Making.ipynb<br>
│ ├── 4. Game State Integration.ipynb<br>
│ └── 5. Visualizations.ipynb<br>
├── reports/<br>
│ ├── figures/ # Static visualizations (PNG/PDF)<br>
│ ├── interactive/ # Interactive reports (HTML)<br>
│ ├── WSL project.pdf # Final report<br>
│ └── WSL.pbix # Power BI dashboard<br>
├── src/ # Utility scripts<br>
├── config/ # Configuration files<br>
├── requirements.txt # Python dependencies<br>
└── README.md # Project documentation<br>

## 🚀 Quick Start

### 1. Installation
git clone https://github.com/SarMayekar/xTbasedAnalysis.git<br>
cd xTbasedAnalysis<br>
pip install -r requirements.txt

### 2. Data Reconstruction (Optional)
If you need the complete dataset:<br>
python src/combine_data.py

### 3. Run Analysis
Execute notebooks in sequential order:
jupyter notebook notebooks/

**Notebook Sequence:**
- Data Acquisition & Game State – Data collection and preprocessing  
- xT Model Construction – Building the Expected Threat model  
- Decision Making – Player decision analysis  
- Game State Integration – Contextual analysis  
- Visualizations – Data visualization and insights  

## 📈 Key Findings

### Team Performance (2018–2021)
- **Most Efficient Team:** Yeovil Town LFC (0.37 xT efficiency)  
- **High Performers:** Aston Villa, Liverpool WFC, Bristol City WFC  
- **Strategic Profiles:** Identified front-runners, comeback specialists, and balanced teams  

### Player Archetypes
- **Consistent Stars (93.94%)**: Perform well in all game states (e.g., Lucy Bronze)  
- **Pressure Performers (3.03%)**: Excel when team is losing (e.g., Jessica Fishlock)  
- **Fair-weather Players**: Better performance when winning  
- **Struggling Players**: Lower performance across all states  

### Game State Insights
- **Winning**: Highest decision efficiency (teams manage leads effectively)  
- **Drawing**: Highest action volume (balanced tactical battles)  
- **Losing**: Lowest efficiency (struggle to create quality chances)  

## 🔧 Technical Implementation

### xT Model Parameters
- Pitch Grid: 12×8 zones (10m×10m each)  
- Discount Factor: γ = 0.95  
- Convergence: Tolerance 1e-6, Max 500 iterations  
- Data: 1,095,921 events from 326 matches  

### Decision Efficiency Metrics
- Cardinal Alternatives: Fixed-direction spatial options (±15m)  
- Realistic Alternatives: Teammate-based options (30m radius, ±5s)  
- Efficiency Ratio: Actual xT / Best alternative xT  

## 📊 Output Files

### Core Analysis
- `wsl_actions_with_xt_OPENPLAY.csv` – 473,805 actions with xT attribution  
- `wsl_actions_with_decision_efficiency_FULL.csv` – Decision metrics  
- `wsl_actions_with_gamestate_efficiency.csv` – Game state context  

### Summary Reports
- `player_decision_efficiency_summary.csv` – 408 player profiles  
- `team_decision_efficiency_summary.csv` – 14 team profiles  
- `team_gamestate_efficiency.csv` – Team performance by game state  

### Visualizations
- **Static**: Heatmaps, radar charts, pressure matrices  
- **Interactive**: Team/player comparison dashboards (HTML)  
- **Dashboard**: Power BI reports for comprehensive analysis  

## 🛠️ Dependencies
See `requirements.txt` for full list. Key packages:  
- Core: pandas, numpy, matplotlib, seaborn  
- Data: statsbombpy, scikit-learn  
- Visualization: plotly, networkx  
- Analysis: scipy, tqdm  

## 📚 Methodology

### Phase 1: Data Acquisition
- StatsBomb API integration for WSL data (2018–2021)  
- Game state annotation (winning/drawing/losing)  
- 1,095,921 events from 326 matches  

### Phase 2: xT Model
- Spatial discretization (96-zone grid)  
- Shot probability estimation with Laplace smoothing  
- Transition matrix construction and value iteration  
- Action-level xT attribution  

### Phase 3: Decision Making
- Cardinal and realistic alternative generation  
- Efficiency delta and ratio calculations  
- Player and team aggregation  

### Phase 4: Game State Integration
- Merge decision efficiency with match context  
- Pressure performance metrics  
- Situational analysis  

### Phase 5: Visualization
- Static and interactive visualizations  
- Performance archetype identification  
- Dashboard preparation  

## 👥 Contributors
- **Sarthak Mayekar** – Project lead and analysis implementation  

## 📄 License
This project is for academic and research purposes. Data sourced from StatsBomb.  

## 🤝 Acknowledgments
- StatsBomb for providing comprehensive football data  
- Women's Super League for competition data  
- Open-source Python community for analytical tools  

*Note: The main event dataset (`wsl_events_all.csv`) is split into 4 parts for GitHub compatibility. Use `src/combine_data.py` to reconstruct the complete dataset if needed.*  
