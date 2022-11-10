import services.database as db
import models.gasto as Gastos

def incluir(gasto):
    count = db.cursor.execute("""
    INSERT INTO dbo.Contole_Gastos (Mes, Renda , Lazer, Alimentacao, Casa, Saude, Transporte) 
    VALUES (?,?,?,?,?,?,?)""",
    gasto.mes, gasto.renda, gasto.lazer, gasto.alimentacao, gasto.casa, gasto.saude, gasto.transporte).rowcount
    db.cnxn.commit()

def consultar():
    db.cursor.execute("SELECT * FROM Contole_Gastos")
    costumerList = []

    for linhas in db.cursor.fetchall():
        costumerList.append(Gastos.Gasto(linhas[0],linhas[1],linhas[2],linhas[3],linhas[4],linhas[5],linhas[6],linhas[7]))
    
    return costumerList

def excluir(ID):
    count = db.cursor.execute("""
    DELETE FROM Contole_Gastos WHERE ID = ?""",
    ID).rowcount
    db.cnxn.commit()

def alterar(gasto):
    count = db.cursor.execute("""
    UPDATE Contole_Gastos 
    SET Mes = ?, Renda = ?, Lazer = ?, Alimentacao = ?, Casa = ?, Saude = ?, Transporte = ?
    WHERE ID = ?
    """,
    gasto.mes, gasto.renda, gasto.lazer, gasto.alimentacao, gasto.casa, gasto.saude, gasto.transporte, gasto.ID).rowcount
    db.cnxn.commit()

def selecionargasto(ID):
    db.cursor.execute("SELECT * FROM Contole_Gastos WHERE ID = ?", ID)
    costumerList = []

    for linhas in db.cursor.fetchall():
        costumerList.append(Gastos.Gasto(linhas[0],linhas[1],linhas[2],linhas[3],linhas[4],linhas[5],linhas[6],linhas[7]))
    
    return costumerList[0]