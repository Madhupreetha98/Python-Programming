import xlrd
workbook = xlrd.open_workbook("file.xlsx")
worksheet = workbook.sheet_by_index(0)
print(" ".format(worksheet.cell(4,2).value))
