f=open('','r')
l=f.readlines()
conn = pymssql.connect(server='icserver.database.windows.net', user='icserver@icserver', password='MANipal2016#', database='Piimagesensor',autocommit=True)
cursor = conn.cursor()
SQLCommand = ("INSERT INTO [dbo].[IC1](operatorid,cableid,uploaddate,shiftstart,shiftend,cabletest,cablesequence) VALUES (%s,%s,%s,%s,%s,%s,%s)")
Values = (oid,cid,dt,shiftstart,shiftend,ans,cseq)
cursor.execute(SQLCommand,Values)
#cursor.commit()
cursor.close()
conn.close()
