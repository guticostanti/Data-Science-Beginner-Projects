import csv
from decimal import Decimal

# lists of data
ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges = [], [], [], [], [], [], []

# Organizing csv data into python lists
def organize_data_in_lists(lst, csvFile, column_name):
    with open(csvFile) as csv_file:
        csv_dict = csv.DictReader(csv_file)
        for row in csv_dict:
            lst.append(row[column_name])
        return lst

organize_data_in_lists(ages, 'insurance.csv', 'age')
organize_data_in_lists(sexes, 'insurance.csv', 'sex')
organize_data_in_lists(bmis, 'insurance.csv', 'bmi')
organize_data_in_lists(num_children, 'insurance.csv', 'children')
organize_data_in_lists(smoker_statuses, 'insurance.csv', 'smoker')
organize_data_in_lists(regions, 'insurance.csv', 'region')
organize_data_in_lists(insurance_charges, 'insurance.csv', 'charges')

# Answering questions
class PatientsInfo:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_statuses, patients_regions, patients_insurance_charges):
        self.ages = patients_ages
        self.sexes = patients_sexes
        self.bmis = patients_bmis
        self.num_children = patients_num_children
        self.smoker_statuses = patients_smoker_statuses
        self.regions = patients_regions
        self.insurance_charges = patients_insurance_charges

    def avarage_age(self):
        sum_of_ages = 0
        legnth_of_ages = len(self.ages)
        for age in self.ages:
            sum_of_ages += int(age)
        avg_age = int(sum_of_ages / legnth_of_ages)
        return "The average age is: {}".format(avg_age)

    def male_or_female(self):
        males = 0
        females = 0
        for sex in self.sexes:
            if sex == 'male':
                males += 1
            else:
                females += 1
        return "The number of males is {males}, and the number of females is {females}.".format(males=males, females=females)

    def unique_regions(self):
        unique_regions = []
        for region in self.regions:
            if region not in unique_regions:
                unique_regions.append(region)
        return "The unique regions are: {}".format(unique_regions)

    def average_charges(self):
        total_charges = 0
        for charge in self.insurance_charges:
            total_charges += Decimal(charge)
        avg_charges = round(total_charges / len(self.insurance_charges), 2)
        return "The average insurance charge is {}".format(avg_charges)

    def create_dictionary(self):
        patients_dict = {}
        patients_dict["age"] = [int(age) for age in self.ages]
        patients_dict["sex"] = self.sexes
        patients_dict["bmi"] = self.bmis
        patients_dict["children"] = self.num_children
        patients_dict["smoker"] = self.smoker_statuses
        patients_dict["region"] = self.regions
        patients_dict["charge"] = self.insurance_charges
        return patients_dict



patients_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

print(patients_info.avarage_age())
print(patients_info.male_or_female())
print(patients_info.unique_regions())
print(patients_info.average_charges())
