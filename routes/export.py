from flask import Blueprint, Response
from models.handover import HandoverRecord
import csv, io

export_bp=Blueprint('export',__name__)

@export_bp.route('/export/csv')
def export_csv():
    output=io.StringIO()
    writer=csv.writer(output)
    writer.writerow(['ID','File Name','Sector','Area','Handover To','Role Team','Date Sent','Sent Through','Status','Remarks'])
    for r in HandoverRecord.query.all():
        writer.writerow([r.id,r.file_name,r.sector,r.area,r.handover_to,r.role_team,r.date_sent,r.sent_through,r.status,r.remarks])
    return Response(output.getvalue(),mimetype='text/csv',headers={'Content-Disposition':'attachment; filename=handover_records.csv'})
