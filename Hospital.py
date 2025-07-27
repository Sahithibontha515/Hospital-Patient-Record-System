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
    
    def discharge_patient(self, patient_id):
        if patient_id in self.records:
            patient_to_remove = self.records[patient_id]
            # Remove from hash map
            del self.records[patient_id]

            # Remove from priority queue by rebuilding it
            self.queue = [patient for patient in self.queue if patient.patient_id != patient_id]
            heapq.heapify(self.queue)  # Re-heapify after removal

            print(f"[Discharged] {patient_to_remove}")
        else:
            print(f"[Not Found] No patient with ID {patient_id} to discharge.")

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
    
    def show_all_patients(self):
        """ Returns all patients in the queue """
        return self.queue
    
    def find_patient(self, patient_id):
        """
        Returns a specific patient's details using a hash map lookup.
        """
        patient = self.records.get(patient_id)
        if patient:
            print(f"[Found] {patient}")
            return patient
        else:
            print(f"[Not Found] No patient with ID: {patient_id}")
            return None
