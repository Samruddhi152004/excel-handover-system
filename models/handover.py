from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class HandoverRecord(db.Model):
    __tablename__ = 'handover_records'
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255), nullable=False)
    sector = db.Column(db.String(150), nullable=False)
    area = db.Column(db.String(150), nullable=False)
    handover_to = db.Column(db.String(150), nullable=False)
    role_team = db.Column(db.String(150), nullable=False)
    date_sent = db.Column(db.Date, nullable=False)
    sent_through = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    remarks = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "file_name": self.file_name,
            "sector": self.sector,
            "area": self.area,
            "handover_to": self.handover_to,
            "role_team": self.role_team,
            "date_sent": self.date_sent.strftime("%Y-%m-%d"),
            "sent_through": self.sent_through,
            "status": self.status,
            "remarks": self.remarks
        }
