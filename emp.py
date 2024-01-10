'''

@Author: Rohan Vetale

@Date: 2023-01-05 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-10 16:00:30

@Title : Employee wage with Use Cases


'''
import random
import logging

logging.basicConfig(filename='employee_log.log', level=logging.DEBUG, format='%(asctime)s %(message)s',
                    datefmt='%m:%d:%y %I:%M:%S %p')
logger = logging.getLogger(__name__)

class Worker:
    def __init__(self, worker_name, wage_per_hour, max_working_day, max_working_hours):
        self.wage_per_hrs = wage_per_hour
        self.max_working_days = max_working_day
        self.max_working_hrs = max_working_hours
        self.worker_name = worker_name
        self.total_wage = 0

    def worker_wage_implementation(self):
        emp_working_hrs = 0
        emp_working_days = 0
        while emp_working_hrs < self.max_working_hrs and emp_working_days < self.max_working_days:
            emp_type = random.randint(0, 2)
            working_hours = 0
            match emp_type:
                case 0:
                    working_hours = 0
                case 1:
                    working_hours = 4
                case 2:
                    working_hours = 8
            emp_working_hrs += working_hours
            self.total_wage += working_hours * self.wage_per_hrs
            emp_working_days += 1

class Organization:
    def __init__(self, org_name):
        self.org_name = org_name
        self.worker_dict = {}

    def add_worker(self, worker_obj: Worker):
        self.worker_dict.update({worker_obj.worker_name: worker_obj})

    def worker_details(self):
        for worker_name, worker_data in self.worker_dict.items():
            logger.info(f"Worker Name: {worker_name} Worker Data: {worker_data.total_wage}")

class MultiOrganization:
    def __init__(self):
        self.org_dict = {}

    def add_organization(self, org_obj):
        self.org_dict.update({org_obj.org_name: org_obj})
        logger.info(f"{org_obj.org_name} is Added!!")

    def all_org_details(self):
        for key, org_data in self.org_dict.items():
            logger.info(f"Organization Name: {key} Organization Data: {org_data.worker_dict}")

    def get_organization(self, org_name):
        return self.org_dict.get(org_name)

    def remove_organization(self, org_name):
        if org_name in self.org_dict:
            self.org_dict.pop(org_name)
            logger.info(f"{org_name} is deleted.")
        else:
            logger.info("Organization not Found")

    def get_organization_with_all_worker(self, org_name):
        org_obj: Organization = self.org_dict.get(org_name)
        if org_obj:
            logger.info(f"{org_obj.org_name} and total workers in organization {len(org_obj.worker_dict)}")
            org_obj.worker_details()
        else:
            logger.info("organization is not present!!")

def main():
    multi_org_obj = MultiOrganization()
    try:
        while True:
            print(
                "choice 1 for add worker\nchoice 2 for all details of worker\nchoice 3 to get an item from dictionary\n"
                "choice 4 for update an item of dictionary\nchoice 5 for delete an item of dictionary\nchoice 6 for all "
                "organization details\nchoice 7 to get organization\nchoice 8 for delete organization\nchoice 9 to get all worker "
                "details in a organization\nchoice 10 to exit")
            user_choice = int(input("Enter your choice: "))
            match user_choice:
                case 1:
                    org_name = input("Enter your organization name: ")
                    org_obj = multi_org_obj.get_organization(org_name)
                    if org_obj is None:
                        org_obj = Organization(org_name)
                    worker_name = input("Enter the worker name: ")
                    wage_per_hour = int(input("Enter wage per Hours: "))
                    max_working_days = int(input("Enter Max working Days: "))
                    max_working_hours = int(input("Enter Max working Hours: "))
                    worker_obj = Worker(worker_name, wage_per_hour, max_working_days, max_working_hours)
                    worker_obj.worker_wage_implementation()
                    org_obj.add_worker(worker_obj)
                    multi_org_obj.add_organization(org_obj)
                case 2:
                    org_name = input("Enter your organization name: ")
                    org_obj = multi_org_obj.get_organization(org_name)
                    if org_obj is None:
                        pass
                    org_obj.worker_details()
                case 3:
                    worker_name = input("Enter the worker name: ")
                    org_name = input("Enter your organization name: ")
                    org_obj = multi_org_obj.get_organization(org_name)
                    if org_obj is None:
                        pass
                    org_obj.get_worker(worker_name)
                case 4:
                    worker_name = input("Enter the worker name: ")
                    org_name = input("Enter your organization name: ")
                    org_obj = multi_org_obj.get_organization(org_name)
                    if org_obj is None:
                        logger.info('Organization not found!!')
                    org_obj.update_worker(worker_name)
                case 5:
                    worker_name = input("Enter the worker name: ")
                    org_name = input("Enter your organization name: ")
                    org_obj = multi_org_obj.get_organization(org_name)
                    if org_obj is None:
                        pass
                    org_obj.delete_worker(worker_name)
                case 6:
                    multi_org_obj.all_org_details()
                case 7:
                    org_name = input("Enter organization name: ")
                    multi_org_obj.get_organization(org_name)
                case 8:
                    org_name = input("Enter organization name: ")
                    multi_org_obj.remove_organization(org_name)
                case 9:
                    org_name = input("Enter your organization name: ")
                    org_obj = multi_org_obj.get_organization(org_name)
                    if org_obj is None:
                        pass
                    multi_org_obj.get_organization_with_all_worker(org_obj.org_name)
                case 10:
                    break
    except Exception as e:
        logger.exception(e)

if __name__ == '__main__':
    main()
