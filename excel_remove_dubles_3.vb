Set objExcel=Createobject("Excel.Application")
Set objWbk=objExcel.Workbooks.Open("FilePath")
Set objSht = objWbk.WorkSheets(1)
objExcel.Visible=True
objSht.UsedRange.RemoveDuplicates 1,1