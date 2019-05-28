#!/usr/bin/env python3

import openpyxl
import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()
    wb = openpyxl.load_workbook('nederlands.xlsx')
    sheet = wb.get_sheet_by_name('ecole')


i=1
nl=sheet["B"+str(i)].value
fr=sheet["B"+str(i)].value

while fr is not None :
	print("NL:" + nl +" FR:" + fr)
	i=i+1
	nl=sheet["A"+str(i)].value
	fr=sheet["B"+str(i)].value