import csv

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
organize_data_in_lists(sexes 'insurance.csv', 'sex')
organize_data_in_lists(bmis 'insurance.csv', 'bmi')
organize_data_in_lists(num_children 'insurance.csv', 'children')
organize_data_in_lists(smoker_statuses 'insurance.csv', 'smoker')
organize_data_in_lists(regions 'insurance.csv', 'region')
organize_data_in_lists(insurance_charges 'insurance.csv', 'charges')

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
        avg_age = sum_of_ages / legnth_of_ages
        return avg_age


patient1 = PatientsInfo()

        

