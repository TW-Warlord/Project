
class Doctor:
    def __init__(self, doctor_id="", name="", specialization="", working_time="", qualification="", room_number=""):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def get_doctor_id(self): 
        return self.doctor_id
    
    def get_name(self):
        return self.name
    
    def get_specialization(self):
        return self.specialization
    
    def get_working_time(self):
        return self.working_time
    
    def get_qualification(self):
        return self.qualification
    
    def get_room_number(self):
        return self.room_number
    
    def set_doctor_id(self, new_id):
        self.doctor_id = new_id

    def set_name(self, new_name):
        self.name = new_name

    def set_specialization(self, new_specialization):
        self.specialization = new_specialization

    def set_working_time(self, new_working_time):
        self.working_time = new_working_time

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    def set_room_number(self, new_room_number):
        self.room_number = new_room_number

    def __str__(self):
        return self.doctor_id + "_" + self.name + "_" + self.specialization + "_" + self.working_time + "_" + self.qualification + "_" + self.room_number
    
class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()
    
    def format_dr_info(self, doctor):
        return doctor.__str__()
    
    def enter_dr_info(self):
        id = input("\nEnter the doctor's ID: ")
        name = input("Enter the doctor's name: ")
        speciality = input("Enter the doctor's speciality: ")
        timing = input("Enter the doctor's timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor's qualification: ")
        room_number = input("Enter the doctor's room number: ")
        return Doctor(id, name, speciality, timing, qualification, room_number)
    
    def read_doctors_file(self):
        file = open("doctors.txt")
        file.readline()
        row = file.readline() 
        while(row != ""):
            split = row.split("_")
            doctor = Doctor(split[0],split[1],split[2],split[3],split[4],split[5].strip())
            self.doctors.append(doctor)
            row = file.readline()
        file.close
    
    def search_doctor_by_id(self):
        id = input("\nEnter the doctor Id: ")
        for doctor in self.doctors:
            if doctor.get_doctor_id() == id:
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor with the same ID on the system")

    def search_doctor_by_name(self):
        name = input("\nEnter the doctor name: ")
        for doctor in self.doctors:
            if doctor.get_name() == name:
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor with the same name on the system")

    def display_doctor_info(self, doctor):
        format_string = "{:<5} {:<15} {:<15} {:<15} {:<15} {:<15}"
        print(format_string.format("\n"'Id','Name', 'Speciality', 'Timing', 'Qualification', 'Room Number'), '\n')
        print(format_string.format(doctor.get_doctor_id(), doctor.get_name(), doctor.get_specialization(), doctor.get_working_time(), doctor.get_qualification(), doctor.get_room_number()))

    def edit_doctor_info(self):
        id = input("\nPlease enter the id of the doctor that you want to edit their information: ")
        for doctor in self.doctors:
            if doctor.get_doctor_id() == id:
                doctor.set_name(input("Enter New name: "))
                doctor.set_specialization(input("Enter New speciality in : "))
                doctor.set_working_time(input("Enter new timing: "))
                doctor.set_qualification(input("Enter new qualification: "))
                doctor.set_room_number(input("Enter new room number: "))
                self.write_list_of_doctors_to_file()
                print("\nDoctor whose ID", id, "has been edited")
                return
        print("Can't find the doctor with the same ID on the system")

    def display_doctors_list(self):
        format_string = "{:<5} {:<15} {:<15} {:<15} {:<15} {:<15}"
        print(format_string.format('Id','Name', 'Speciality', 'Timing', 'Qualification', 'Room Number'))
        for doctor in self.doctors:
            print("")
            print(format_string.format(doctor.get_doctor_id(), doctor.get_name(), doctor.get_specialization(), doctor.get_working_time(), doctor.get_qualification(), doctor.get_room_number()))

    def write_list_of_doctors_to_file(self):
        file = open("doctors.txt", "w")
        file.write("id_name_specialist_timing_qualification_roomNb\n")
        # write information for each doctor
        for doctor in self.doctors:
            file.write(self.format_dr_info(doctor)+'\n')
        file.close

    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        self.write_list_of_doctors_to_file()
        print("\nDoctor whose ID is", new_doctor.get_doctor_id(), "has been added")
           
class Patient:
    def __init__(self, id="", name="", disease="", gender="", age=""):
        self.id = id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def get_id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_disease(self):
        return self.disease

    def set_disease(self, new_disease):
        self.disease = new_disease

    def get_gender(self):
        return self.gender

    def set_gender(self, new_gender):
        self.gender = new_gender

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f"{self.id}_{self.name}_{self.disease}_{self.gender}_{self.age}"

class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    def format_patient_Info_for_file(self,patients):
        return patients.__str__()

    def enter_patient_info(self):
        id = input("\nEnter patient Id: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        gender = input("Enter patient gender: ")
        age = input("Enter patient age: ")
        
        patient_obj = Patient(id, name, disease, gender, age)
        return patient_obj
    
    def read_patients_file(self):
        with open("patients.txt", "r") as file:
            file.readline()
            for line in file:
                patient_data = line.strip().split("_")
                if len(patient_data) == 5:
                    patient_data = Patient(patient_data[0], patient_data[1], patient_data[2], patient_data[3], patient_data[4])
                    self.patients.append(patient_data)
    
    def search_patient_by_Id(self):
        patient_id = input("\nEnter the Patient Id: ")
        for patient_data in self.patients:
             if patient_data.get_id() == patient_id:
                 self.display_patient_info(patient_data)
                 return 

        print("Can't find the Patient with the same id on the system")

    def display_patient_info(self, patient_data):

        format_string = "{:<5} {:<20} {:<15} {:<15} {:<15}"
        print(format_string.format("\n"'Id','Name', 'Disease', 'Gender', 'Age'), '\n')
        print(format_string.format(patient_data.get_id(), patient_data.get_name(), patient_data.get_disease(), patient_data.get_gender(), patient_data.get_age()))
        
    def edit_patient_info_by_id(self):
        target_id = input("\nPlease enter the id of the Patient that you want to edit their information: ")
        for patient in self.patients:
            if patient.get_id() ==target_id:

                patient.set_name(input("Enter new Name: "))
                patient.set_disease(input("Enter new patient disease: "))
                patient.set_gender(input("Enter new patient gender: "))
                patient.set_age(input("Enter new patient age: "))

                self.write_list_of_patients_to_file()

                print("\nPatient whose ID is", target_id ,"has been edited.")
                return
        print("Cannot find the patient with the given ID.")

    def display_patient_list(self):
        format_string = "{:<5} {:<20} {:<15} {:<15} {:<15}"

        print(format_string.format("\n"'Id','Name', 'Disease', 'Gender', 'Age'))
        for patient in self.patients:
            print()        
            print(format_string.format(patient.get_id(), patient.get_name(), patient.get_disease(), patient.get_gender(), patient.get_age()))

    def write_list_of_patients_to_file(self):
        with open('patients.txt', 'w') as file:
            file.write("id_Name_Disease_Gender_Age\n")
            for patient in self.patients:
                file.write(self.format_patient_Info_for_file(patient)+"\n")
        
    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        print("Adding new patient to the list:", new_patient)
        
        self.write_list_of_patients_to_file()
        print("\nPatient whose ID is", new_patient.get_id(), "has been added")
        return

class Management:
    def display_menu(self):

        while True:
            main_menu = (input("\nWelcome to Alberta Hospital (AH) Management System\nSelect from the following options, or select 0 to stop:\n1 - Doctors\n2 - Patients\n3 - Exit Program\n>>> "))


            if main_menu == "1":
                doctor_options = ["1","2","3","4","5","6"]

                while True:

                    doctor_menu = (input("\nDoctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n>>> "))


                    if doctor_menu == "1":
                        show_doctor_list = DoctorManager()
                        show_doctor_list.display_doctors_list()

                    elif doctor_menu == "2":
                        doctor_by_id = DoctorManager()
                        doctor_by_id.search_doctor_by_id()

                    elif doctor_menu == "3":
                        doctor_by_name = DoctorManager()
                        doctor_by_name.search_doctor_by_name()

                    elif doctor_menu == "4":
                        doctor_add_new = DoctorManager()
                        doctor_add_new.add_dr_to_file()

                    elif doctor_menu == "5":
                        doctor_edit = DoctorManager()
                        doctor_edit.edit_doctor_info()

                    elif doctor_menu == "6":
                        break

                    else:
                        print("\nInvalid input, please indicate a correct integer\n")
                        continue


            elif main_menu == "2":

                patient_options = ["1","2","3","4","5"]

                while True:

                    patient_menu = (input("\nPatients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n>>> "))

                    if patient_menu not in patient_options:
                        print("\nInvalid input, please indicate a correct integer\n")
                        patient_menu = (input("1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu"))

                    else:

                        if patient_menu == "1":
                            show_patient_list = PatientManager()
                            show_patient_list.display_patient_list()

                        elif patient_menu == "5":
                            break


            elif main_menu == "3":
                print("Thanks for using the program. Bye!")
                break


            else:
                print("\nInvalid input, please indicate a correct integer\n")


if __name__ == "__main__":
    menu = Management()
    menu.display_menu()
            
