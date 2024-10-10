import csv


from database.connect import db, drivers, cars


def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row

   for row in read_csv('data/practice_data.csv'):
       car = {
           'license_id': row['CarLicense'],
           'brand': row['CarBrand'],
           'color': row['CarColor']
       }


       car_id = cars.insert_one(car).inserted_id


       address = {
           'city': row['City'],
           'street': row['Street'],
           'state': row['State']
       }


       driver = {
           'passport': row['PassportNumber'],
           'first_name': row['FullName'].split(' ')[0],
           'last_name': row['FullName'].split(' ')[1],
           'car_id': car_id,
           'address': address
       }


       drivers.insert_one(driver)