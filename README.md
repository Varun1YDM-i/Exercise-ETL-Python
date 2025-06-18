# 💪 Exercise ETL Project

A modular and maintainable ETL (Extract, Transform, Load) pipeline that fetches exercise data from the [ExerciseDB API](https://rapidapi.com/justin-WFnsXH_t6/api/exercisedb) and writes it to a CSV file, with complete logging and error handling.

---

## 🧱 Project Structure
```
exercise_etl/
├── README.md          # Documentation
├── logs/              # Log files
│   └── log.txt
├── output/            # CSV data output
│   └── exercise.csv
└── src/               # Source code modules
    ├── api_client.py  # Handles API requests
    ├── csv_writer.py  # Writes data to CSV
    ├── etl.py         # Orchestrates the ETL flow
    └── logger.py      # Manages logging
```
## 🧪 Sample Columns
**Sample CSV Columns:**a
- bodyPart
- equipment
- gifUrl
- id
- name
- target
- secondaryMuscles
- instructions
- description
- difficulty
- category

---

## 📦 Requirements
- Python 3.7+
- `requests` library

Install the required dependencies:
```bash
pip install requests
```

---

## 🚀 Getting Started
1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/exercise-etl.git
cd exercise-etl
```

2. **Run the ETL script:**
```bash
cd src
python etl.py
```

3. **Check the outputs:**
- CSV File: `../output/exercise.csv`
- Logs: `../logs/log.txt`

---

## 🛠 Features
- Object-Oriented Design
- Clean error handling for API & File I/O
- Step-by-step logging
- Easily extendable (e.g., DB load, API filters, CLI support)


