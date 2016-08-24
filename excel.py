from itertools import izip

import openpyxl

def xls(titles, urls):
  wb = openpyxl.Workbook()
  sheet = wb.active
  sheet.title = "test"
  i = 1
  for t, u in izip(titles, urls):
    sheet.cell('A' + str(i)).value = u'=HYPERLINK("{}","{}")'.format(u, t)
    i += 1

  wb.save('a.xls')

