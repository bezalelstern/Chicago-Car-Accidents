from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request
from database.connect import accidents
from repository.accident_repository import get_accidents_by_beat
from repository.csv_repository import init_db
from services.service import get_time_range

info_bp = Blueprint('info_bp', __name__)

@info_bp.route('/init', methods=['GET'])
def init():
    init_db()
    return jsonify({'message': 'Database initialized'})

@info_bp.route('/accidents/<beat>', methods=['GET'])
def get_accidents(beat):
    accidents = get_accidents_by_beat(beat)
    return jsonify(accidents)


@info_bp.route('/accidents_date', methods=['POST'])
def get_accidents_by_date():
    try:
        data = request.json
        beat = data.get('beat')
        time_period = data.get('time_period')
        start_date = data.get('start_date')
        start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
        start_date,end_date = get_time_range(time_period, start_date)

        query = {
            'BEAT_OF_OCCURRENCE': beat,
            'crash_date': {'$gte': str(start_date), '$lte': str(end_date)}
        }

        crashes = accidents.find(query)
        crash_count1 = len(list(crashes))
        print(crash_count1)
        crash_count = accidents.count_documents(query)
        return jsonify({"total_accidents": crash_count})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


