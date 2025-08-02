import heapq
import csv
from datetime import timedelta, datetime
class HospitalSystem:
    """ Manages patient admissions, treatment, and records using a priority queue and hash map. """
    
    def __init__(self):
        self.queue = []
        self.records = {}
        self.index_map = {}  # Optional: for advanced operations like updates

    def admit_patient(self, patient):
        if patient.patient_id in self.records:
            print(f"[Duplicate] Patient ID {patient.patient_id} already exists.")
            return
        heapq.heappush(self.queue, patient)
        self.records[patient.patient_id] = patient
        self.index_map[patient.patient_id] = len(self.queue) - 1  # index mapping
        #print(f"[Admitted] {patient}")

        if len(self.queue) > 50:
            self.cleanup_heap()

    def discharge_patient(self, patient_id):
        if patient_id in self.records:
            patient_to_remove = self.records[patient_id]
            patient_to_remove.discharged = True  # Lazy deletion
            del self.records[patient_id]
            print(f"[Discharged] {patient_to_remove}")
        else:
            print(f"[Not Found] No patient with ID {patient_id} to discharge.")

    def get_patient_with_max_severity(self):
        while self.queue:
            patient = heapq.heappop(self.queue)
            if not patient.discharged:
                self.records.pop(patient.patient_id, None)
                #print(f"[Treated] {patient}")
                return patient
        print("[Info] No active patients in the queue.")
        return None

    def show_patient_with_max_severity(self):
        while self.queue:
            top = self.queue[0]
            if top.discharged:
                heapq.heappop(self.queue)
            else:
                print(f"[Next to Treat] {top}")
                return top
        print("[Info] No active patients in the queue.")
        return None

    def show_all_patients(self):
        """ Show all patients currently in the queue (excluding discharged ones). """
        return [p for p in self.queue if not p.discharged]

    def find_patient(self, patient_id):
        patient = self.records.get(patient_id)
        if patient:
            print(f"[Found] {patient}")
            return patient
        else:
            print(f"[Not Found] No patient with ID: {patient_id}")
            return None

    def cleanup_heap(self):
        """ Remove discharged patients and re-heapify the queue. """
        self.queue = [p for p in self.queue if not p.discharged]
        heapq.heapify(self.queue)
        #print("[Cleanup] Discharged patients removed from heap.")


    def archive_old_patients(self, days=7, filename="archived_patients.csv"):
        cutoff = datetime.now() - timedelta(days=days)
        
        # Filter out old patients
        old_patients = [p for p in self.queue if p.admission_time < cutoff]
        
        if not old_patients:
            print("[Archive] No patients found for archiving.")
            return

        # Write to CSV
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Patient ID", "Name", "Age", "Priority", "Condition", "Admission Time"])
            
            for p in old_patients:
                writer.writerow([
                    p.patient_id,
                    p.name,
                    p.age,
                    p.priority.name,
                    p.condition,
                    p.admission_time.strftime("%Y-%m-%d %H:%M:%S")
                ])

        # Remove from queue and records
        self.queue = [p for p in self.queue if p.admission_time >= cutoff]
        for p in old_patients:
            self.records.pop(p.patient_id, None)

        # Re-heapify the queue
        heapq.heapify(self.queue)

        print(f"[Archive] Archived {len(old_patients)} patients to '{filename}' and removed them from memory.")


