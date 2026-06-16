from flask import Blueprint, jsonify
from models.handover import HandoverRecord, db

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    return jsonify({
        'total_files_handed_over': HandoverRecord.query.count(),
        'total_persons_assigned': db.session.query(HandoverRecord.handover_to).distinct().count(),
        'total_sent_records': HandoverRecord.query.filter_by(status='Sent').count(),
        'total_completed_records': HandoverRecord.query.filter_by(status='Completed').count()
    })
