import openpyxl
#read our xl-file:
wb = openpyxl.load_workbook(r'app\db\records.xlsx')
#active sheet in xl-file:
sheet = wb.active
print(sheet['A1'].value)
print(sheet['B1'].value)
sheet['B2'] = '1234'
print(sheet['B2'].value)
wb.save(r'app\db\records2.xlsx')
