from app import db
from datetime import datetime
from app.model.loan import Loan

class Payment(db.Model):
    payment_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    loan_id = db.Column(db.BigInteger, db.ForeignKey('loan.loan_id'))
    jumlah_pengembalian = db.Column(db.Float, nullable=False)
    tanggal_pengembalian = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Pengembalian {}>'.format(self.payment_id)

