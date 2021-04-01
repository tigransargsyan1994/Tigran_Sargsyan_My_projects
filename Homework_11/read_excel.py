import os


from openpyxl import load_workbook
wb = load_workbook(filename= 'example.xlsx')
sheet_ranges = wb['Sheet1']

c1 = sheet_ranges['A']
c2 = sheet_ranges['B']

d = {}
for i in zip(c1,c2):
    d[i[0].value] = i[1].value

print(d)