class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    def format_patient_Info_for_file(self, patients):
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
                    patient_data = Patient(patient_data[0], patient_data[1], patient_data[2], patient_data[3],
                                           patient_data[4])
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
        print(format_string.format("\n"'Id', 'Name', 'Disease', 'Gender', 'Age'), '\n')
        print(format_string.format(patient_data.get_id(), patient_data.get_name(), patient_data.get_disease(),
                                   patient_data.get_gender(), patient_data.get_age()))

    def edit_patient_info_by_id(self):
        target_id = input("\nPlease enter the id of the Patient that you want to edit their information: ")
        for patient in self.patients:
            if patient.get_id() == target_id:
                patient.set_name(input("Enter new Name: "))
                patient.set_disease(input("Enter new patient disease: "))
                patient.set_gender(input("Enter new patient gender: "))
                patient.set_age(input("Enter new patient age: "))

                self.write_list_of_patients_to_file()

                print("\nPatient whose ID is", target_id, "has been edited.")
                return
        print("Cannot find the patient with the given ID.")

    def display_patient_list(self):
        format_string = "{:<5} {:<20} {:<15} {:<15} {:<15}"

        print(format_string.format("\n"'Id', 'Name', 'Disease', 'Gender', 'Age'))
        for patient in self.patients:
            print()
            print(
                format_string.format(patient.get_id(), patient.get_name(), patient.get_disease(), patient.get_gender(),
                                     patient.get_age()))

    def write_list_of_patients_to_file(self):
        with open('patients.txt', 'w') as file:
            file.write("id_Name_Disease_Gender_Age\n")
            for patient in self.patients:
                file.write(self.format_patient_Info_for_file(patient) + "\n")

    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        print("Adding new patient to the list:", new_patient)

        self.write_list_of_patients_to_file()
        print("\nPatient whose ID is", new_patient.get_id(), "has been added")
        return


def main():
    welcome_value = [1, 2, 3]

    while True:
        user_welcome_input = int(input(
            "\nWelcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop:\n1 - Doctors\n2 - Patients\n3 - Exit Program\n>>> "))

        if user_welcome_input not in welcome_value:
            print("\nInvalid input, please indicate a correct integer\n")
        else:

            if user_welcome_input == 1:
                doctor_set_menu = [1, 2, 3, 4, 5, 6]
                while True:
                    doctor_initial_menu = int(input(
                        "\nDoctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n>>> "))
                    if doctor_initial_menu not in doctor_set_menu:
                        print("\nInvalid input, please indicate a correct integer\n")
                        doctor_initial_menu = int(input(
                            "\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n>>> "))
                    else:
                        if doctor_initial_menu == 1:
                            show_doctor_list = DoctorManager()
                            show_doctor_list.display_doctors_list()

                        elif doctor_initial_menu == 2:
                            doctor_by_id = DoctorManager()
                            doctor_by_id.search_doctor_by_id()

                        elif doctor_initial_menu == 3:
                            doctor_by_name = DoctorManager()
                            doctor_by_name.search_doctor_by_name()

                        elif doctor_initial_menu == 4:
                            doctor_add_new = DoctorManager()
                            doctor_add_new.add_dr_to_file()

                        elif doctor_initial_menu == 5:
                            doctor_edit = DoctorManager()
                            doctor_edit.edit_doctor_info()

                        elif doctor_initial_menu == 6:
                            break

            elif user_welcome_input == 2:

                patient_initial_input = [1, 2, 3, 4, 5]
                while True:
                    patient_details_input = int(input(
                        "\nPatients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n>>> "))
                    if patient_details_input not in patient_initial_input:
                        print("\nInvalid input, please indicate a correct integer\n")
                        patient_details_input = int(input(
                            "1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu"))
                    else:
                        if patient_details_input == 1:
                            show_patient_list = PatientManager()
                            show_patient_list.display_patient_list()

                        elif patient_details_input == 2:
                            patient_by_id = PatientManager()
                            patient_by_id.search_patient_by_Id()

                        elif patient_details_input == 3:
                            patient_add_new = PatientManager()
                            patient_add_new.add_patient_to_file()

                        elif patient_details_input == 4:
                            patient_edit = PatientManager()
                            patient_edit.edit_patient_info_by_id()

                        elif patient_details_input == 5:
                            break

            elif user_welcome_input == 3:
                print("Thanks for using the program. Bye!")
                break
