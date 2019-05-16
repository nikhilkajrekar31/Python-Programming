# The Employee class holds employee information.

class Employee:
    # The __init__ method initializes the attributes.
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    # The set_name method sets the name attribute.
    def set_name(self, name):
        self.__name = name

    # The set_id_number method sets the id_number attribute.
    def set_id_number(self, id_number):
        self.__id_number = id_number

    # The set_department method sets the department attribute.
    def set_department(self, department):
        self.__department = department

    # The set_job_title method sets the job_title attribute.
    def set_job_title(self, job_title):
        self.__job_title = job_title

    # The get_name method returns the name attribute.
    def get_name(self):
        return self.__name

    # The get_id_number method returns the id_number attribute.
    def get_id_number(self):
        return self.__id_number

    # The get_department method returns the department attribute.
    def get_department(self):
        return self.__department

    # The get_job_title method returns the job_title attribute.
    def get_job_title(self):
        return self.__job_title

    # The __str__ method returns the object's state
    # as a string.
    def __str__(self):
        return "Name: " + self.__name + \
               "\nID Number: " + self.__id_number + \
               "\nDepartment: " + self.__department + \
               "\nJob Title: " + self.__job_title
