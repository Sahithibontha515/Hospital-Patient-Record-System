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

    def __lt__(self, other):
        # Lower enum value = higher severity
        return (self.priority.value, self.admission_time) < (other.priority.value, other.admission_time)

    def __repr__(self):
        return f"{self.name} (Priority: {self.priority.name}, ID: {self.patient_id})"
    

# Patient Priority
class PatientPriority(Enum):
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4

# Patient Condition
class ConditionType(Enum):
    CARDIAC = "Cardiac Emergency"
    RESPIRATORY = "Respiratory Issue"
    FRACTURE = "Bone Fracture"
    TRAUMA = "Physical Trauma"
    FEVER = "High Fever"
    BURN = "Burn Injury"
    ALLERGIC_REACTION = "Allergic Reaction"
    OTHER = "Other"


    
