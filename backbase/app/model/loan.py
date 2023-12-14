from app import db
from datetime import datetime
from app.model.user import User

class Loan(db.Model):
    loan_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'))
    jumlah_pinjaman = db.Column(db.Float, nullable=False)
    tanggal_pinjaman = db.Column(db.DateTime, default=datetime.utcnow)
    tanggal_jatuh_tempo = db.Column(db.DateTime, nullable=False)
    status_pinjaman = db.Column(db.String(50), nullable=False)
    bunga_pinjaman = db.Column(db.Float, nullable=False)
    total_pembayaran = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Loan {}>'.format(self.loan_id)

