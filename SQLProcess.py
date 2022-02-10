import sys
import site
import pyodbc
from datetime import datetime
from datetime import timedelta

# server = 'DCKR00802521'
# database = 'QualityEngineeringDB'
# username = 'sa'
# password = 'Labsql!'
# conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

server = 'FSNGPZ\SQLEXPRESS'
database = 'QualityEngineeringDB'
username = ''
password = ''
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = conn.cursor()

def qcmold(partnum):
    sql = f"SELECT RTRIM(LTRIM(LINK)), RTRIM(LTRIM(CRITICAL)) FROM [QualityEngineeringDB].[dbo].[SQTLogbook] WHERE PART# like '%{partnum}%'"
    print(sql)
    cursor.execute(sql)
    count = 0
    for row in cursor:
        count = 1
        link = row[0]
        critical = row[1]
        return critical, link
    if count == 0:
        return None

# result = (qcmold('11002-882414'))
# if result == None:
#     print("Kesini")

def suppclass(code):
    sql = f"SELECT RTRIM(LTRIM(STATUS)), RTRIM(LTRIM(CLASS)) FROM [IQC].[dbo].[SupplierClass] WHERE Code like '%{code}%'"
    print(sql)
    cursor.execute(sql)
    for row in cursor:
        status = row[0]
        CClass = row[1]

    return status, CClass


def subcom(partnum):
    count = 0
    sql = f"SELECT TOP 1 RTRIM(LTRIM(COMM)), RTRIM(LTRIM(CMID)) FROM [IQC].[dbo].[PNSubcom] WHERE RTRIM(LTRIM(PART#)) LIKE '%{partnum}%' "
    print(sql)
    cursor.execute(sql)
    for row in cursor:
        count = 1
        comm = row[0]
        cmid = row[1]
        return comm, cmid
    if count == 0:
        return None

# print(subcom('P108-0300'))
def materialrisk(comm, cmid):
    sql = f"SELECT RTRIM(LTRIM(HE)), RTRIM(LTRIM(PH)) FROM [IQC].[dbo].[MaterialRisk] WHERE COMODITY LIKE '%{comm}%' AND SUBCOMODITY LIKE '%{cmid}%'"
    count = 0
    cursor.execute(sql)
    materialrisk = []
    for row in cursor:
        count = 1
        materialrisk.append(row)
        he = row[0]
        ph = row[1]
    if count == 0:
        return None
    return he, ph


def typeClass(comm, cmid):
    sql = f"SELECT RTRIM(LTRIM(TypeClass)) FROM [IQC].[dbo].[MaterialRisk] WHERE COMODITY LIKE '%{comm}%' AND SUBCOMODITY LIKE '%{cmid}%'"
    print(sql)
    count = 0
    cursor.execute(sql)
    for row in cursor:
        count = 1
        tClass = row[0]
    if count == 0:
        return None
    return tClass

def rawMatLER(partnumRawMat, suppcode):
    sql = f"SELECT RTRIM(LTRIM(HE_LER#)), RTRIM(LTRIM(HE_Date)), RTRIM(LTRIM(PH_LER#)), " \
          f"RTRIM(LTRIM(PH_Date)) FROM  [IQC].[dbo].[RawMatxLER] WHERE Raw_Material LIKE '%{partnumRawMat}%' AND " \
          f"Subcon LIKE( SELECT Name FROM [IQC].[dbo].[SupplierClass] WHERE Code LIKE '%{suppcode}%')"
    print(sql)
    count = 0
    cursor.execute(sql)
    for row in cursor:
        count = 1
        HE_LER = row[0]
        HE_Date = row[1]
        PH_LER = row[2]
        PH_Date = row[3]
    if count == 0:
        sqlrawMat = f"SELECT RTRIM(LTRIM(HE_LER#)), RTRIM(LTRIM(HE_Date)), RTRIM(LTRIM(PH_LER#)), " \
        f"RTRIM(LTRIM(PH_Date)) FROM  [IQC].[dbo].[RawMatxLER] WHERE Raw_Material LIKE '%{partnumRawMat}%'"
        print("Check", sqlrawMat)
        cursor.execute(sqlrawMat)
        dataRawMat = []
        for row in cursor:
            dataRawMat = [row[0], row[1], row[2], row[3]]

        sqlNameSubcon = f"SELECT Name FROM [IQC].[dbo].[SupplierClass] WHERE Code LIKE '%{suppcode}%'"
        cursor.execute(sqlNameSubcon)
        nameSubcon = None

        for row in cursor:
            nameSubcon = row[0]

        if nameSubcon is None:
            return None, suppcode
        else:
            sqlSubcon = f"SELECT RTRIM(LTRIM(HE_LER#)), RTRIM(LTRIM(HE_Date)), RTRIM(LTRIM(PH_LER#)), " \
            f"RTRIM(LTRIM(PH_Date)) FROM  [IQC].[dbo].[RawMatxLER] WHERE Subcon LIKE( SELECT Name FROM [IQC].[dbo].[SupplierClass] WHERE Code LIKE '%{suppcode}%')"
            print(sqlSubcon)
            cursor.execute(sqlSubcon)
            dataSubcon = []
            for row in cursor:
                dataSubcon = row[0]
            print("DATASUBCON:", dataSubcon)
            print("DATARAWMAT:", dataRawMat)
            if not dataSubcon and not dataRawMat:
                print("1")
                return None, partnumRawMat, suppcode
            elif not dataRawMat:
                print("2")
                return None, "PNRawMat:" + partnumRawMat
            elif not dataSubcon:
                print("2")
                return None, "Subcon:" + nameSubcon

    return (HE_LER, HE_Date, PH_LER, PH_Date)
# print(rawMatLER("11007-74751", "4341"))

def PNRawMat(partnum):
    sql = f"SELECT Raw_Material FROM [IQC].[dbo].[PNxRawMat] WHERE PART# = '{partnum}'"
    print(sql)
    count = 0
    cursor.execute(sql)
    for row in cursor:
        count = 1
        rawMat = row[0]
    if count == 0:
        return None
    return (rawMat)
#print(PNRawMat('BCN33-2179'))

def risklevel (CClass, he, ph):

    if he == 'N/A':
        TestHE = int(0)
    else:
        sqlHE = f"SELECT RTRIM(LTRIM(Class{CClass})) FROM [IQC].[dbo].[RiskLevelSupp] WHERE RiskLevel = '{he}'"
        print(sqlHE)
        cursor.execute(sqlHE)
        for row in cursor:
            TestHE = row[0]

        x = TestHE.isnumeric()
        if x == True:
            TestHE = int(TestHE)
        else:
            TestHE = str(TestHE)
    if ph == 'N/A':
        TestPH = int(0)
    else:
        sqlPH = f"SELECT RTRIM(LTRIM(Class{CClass})) FROM [IQC].[dbo].[RiskLevelSupp] WHERE RiskLevel = '{ph}'"
        print(sqlPH)
        cursor.execute(sqlPH)
        for row in cursor:
            TestPH = row[0]

        x = TestPH.isnumeric()
        if x == True:
            TestPH = int(TestPH)
        else:
            TestPH = str(TestPH)

    return TestHE, TestPH

def risklevelSubcon (CClass, he, ph):

    if he == 'N/A':
        TestHE = int(0)
    else:
        sqlHE = f"SELECT RTRIM(LTRIM(Class{CClass})) FROM [IQC].[dbo].[RiskLevelSubcon] WHERE RiskLevel = '{he}'"
        print(sqlHE)
        cursor.execute(sqlHE)
        for row in cursor:
            TestHE = row[0]

        x = TestHE.isnumeric()
        if x == True:
            TestHE = int(TestHE)
        else:
            TestHE = str(TestHE)
    if ph == 'N/A':
        TestPH = int(0)
    else:
        sqlPH = f"SELECT RTRIM(LTRIM(Class{CClass})) FROM [IQC].[dbo].[RiskLevelSubcon] WHERE RiskLevel = '{ph}'"
        print(sqlPH)
        cursor.execute(sqlPH)
        for row in cursor:
            TestPH = row[0]

        x = TestPH.isnumeric()
        if x == True:
            TestPH = int(TestPH)
        else:
            TestPH = str(TestPH)

    return TestHE, TestPH

def report(partnum, TestHE, TestPH):
    sql = f"select TOP 1 t.batch# from ( SELECT part#,vendor,MAX(submitDate) as MaxDate From [ChemLabEast].[dbo].[submission] Group by part#,vendor) r Inner JOIN [ChemLabEast].[dbo].[submission] t On t.part# = r.part# And t.submitDate = r.MaxDate where t.testing like '%HE%' and t.part# = '{partnum}' ORDER BY MaxDate DESC"
    print(sql)
    c = cursor.execute(sql)
    rows = c.fetchone()
    if rows is not None:
        for row in rows:
            batchHE = row
        sql = f"select TOP 1 r.MaxDate from ( SELECT part#,vendor,MAX(submitDate) as MaxDate From [ChemLabEast].[dbo].[submission] Group by part#,vendor) r Inner JOIN [ChemLabEast].[dbo].[submission] t On t.part# = r.part# And t.submitDate = r.MaxDate where t.testing like '%HE%' and t.part# = '{partnum}' ORDER BY MaxDate DESC"
        cursor.execute(sql)
        for row in cursor:
            LRHe = row[0]
        LRHe = datetime.strptime(LRHe, '%Y-%m-%d')
        totalHE = LRHe + timedelta(days=TestHE)
        dateHE = totalHE.strftime("%Y-%m-%d")
        now = datetime.now()
        diffHE = (totalHE- now).days
        print("Test in ", diffHE, " Days")
        totalHE = totalHE.date()
        LRHe = LRHe.date()
        # diff = totalHE - now
        # print(diff.days)
    else:
        LRHe = '-'
        batchHE = '-'
        totalHE = '-'
        diffHE = '-'
        print("No report for Heavy Element")
    ### End Heavy Element

    sql = f"select TOP 1 t.batch# from ( SELECT part#,vendor,MAX(submitDate) as MaxDate From [ChemLabEast].[dbo].[submission] Group by part#,vendor) r Inner JOIN [ChemLabEast].[dbo].[submission] t On t.part# = r.part# And t.submitDate = r.MaxDate where t.testing like '%PH%' and t.part# = '{partnum}' ORDER BY MaxDate DESC"
    c = cursor.execute(sql)
    rows = c.fetchone()
    if rows is not None:
        for row in rows:
            batchPH = row
        sql = f"select TOP 1 r.MaxDate from ( SELECT part#,vendor,MAX(submitDate) as MaxDate From [ChemLabEast].[dbo].[submission] Group by part#,vendor) r Inner JOIN [ChemLabEast].[dbo].[submission] t On t.part# = r.part# And t.submitDate = r.MaxDate where t.testing like '%PH%' and t.part# = '{partnum}' ORDER BY MaxDate DESC"
        cursor.execute(sql)
        for row in cursor:
            LRPH = row[0]
        LRPH = datetime.strptime(LRPH, '%Y-%m-%d')
        totalPH = LRPH + timedelta(days=TestPH)
        datePH = totalPH.strftime("%Y-%m-%d")
        diffPH = (totalPH - now).days
        print("Test in ", diffPH, " Days")
        totalPH = totalPH.date()
        LRPH = LRPH.date()
    else:
        LRPH = '-'
        batchPH = '-'
        totalPH = '-'
        diffPH = '-'
        print("No report for Phthalate")

    return batchHE, totalHE, diffHE, batchPH, totalPH, diffPH, LRPH, LRHe

# print(report('HCB75-JA70', 360, 0))