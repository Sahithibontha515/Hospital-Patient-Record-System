# 🏥 Hospital Patient Record System

A Python-based application to manage hospital patient triage using data structures like Priority Queues and Hash Maps. This system ensures patients are treated based on severity and maintains efficient record lookup, discharge, and archival features.

---

## 📁 Project Structure

BatchProcess.py → Handles batch processing like archiving old patient records

Hospital.py → Core hospital system logic with priority queue and hash map

HRSEnums.py → Enum classes for patient priority levels and other constants

main.py → Entry point for interactive testing or running the app

Patient.py → Patient class with severity comparison logic and admission data

tests.py → Unit and performance tests including correctness, stress, and scalability


---

## 🔧 Features

- Admit patients with severity-based priority
- Treat patients based on triage index (CRITICAL > HIGH > MEDIUM > LOW)
- Discharge patients (lazy deletion supported)
- Show or treat highest severity patient
- Find specific patients using efficient hash map lookup
- Archive old patients to CSV
- Batch cleanup and heap maintenance
- Advanced testing and benchmarking for scalability

---

## 🧠 Data Structures Used

- **Priority Queue (Min-Heap)**: Efficient retrieval of highest-priority patients.
- **Hash Map (Dictionary)**: Fast lookup of patient records by ID.
- **Enums**: Structured representation of patient priority and condition.

---

## ▶️ How to Run

### 1. Run the main program
```bash
python run main.py
```

### 2. To run the tests for benchmark
```bash
python run tests.py
```

