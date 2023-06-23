welcome_prompt = "Welcome doctor! What would you like to do today?\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"
error_message = "Invalid input! Could not save data due to invalid entry."
name_prompt = "What is the patient's name?\n"
appearance_prompt = "How is the patient's general appearance?\n - 1. Normal apperance\n - 2. Irritable or lethargic\n"
eye_prompt = "How are the patient's eyes?\n 1. Eyes normal or slightly sunken\n 2. Eyes are very sunken.\n"
skin_prompt = "How is the patient's skin when pinched?\n 1. Normal skin pinch\n 2. Slow skin pinch\n"

severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"

# Initial list of patients and diagnoses
patients_and_diagnoses = [
  "Mike - Severe dehydration",
  "Sarah - Some dehydration",
  "Katie - No dehydration"
]

# Prints out the list of patients and their diagnoses
def list_patients():
  for patient in patients_and_diagnoses:
    print(patient)

# Saves a new patient and diagnosis to the list
def save_new_diagnosis(name, diagnosis):
  # Checks to see if name or diagnosis are empty strings
  if name == "" or diagnosis == "":
    # If any of them are, we simply retrun an error message and do not add the patient to the list
    print(error_message)
    return
  final_diagnosis = name + " - " + diagnosis
  patients_and_diagnoses.append(final_diagnosis)
  print("Final diagnosis:", final_diagnosis, "\n")

# Diagnose appearance
def assess_appearance():
  appearance = input(appearance_prompt)
  if appearance == "1":
      eyes = input(eye_prompt)
      return assess_eyes(eyes)
  elif appearance == "2":
      skin = input(skin_prompt)
      return assess_skin(skin)
  else:
    # Returns an empty string if user input is neither 1 nor 2
    return ""

def assess_skin(skin):
  if skin == "1":
      return some_dehydration
  elif skin == "2":
      return severe_dehydration
  else:
    return ""

def assess_eyes(eyes):
  if eyes == "1":
      return no_dehydration
  elif eyes == "2":
      return severe_dehydration
  else:
    return ""


def start_new_diagnosis():
  name = input(name_prompt)
  diagnosis = assess_appearance()
  save_new_diagnosis(name, diagnosis)
  


def main():
  while(True):
    selection = input(welcome_prompt)
    if selection == "1":
      list_patients()
    elif selection == "2":
      start_new_diagnosis()
    elif selection == "q":
        return


main()

# Assessing all if-then-else cases for both skin and eyes
#def test_assess_skin():
  #print(assess_skin("1") == some_dehydration)
  #print(assess_skin("2") == severe_dehydration)
  #print(assess_skin("") == "")

#def test_assess_eyes():
  #print(assess_eyes("1") == no_dehydration)
  #print(assess_eyes("2") == severe_dehydration)
  #print(assess_eyes("") == "")

#def test_assess_appearance():
 #print(assess_appearance())

# Assessing all possible cases of entries for name and diagnosis
#def test_save_new_diagnosis():
    #save_new_diagnosis("", "")
    #print(patients_and_diagnoses == [
        #"Mike - Severe dehydration",
        #"Sally - No dehydration",
        #"Kate - Some dehydration"
    #])
    #save_new_diagnosis("Nimish", "")
    #print(patients_and_diagnoses == [
        #"Mike - Severe dehydration",
        #"Sally - No dehydration",
        #"Kate - Some dehydration"
    #])
    #save_new_diagnosis("", "No dehydration")
    #print(patients_and_diagnoses == [
        #"Mike - Severe dehydration",
        #"Sally - No dehydration",
        #"Kate - Some dehydration"
    #])
    #save_new_diagnosis("Nimish", "Some dehydration")
    #print(patients_and_diagnoses == [
        #"Mike - Severe dehydration",
        #"Sally - No dehydration",
        #"Kate - Some dehydration",
        #"Nimish - Some dehydration"
    #])

#test_assess_skin()
#test_assess_eyes()
#test_save_new_diagnosis()