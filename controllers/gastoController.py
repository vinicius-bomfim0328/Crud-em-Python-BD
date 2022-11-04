import services.database as db
import models.gasto as Gastos

def incluir(gasto):
    count = db.cursor.execute("""
    INSERT INTO dbo.gastos (mes, renda ,lazer, alimentacao, casa, saude, transporte) 
    VALUES (?,?,?,?,?,?,?)""",
    gasto.mes, gasto.lazer, gasto.renda, gasto.alimentacao, gasto.casa, gasto.saude, gasto.transporte).rowcount
    db.cnxn.commit()

def consultar():
    db.cursor.execute("SELECT * FROM gastos")
    costumerList = []

    for linhas in db.cursor.fetchall():
        costumerList.append(Gastos.Gasto(linhas[1],linhas[2],linhas[3],linhas[4],linhas[5],linhas[6],linhas[7]))
    
    return costumerList