from enum import Enum

'''This file contains all the enums/constants present in hospital record system'''

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