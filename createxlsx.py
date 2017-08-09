import xlsxwriter

#create xlsx
workbook = xlsxwriter.Workbook('3.xlsx')
worksheet = workbook.add_worksheet()

#format content
format = workbook.add_format()
format.set_font_color('black')
format.set_bg_color('green')
format.set_border(1)

#write  
for i in range(10,15):
    worksheet.write('H'+str(i), 'ok',format)

workbook.close()
