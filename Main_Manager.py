def main():
    welcome_value = [1, 2, 3]

    while True:
        user_welcome_input = int(input(
            "\nWelcome to Alberta Hospital (AH) Management system\nSelect from the following options, or select 0 to stop:\n1 - Doctors\n2 - Patients\n3 - Exit Program\n>>> "))

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
                            # show_doctor_list = DoctorManager()
                            # show_doctor_list.display_doctors_list()
                            DoctorManager().display_doctors_list()

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


main()
