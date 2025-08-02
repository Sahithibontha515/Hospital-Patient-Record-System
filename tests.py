from Hospital import HospitalSystem
from Patient import Patient
from HRSEnums import PatientPriority , ConditionType
import time
import random
from datetime import datetime, timedelta

def test_correctness():
    hospital = HospitalSystem()
    
    # Add patients
    p1 = Patient(1, "Alice", 30, PatientPriority.CRITICAL, "Cardiac Arrest")
    p2 = Patient(2, "Bob", 45, PatientPriority.HIGH, "Fracture")
    p3 = Patient(3, "Clara", 27, PatientPriority.MEDIUM, "Fever")
    
    hospital.admit_patient(p1)
    hospital.admit_patient(p2)
    hospital.admit_patient(p3)

    # Show max severity (should be Alice)
    assert hospital.show_patient_with_max_severity().name == "Alice"

    # Treat highest severity (Alice)
    assert hospital.get_patient_with_max_severity().name == "Alice"

    # Find specific patient
    assert hospital.find_patient(2).name == "Bob"

    # Try discharging a non-existent patient
    hospital.discharge_patient(99)  # Should print "Not Found"

    # Discharge Bob
    hospital.discharge_patient(2)
    assert hospital.find_patient(2) is None

    print("[PASS] Correctness and edge cases passed.")

def stress_test(num_patients=10000):
    print(f"\n[Stress Test] Admitting {num_patients} patients...")
    hospital = HospitalSystem()
    start = time.time()
    
    for i in range(1, num_patients + 1):
        name = f"Patient-{i}"
        age = random.randint(1, 100)
        priority = random.choice(list(PatientPriority))
        condition = f"Condition-{random.randint(1, 20)}"
        
        patient = Patient(i, name, age, priority, condition)
        # Manually backdate some admissions
        patient.admission_time -= timedelta(days=random.randint(0, 10))
        
        hospital.admit_patient(patient)

    end = time.time()
    print(f"[Completed] Admitted {num_patients} patients in {end - start:.2f} seconds")

    # Archive patients older than 5 days
    hospital.archive_old_patients(days=5)

def scalability_benchmark():
    print("\n[Benchmark] Testing with increasing dataset sizes...")
    sizes = [1000, 5000, 10000, 20000]
    
    for size in sizes:
        hospital = HospitalSystem()
        patients = [
            Patient(i, f"P{i}", random.randint(1, 90),
                    random.choice(list(PatientPriority)),
                    f"Condition-{i % 10}")
            for i in range(size)
        ]
        
        start = time.time()
        for patient in patients:
            hospital.admit_patient(patient)
        admit_time = time.time() - start
        
        start = time.time()
        for _ in range(size // 10):
            hospital.get_patient_with_max_severity()
        treat_time = time.time() - start

        print(f"Size: {size} | Admit Time: {admit_time:.3f}s | Treat Time (10%): {treat_time:.3f}s")

if __name__ == "__main__":
    test_correctness()
    stress_test()
    scalability_benchmark()
