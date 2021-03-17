
import openpyxl


path = 'sheet1.xlsx'

wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

cell_obj = sheet_obj.cell(row=2, column=3)

print(cell_obj.value)

a = 5
a.bit_length()