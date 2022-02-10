import xlwings as xw
import openpyxl
from datetime import date
import os
from pathlib import Path

# filepath = r"\\Apckranefa01pv\apckr001\CKR\APCKRMFLPT001P\G_Drive\Groups\QA\SQT by QE\MODULES\TeleBot\QC Molding System for Telebot.xlsm"



def saveone(filepath):
    parentDir = r"C:\Users\User\Documents\President University\Thesis\Production Schedule"
    dateDir = str("2021-12-29")

    link = os.path.join(parentDir, dateDir)
    p = Path(link)

    if p.exists() == True:
        dirExist = True
        print("Exist")
    else:
        os.mkdir(link)

    xlDir = Path(os.path.join(p, "ScheduleToday.xlsx"))
    if xlDir.exists() == True:
        return xlDir
    else:
        app = xw.App(visible=True, add_book=False)
        wb = app.books.open(filepath)
        run = wb.app.macro("SQL_Server.runs")
        run()

        wb.save()
        if len(wb.app.books) == 1:
            wb.app.quit()
        else:
            wb.close()

        wb = openpyxl.load_workbook(filepath)

        sheets = wb.sheetnames

        for s in sheets:
            print(s)
            if s != 'MAIN':
                sheet_name = wb.get_sheet_by_name(s)
                wb.remove_sheet(sheet_name)

        if p.exists() == True:
            # savedXl = fr'{link}/ScheduleToday.xlsx'
            savedXl = xlDir
            wb.save(savedXl)
            return savedXl
        else:
            print("No Such Directory")
            return None


#(saveone(filepath))