from app.model.payment import Payment
from app import response, app, db
from flask import request
from datetime import datetime

def index():
    try:
        payments = Payment.query.all()
        data_payment = transfrom(payments)
        return response.ok(data_payment, "success")
    except Exception as e:
        print(e)

def transfrom(payments):
    array = []
    for i in payments:
        array.append({
            'payment_id': i.payment_id,
            'loan_id': i.loan_id,
            'jumlah_pengembalian': i.jumlah_pengembalian,
            'tanggal_pengembalian': i.tanggal_pengembalian,
        })
    return array

def show(payment_id):
    try:
        payment = Payment.query.filter_by(payment_id=payment_id).first()
        if not payment:
            return response.badRequest([], 'Empty....')
        
        data_payment = singleTransfrom(payment)
        return response.ok(data_payment, "")
    except Exception as e:
        print(e)

def singleTransfrom(payment):
    data_payment = {
        'payment_id': payment.payment_id,
        'loan_id': payment.loan_id,
        'jumlah_pengembalian': payment.jumlah_pengembalian,
        'tanggal_pengembalian': payment.tanggal_pengembalian,
    }

    return data_payment

def store():
    try:
        loan_id = request.json['loan_id']
        jumlah_pengembalian = request.json['jumlah_pengembalian']
        tanggal_pengembalian = datetime.now()

        payment = Payment(loan_id=loan_id, jumlah_pengembalian=jumlah_pengembalian, tanggal_pengembalian=tanggal_pengembalian)
        
        db.session.add(payment)
        db.session.commit()

        return response.ok('', 'Successfully Create data!')
    
    except Exception as e:
        print(e)

def update(payment_id):
    try:
        loan_id = request.json['loan_id']
        jumlah_pengembalian = request.json['jumlah_pengembalian']
        tanggal_pengembalian = datetime.now()

        payment = Payment.query.filter_by(payment_id=payment_id).first()

        if not payment:
            return response.badRequest([], 'Pembayaran tidak ditemukan')

        payment.loan_id = loan_id
        payment.jumlah_pengembalian = jumlah_pengembalian
        payment.tanggal_pengembalian = tanggal_pengembalian

        db.session.commit()

        return response.ok('', 'Berhasil memperbarui data!')
    
    except Exception as e:
        print(e)
        return response.badRequest([], 'Terjadi kesalahan selama proses pembaruan')
    

def delete(payment_id):
    try:
        payment = Payment.query.filter_by(payment_id=payment_id).first()

        if not payment:
            return response.badRequest([], 'Empty...')

        db.session.delete(payment)
        db.session.commit()

        return response.ok('', 'Successfully delete data!')
    
    except Exception as e:
        print(e)

