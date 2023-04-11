import xlrd
excel_book = xlrd.open_workbook('./files/excel_example.xlsx')
print(excel_book.nsheets)
print(excel_book.sheet_names)