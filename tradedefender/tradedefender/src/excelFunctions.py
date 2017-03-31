import win32com.client as win32
from win32com.client import Dispatch
import os
import sys

COLUMN_INDEX_MAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def printRangeAsPicture(wbkObj, selectionRange, outPath):
    sheetName = selectionRange[:selectionRange.index("!")]
    sheetRange = selectionRange[selectionRange.index("!")+1:]
    xlRange = wbkObj.Sheets(sheetName).Range(sheetRange)
    wbkObj.Sheets.Add(After=wbkObj.Worksheets.Count).Name="temp_image_sheet"
    cht = wbkObj.ActiveSheet.ChartObjects().Add(0, 0, xlRange.Width, xlRange.Height)
    xlRange.CopyPicture()
    # add the chart to new sheet
    cht.Chart.Paste()
    # Export the sheet with the chart to a new file
    cht.Chart.Export(outPath)
    # Delete the sheet
    cht.Delete()
    wbkObj.ActiveSheet.Delete()

def printRangeAsPdf(wbkObj, selectionRange, outPath):
    pass

def openWorkbook(filePath):
    excelObj = Dispatch("Excel.Application")
    excelObj.DisplayAlerts = False
    wbkObj = excelObj.Workbooks.Open(Filename=filePath)
    return(excelObj, wbkObj)

def saveWorkbook(wbkObj):
    wbkObj.Save()

def closeWorkbook(wbkObj):
    wbkObj.Application.Quit()

def closeExcel(excelObj):
    excelObj.Application.Quit()
    del excelObj

def runMacro(wbkObj, moduleName, macroName):
    wbkObj.Application.Run(moduleName+"."+macroName)

def getRangeIndices(selectionRange):
    startCell = selectionRange[selectionRange.index("!")+1:selectionRange.index(":")]
    endCell = selectionRange[selectionRange.index(":")+1:]
    startColumn = COLUMN_INDEX_MAP.index(startCell[0])
    endColumn = COLUMN_INDEX_MAP.index(endCell[0])
    columns = list(sorted(range(startColumn, endColumn)))
    rows = list(sorted(range(int(startCell[1:]), int(endCell[1:])+1)))
    return(rows, columns)

def getCellValue(wbkObj, selectionRange):
    sheetName = selectionRange[:selectionRange.index("!")]
    if(":" in selectionRange):
        rows, columns = getRangeIndices(selectionRange)
        print(rows, columns)
        val = []
        for row in rows:
            tempRow = []
            for column in columns:
                columnChar = COLUMN_INDEX_MAP[column]
                cellTarget = columnChar+str(row)
                tempVal = wbkObj.Sheets(sheetName).Range(cellTarget).Value
                tempRow.append(tempVal)
            val.append(tempRow)
    else:
        val = wbkObj.Sheets(sheetName).Range(selectionRange).Value
    return(val)

def getCellFormula(wbkObj, selectionRange):
    sheetName = selectionRange[:selectionRange.index("!")]
    if(":" in selectionRange):
        rows, columns = getRangeIndices(selectionRange)
        print(rows, columns)
        val = []
        for row in rows:
            tempRow = []
            for column in columns:
                columnChar = COLUMN_INDEX_MAP[column]
                cellTarget = columnChar+str(row)
                tempVal = wbkObj.Sheets(sheetName).Range(cellTarget).Formula
                tempRow.append(tempVal)
            val.append(tempRow)
    else:
        val = wbkObj.Sheets(sheetName).Range(selectionRange).Formula
    return(val)

def changeCellValue(wbkObj, selectionRange, values):
    sheetName = selectionRange[:selectionRange.index("!")]
    if(":" in selectionRange):
        rows, columns = getRangeIndices(selectionRange)
        print(rows, columns)
        if(type(values) != list):
            raise Exception("Multi-cell ranges must be filled with 2-D lists")
        if((len(values)*len(values[0])) != (len(rows)*len(columns))):
            raise Exception("Formula size does not match range size")
        for row in rows:
            for column in columns:
                columnChar = COLUMN_INDEX_MAP[column]
                cellTarget = columnChar+str(row)
                print(row-1, column-columns[0])
                wbkObj.Sheets(sheetName).Range(cellTarget).Value = values[row-1][column-columns[0]]
    else:
        wbkObj.Sheets(sheetName).Range(selectionRange[selectionRange.index("!")+1:]).Value = values

def changeCellFormula(wbkObj, selectionRange, values):
    sheetName = selectionRange[:selectionRange.index("!")]
    if(":" in selectionRange):
        rows, columns = getRangeIndices(selectionRange)
        print(rows, columns)
        if(type(values) != list):
            raise Exception("Multi-cell ranges must be filled with 2-D lists")
        if((len(values)*len(values[0])) != (len(rows)*len(columns))):
            raise Exception("Formula size does not match range size")
        for row in rows:
            for column in columns:
                columnChar = COLUMN_INDEX_MAP[column]
                cellTarget = columnChar+str(row)
                print(row-1, column-columns[0])
                wbkObj.Sheets(sheetName).Range(cellTarget).Formula = values[row-1][column-columns[0]]
    else:
        wbkObj.Sheets(sheetName).Range(selectionRange[selectionRange.index("!")+1:]).Formula = values


if __name__ == "__main__":
    print("Work in progress...")
