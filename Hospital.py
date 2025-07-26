import heapq

class HospitalSystem:
    """ Manages patient admissions, treatment, and records using a priority queue and hash map. """
    def __init__(self):
        self.queue = []
        self.records = {}

    def admit_patient(self, patient):
        """ Admit a new patient to the hospital. """ 
        if patient.patient_id in self.records:
            return
        heapq.heappush(self.queue, patient)
        self.records[patient.patient_id] = patient
        print(f"[Admitted] {patient}")

    def get_patient_with_max_severity(self):
        """ Removes and returns the patient with the highest severity. """
        if not self.queue:
            print("[Info] No patients in the queue.")
            return None
        patient = heapq.heappop(self.queue)
        self.records.pop(patient.patient_id, None)
        print(f"[Treated] {patient}")
        return patient

    def show_patient_with_max_severity(self):
        """ Returns the patient with the highest severity without removing them """
        if not self.queue:
            print("[Info] No patients in the queue.")
            return None
        return self.queue[0]
