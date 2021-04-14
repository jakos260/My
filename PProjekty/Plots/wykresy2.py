import matplotlib.pyplot as plt
from openpyxl import load_workbook

wb = load_workbook('mat3.xlsx') #___nazwa pliku___

sheet = wb.active
# sheet = wb.get_sheet_by_name('Dane') #___nazwa arkusza___

# wb.save('excel_file.xlsx')
print(wb)
