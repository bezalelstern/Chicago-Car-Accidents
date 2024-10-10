import csv
from datetime import datetime

from database.connect import accidents, accident_details, injuries


def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row



def init_db():
   accidents.drop()
   accident_details.drop()
   injuries.drop()

   for row in read_csv('data/Traffic_Crashes_-_Crashes - 20k rows.csv'):
       accident_detail = {
           '_id': row['CRASH_RECORD_ID'],
           'FIRST_CRASH_TYPE': row['FIRST_CRASH_TYPE'],
           'CRASH_TYPE': row['CRASH_TYPE'],
           'BEAT_OF_OCCURRENCE': row['BEAT_OF_OCCURRENCE'],
           'PRIM_CONTRIBUTORY_CAUSE': row['PRIM_CONTRIBUTORY_CAUSE'],
           'SEC_CONTRIBUTORY_CAUSE': row['SEC_CONTRIBUTORY_CAUSE'],
           'NUM_UNITS': row['NUM_UNITS'],
           'DAMAGE': row['DAMAGE']
       }


       details_id = accident_details.insert_one(accident_detail).inserted_id



       injurie = {
                '_id': row['CRASH_RECORD_ID'],
                'BEAT_OF_OCCURRENCE': row['BEAT_OF_OCCURRENCE'],
               "MOST_SEVERE_INJURY": row["MOST_SEVERE_INJURY"],
               "INJURIES_TOTAL": row["INJURIES_TOTAL"],
               "INJURIES_FATAL": row["INJURIES_FATAL"],
               "INJURIES_INCAPACITATING": row["INJURIES_INCAPACITATING"],
               "INJURIES_NON_INCAPACITATING": row["INJURIES_NON_INCAPACITATING"],
               "INJURIES_REPORTED_NOT_EVIDENT": row["INJURIES_REPORTED_NOT_EVIDENT"],
               "INJURIES_NO_INDICATION": row["INJURIES_NO_INDICATION"],
           }

       injurie_id = injuries.insert_one(injurie).inserted_id

       accident = {
           '_id': row['CRASH_RECORD_ID'],
           "crash_date": parse_date(row["CRASH_DATE"]),
           'BEAT_OF_OCCURRENCE': row['BEAT_OF_OCCURRENCE'],
           'details_id': details_id,
           'injurie_id': injurie_id,
           'CRASH_HOUR': row['CRASH_HOUR'],
           'CRASH_DAY_OF_WEEK': row['CRASH_DAY_OF_WEEK'],
           'CRASH_MONTH': row['CRASH_MONTH'],
           "location": {
               "street_no": row["STREET_NO"],
               "street_direction": row["STREET_DIRECTION"],
               "street_name": row["STREET_NAME"],
               "latitude": row["LATITUDE"],
               "longitude": row["LONGITUDE"]
           },
       }
       accidents.insert_one(accident)

def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return str(datetime.strptime(date_str, date_format).date())