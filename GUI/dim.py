from tkinter import * 
from tkinter import ttk
from openpyxl.workbook import Workbook #Create workbook in our own
from openpyxl import load_workbook # file that has been already created

# Drop boxes for Wrapper2
Dimensions = ttk.Combobox(wrapper2, value = [" "], width=15)
Dimensions.grid(row=2, column = 3, padx=10, pady=10)
Dimensions.current(0)

Dimensions.config(value=Mich_dim)
if(Dimensions.get() == '10R22.5'):
	TP.config(value=[' ','All'])
	SLR_in.config(value = [ ' ','18.7'])
	SLR_mm.config(value=[' ','474.98'])
	UND_in.config(value=[' ','40.1'])
	UND_mm.config(value=[' ','1018.54'])
				

		
		