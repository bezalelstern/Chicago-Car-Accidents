import pymongo
from flask import jsonify

from database.connect import accidents, accident_details, injuries


def get_accidents_by_beat(beat):
    accident_count = accidents.count_documents({'BEAT_OF_OCCURRENCE': str(beat)})
    return {
        "beat": beat,
        "accident_count": accident_count
    }

def get_accidents_by_date(beat,start_date,end_date):
    try:
        query = {
            'BEAT_OF_OCCURRENCE': beat,
            'crash_date': {'$gte': str(start_date), '$lte': str(end_date)}
        }

        crash_count = accidents.count_documents(query)
        return jsonify({"total_accidents": crash_count})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
