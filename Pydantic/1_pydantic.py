from pydantic import BaseModel , EmailStr,AnyUrl,Field
from typing import List, Dict , Optional,Annotated

# AnyUrl is used to validate URLs, but it is not used in this example any kind of url is allowed if it is in correct format
class Patient(BaseModel):
	name: Annotated[str , Field(max_length=50 , description='Give name of patient in less then 50 characters ', examples=['John Doe', 'Jane Smith'])]
# this validates that name is a string with a maximum length of 50 characters
	email:EmailStr # this validates that email is a valid email address used for data validation
	age: int= Field(gt=0, lt=120)# Field can also be used to validate a range of values, here age must be greater than 0 and less than 120
	weight: float=Field(gt=0, description="Weight must be greater than 0") # this validates that weight is a float greater than 0 , for this Field is used as a validator
	married: Annotated[bool, Field(default=None,description="Is the patient married?")] # this validates that married is a boolean value
	allergies: Optional[List[str]] # this validates that allergies is a list of strings
	contact_details: Dict[str,str] # this validates that contact_details is a dictionary with string keys and values

def insert_patient_data(patient: Patient):
    
	print(patient.name)
	print(patient.age)
	print(patient.weight)
	print("updated")



patient_info={'name': 'John Doe','email':'Abc@gmail.com','age': 30,'weight': 70.5 , 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'Phone':'154785762'} }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
