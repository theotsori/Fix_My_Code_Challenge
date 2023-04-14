from flask import Blueprint, jsonify

statu_bp = Blueprint("status", __name__)

@status_bp.route('/api/v1/status', methods=['GET'])
def get_status():
    return jsonify({'status': 'OK'})
