from app.model.loan import Loan
from app import response, app,db
from flask import request


def index():
    try:
        loan = Loan.query.all()
        data_loan = transfrom (loan)
        return response.ok (data_loan, "success")
    except Exception as e:
        print (e)

def transfrom(loan):
    array = []
    for i in loan:
        array.append({
            'loan_id' : i.loan_id,
            'user_id' : i.user_id,
            'jumlah_pinjaman' : i. jumlah_pinjaman,
            'tanggal_pinjaman' : i.tanggal_pinjaman,
            'tanggal_jauth_tempo' : i.tanggal_jatuh_tempo,
            'setatus_pinjaman' : i.setatus_pinjaman,
            'bungga_pinjaman' : i.bunga_pinjaman,
            'total_pinjaman' : i.total_pinjaman
        })
    return array

def show(loan_id):
    try:
        loan = Loan.query.filter_by(loan_id=loan_id).first()
        if not loan:
            return response.badRequest([],'Empty....')
        
        data_loan = singleTransfrom(loan)
        return response.ok(data_loan,"")
    except Exception as e:
        print(e)

def singleTransfrom(loan):
    data_loan ={
        'loan_id' : loan.loan_id,
        'user_id' : loan.user_id,
        'jumlah_pinjaman' : loan. jumlah_pinjaman,
        'tanggal_pinjaman' : loan.tanggal_pinjaman,
        'tanggal_jautuh_tempo' : loan.tanggal_jatuh_tempo,
        'setatus_pinjaman' : loan.setatus_pinjaman,
        'bungga_pinjaman' : loan.bunga_pinjaman,
        'total_pinjaman' : loan.total_pinjaman
    }

    return data_loan

def store():
    try:
        loan_id = request.json['loan_id']
        user_id = request.json['user_id']
        jumlah_pinjaman = request.json['jumlah_pinjaman']
        tanggal_pinjaman = request.json['tanggal_pinjaman']
        tanggal_jatuh_tempo = request.json['tanggal_jauth_tempo']
        setatus_pinjaman = request.json['setatus_pinjaman']
        bungga_pinjaman = request.json['bungga_pinjaman']
        total_pinjaman = request.json['total_pinjaman']

        loan = Loan(loan_id = loan_id,user_id = user_id,jumlah_pinjaman = jumlah_pinjaman,tanggal_pinjaman = tanggal_pinjaman,tanggal_jatuh_tempo = tanggal_jatuh_tempo,setatus_pinjaman = setatus_pinjaman,bungga_pinjaman = bungga_pinjaman,total_pinjaman = total_pinjaman)
        
        db.session.add(loan)
        db.session.commit()

        return response.ok('', 'Successfully Create data!')
    
    except Exception as e:
        print(e)

def update(loan_id):
    try: 
        loan_id = request.json['loan_id']
        user_id = request.json['user_id']
        jumlah_pinjaman = request.json['jumlah_pinjaman']
        tanggal_pinjaman = request.json['tanggal_pinjaman']
        tanggal_jatuh_tempo = request.json['tanggal_jauth_tempo']
        setatus_pinjaman = request.json['setatus_pinjaman']
        bungga_pinjaman = request.json['bungga_pinjaman']
        total_pinjaman = request.json['total_pinjaman']

        loan = Loan.query.filter_by(id=id).first()
        loan.loan_id = loan_id
        loan.user_id = user_id
        loan.jumlah_pinjaman = jumlah_pinjaman
        loan.tanggal_pinjaman = tanggal_pinjaman
        loan.tanggal_jatuh_tempo = tanggal_jatuh_tempo
        loan.setatus_pinjaman = setatus_pinjaman
        loan.bungga_pinjaman = bungga_pinjaman
        loan.total_pinjaman = total_pinjaman

        db.session.commit()

        return response.ok ('', 'Successfully update data!')
    
    except Exception as e:
        print(e)

def delate (loan_id):
    try:
        loan = Loan.query.filter_by(loan_id=loan_id).first()

        if not loan:
            return response.badRequest([], 'Empty...')

        db.session.delete(loan)

        return response.ok ('', 'Successfully update data!')
    
    except Exception as e:
        print(e)
























