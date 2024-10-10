from flask import Blueprint, jsonify, request
from repository.accident_repository import get_accidents_by_beat, find_by_date, group_accidents
from repository.csv_repository import init_db
from services.service import get_time

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

        start_date,end_date = get_time(time_period, start_date)
        result = find_by_date(beat, start_date, end_date)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@info_bp.route('/accidents/by_cause/<beat>', methods=['GET'])
def get_accidents_by_cause(beat):
    return jsonify(group_accidents(beat))





