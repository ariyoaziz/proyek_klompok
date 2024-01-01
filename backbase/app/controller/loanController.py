from app.model.payment import Loan
from app import response, app, db
from flask import request
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def index():
    try:
        loans = Loan.query.all()
        data_loans = transform(loans)
        return response.ok(data_loans, "success")
    except Exception as e:
        return response.badRequest([], f"Failed to fetch data. Error: {str(e)}")

def transform(loans):
    array = []
    for loan in loans:
        array.append(singleTransform(loan))
    return array

def singleTransform(loan):
    data_loan = {
        'loan_id': loan.loan_id,
        'user_id': loan.user_id,
        'jumlah_pinjaman': loan.jumlah_pinjaman,
        'jangka_waktu_peminjaman': loan.jangka_waktu_peminjaman,
        'tanggal_pinjaman': loan.tanggal_pinjaman,
        'tanggal_jatuh_tempo': loan.tanggal_jatuh_tempo,
        'status_pinjaman': loan.status_pinjaman,
        'bunga_pinjaman': loan.bunga_pinjaman,
        'total_pembayaran': loan.total_pembayaran
    }
    return data_loan

def store():
    try:
        user_id = request.json['user_id']
        jumlah_pinjaman = request.json['jumlah_pinjaman']
        jangka_waktu_peminjaman = request.json['jangka_waktu_peminjaman']
        bunga_pinjaman = request.json['bunga_pinjaman']
        status_pinjaman = request.json['status_pinjaman']

      
        total_pembayaran = jumlah_pinjaman + (jumlah_pinjaman * (bunga_pinjaman / 100) * jangka_waktu_peminjaman)

        tanggal_pinjaman = datetime.now()
        tanggal_jatuh_tempo = tanggal_pinjaman + relativedelta(months=jangka_waktu_peminjaman)

        

        data_loan = Loan(
            user_id=user_id,
            jumlah_pinjaman=jumlah_pinjaman,
            jangka_waktu_peminjaman=jangka_waktu_peminjaman,
            bunga_pinjaman=bunga_pinjaman,
            status_pinjaman=status_pinjaman,
            total_pembayaran=total_pembayaran,
            tanggal_jatuh_tempo=tanggal_jatuh_tempo,
        )

    
        db.session.add(data_loan)
        db.session.commit()

        return response.ok("", "Successfully created data!")
    except Exception as e:
        return response.badRequest([], f"Data failed to create. Error: {str(e)}")


def update(loan_id):
    try:
        jumlah_pinjaman = request.json.get('jumlah_pinjaman')
        jangka_waktu_peminjaman = request.json.get('jangka_waktu_peminjaman')
        bunga_pinjaman = request.json.get('bunga_pinjaman')
        status_pinjaman = request.json.get('status_pinjaman')

        loan = Loan.query.filter_by(loan_id=loan_id).first()

        if not loan:
            return response.badRequest([], 'Pinjaman tidak ditemukan')


        loan.jumlah_pinjaman = jumlah_pinjaman or loan.jumlah_pinjaman
        loan.jangka_waktu_peminjaman = jangka_waktu_peminjaman or loan.jangka_waktu_peminjaman
        loan.bunga_pinjaman = bunga_pinjaman or loan.bunga_pinjaman
        loan.status_pinjaman = status_pinjaman or loan.status_pinjaman

        # Recalculate total_pembayaran if necessary
        loan.total_pembayaran = loan.jumlah_pinjaman + (loan.jumlah_pinjaman * (loan.bunga_pinjaman / 100) * loan.jangka_waktu_peminjaman)

        db.session.commit()

        return response.ok('', 'Berhasil memperbarui data pinjaman!')
    
    except Exception as e:
        print(e)
        return response.badRequest([], 'Terjadi kesalahan selama proses pembaruan pinjaman')


def delete(loan_id):
    try:
        loan = Loan.query.filter_by(loan_id=loan_id).first()

        if not loan:
            return response.badRequest([], 'Empty...')

        db.session.delete(loan)
        db.session.commit()

        return response.ok('', 'Successfully delete data!')
    
    except Exception as e:
        print(e)

