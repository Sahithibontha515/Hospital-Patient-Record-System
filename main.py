from Hospital import HospitalSystem
from Patient import Patient
from HRSEnums import PatientPriority , ConditionType

hospital = HospitalSystem()


p1 = Patient(101, "Bob", 45, PatientPriority.LOW, ConditionType.BURN)
p2 = Patient(102, "Clara", 27, PatientPriority.HIGH, ConditionType.ALLERGIC_REACTION)
p3 = Patient(103, "Alice", 30, PatientPriority.CRITICAL, ConditionType.CARDIAC)


hospital.admit_patient(p1)
hospital.admit_patient(p2)
hospital.admit_patient(p3)

print()
print("[Max Severity]:", hospital.show_patient_with_max_severity())
print()

print("Show all Patients:")
for patient in hospital.show_all_patients():
    print(patient)


print("Patient with id ",hospital.find_patient(101))