from database.connect import accidents, accident_details, injuries


def get_accidents_by_beat(beat):
    accident_count = accidents.count_documents({'BEAT_OF_OCCURRENCE': str(beat)})
    return {
        "beat": beat,
        "accident_count": accident_count
    }



def find_by_date(beat,start_date,end_date):
    try:
        query = {
            'BEAT_OF_OCCURRENCE': beat,
            'crash_date': {'$gte': str(start_date), '$lte': str(end_date)}
        }
        crash_count = accidents.count_documents(query)
        return {"total_accidents": crash_count}
    except Exception as e:
        return {"error": str(e)}, 500



def group_accidents(beat):
    try:
        query = [
            {"$match":{
            "BEAT_OF_OCCURRENCE": beat
        }},
            {'$group': {
                '_id': '$PRIM_CONTRIBUTORY_CAUSE',
                'count': {'$sum': 1},
                'accidents': {'$push': {
                    'crash_type': '$CRASH_TYPE',
                    'damage': '$DAMAGE',
                    'num_units': '$NUM_UNITS',
                    'sec_contributory_cause': '$SEC_CONTRIBUTORY_CAUSE'
                }}
            }},
        ]
        results = list(accident_details.aggregate(query))
        return results

    except Exception as e:
        return {"error": str(e)}, 500
