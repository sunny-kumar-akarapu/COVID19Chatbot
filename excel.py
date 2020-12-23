from xlwt import Workbook
import xlrd
# Workbook is created
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

def initiate():
    file = open('questions.txt', 'r')
    Questions=[line for line in file]
    size=len(Questions)
    for Qno in range(1,len(Questions)+1):
        sheet1.write(Qno, 0,Questions[Qno-1])
    wb.save('patientsDetails.xls')

def addNewColumn(details):
    wbR=xlrd.open_workbook('patientsDetails.xls')
    sheet=wbR.sheet_by_name('Sheet 1')
    for i in range(0,len(details)):
        sheet1.write(i,sheet.ncols+1,details[i])
    wb.save('patientsDetails.xls')
