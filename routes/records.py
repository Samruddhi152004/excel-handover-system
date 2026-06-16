from flask import Blueprint, request, jsonify
from datetime import datetime
from models.handover import HandoverRecord, db
from utils.validators import validate_record

records_bp = Blueprint('records', __name__)

@records_bp.route('/records', methods=['POST'])
def create_record():
    data=request.json
    valid,msg=validate_record(data)
    if not valid:
        return jsonify({'error':msg}),400
    record=HandoverRecord(
        file_name=data['file_name'],
        sector=data['sector'],
        area=data['area'],
        handover_to=data['handover_to'],
        role_team=data['role_team'],
        date_sent=datetime.strptime(data['date_sent'],'%Y-%m-%d'),
        sent_through=data['sent_through'],
        status=data['status'],
        remarks=data.get('remarks')
    )
    db.session.add(record)
    db.session.commit()
    return jsonify({'message':'Record Created','id':record.id})

@records_bp.route('/records')
def get_records():
    search=request.args.get('search')
    status=request.args.get('status')
    query=HandoverRecord.query
    if search:
        query=query.filter(
            (HandoverRecord.file_name.ilike(f'%{search}%')) |
            (HandoverRecord.sector.ilike(f'%{search}%')) |
            (HandoverRecord.area.ilike(f'%{search}%')) |
            (HandoverRecord.handover_to.ilike(f'%{search}%')) |
            (HandoverRecord.role_team.ilike(f'%{search}%'))
        )
    if status:
        query=query.filter_by(status=status)
    return jsonify([r.to_dict() for r in query.all()])

@records_bp.route('/records/<int:id>')
def get_record(id):
    return jsonify(HandoverRecord.query.get_or_404(id).to_dict())

@records_bp.route('/records/<int:id>', methods=['PUT'])
def update_record(id):
    record=HandoverRecord.query.get_or_404(id)
    data=request.json
    for k,v in data.items():
        if k == "date_sent":
            v = datetime.strptime(v, "%Y-%m-%d")
        setattr(record,k,v)
    db.session.commit()
    return jsonify({'message':'Record Updated'})

@records_bp.route('/records/<int:id>', methods=['DELETE'])
def delete_record(id):
    record=HandoverRecord.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    return jsonify({'message':'Record Deleted'})

@records_bp.route('/records', methods=['DELETE'])
def delete_all_records():
    HandoverRecord.query.delete()
    db.session.commit()
    return jsonify({'message':'All Records Deleted'})


