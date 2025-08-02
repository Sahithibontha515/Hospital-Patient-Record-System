import csv
from Patient import Patient , PatientPriority
from Hospital import HospitalSystem

def load_patients_from_csv(filepath, hospital: HospitalSystem):
    with open(filepath, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            patient = Patient(
                int(row["patient_id"]),
                row["name"],
                int(row["age"]),
                PatientPriority[row["priority"].upper()],
                row["condition"]
            )
            hospital.admit_patient(patient)