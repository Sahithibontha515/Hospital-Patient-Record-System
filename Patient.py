from datetime import datetime
from enum import Enum

# Patient Class
class Patient:
    def __init__(self, patient_id, name, age, priority, condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.priority = priority
        self.condition = condition
        self.admission_time = datetime.now()
        self.discharged = False  # Mark discharged patients

    def __lt__(self, other):
        # Lower enum value = higher severity
        return (self.priority.value, self.admission_time) < (other.priority.value, other.admission_time)

    def __repr__(self):
        return f"{self.name} (Priority: {self.priority.name}, ID: {self.patient_id}), Condition: {self.condition}"
    



    
