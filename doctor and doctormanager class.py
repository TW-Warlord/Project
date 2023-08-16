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
        while (row != ""):
            split = row.split("_")
            doctor = Doctor(split[0], split[1], split[2], split[3], split[4], split[5].strip())
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
        print(format_string.format("\n"'Id', 'Name', 'Speciality', 'Timing', 'Qualification', 'Room Number'), '\n')
        print(format_string.format(doctor.get_doctor_id(), doctor.get_name(), doctor.get_specialization(),
                                   doctor.get_working_time(), doctor.get_qualification(), doctor.get_room_number()))

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
        print(format_string.format('Id', 'Name', 'Speciality', 'Timing', 'Qualification', 'Room Number'))
        for doctor in self.doctors:
            print("")
            print(format_string.format(doctor.get_doctor_id(), doctor.get_name(), doctor.get_specialization(),
                                       doctor.get_working_time(), doctor.get_qualification(), doctor.get_room_number()))

    def write_list_of_doctors_to_file(self):
        file = open("doctors.txt", "w")
        file.write("id_name_specialist_timing_qualification_roomNb\n")
        for doctor in self.doctors:
            file.write(self.format_dr_info(doctor) + '\n')
        file.close

    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        self.write_list_of_doctors_to_file()
        print("\nDoctor whose ID is", new_doctor.get_doctor_id(), "has been added")