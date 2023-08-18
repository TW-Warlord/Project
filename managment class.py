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