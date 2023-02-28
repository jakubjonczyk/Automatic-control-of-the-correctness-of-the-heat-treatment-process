
import pandas as pd  

from tkinter import *
from tkinter import messagebox

Test = pd.read_csv("Test.csv")
DB = pd.read_csv("DB.csv")

for ind in Test.index:
   x = DB[DB['Part'] == Test['Part'][ind]]
   if x.empty:
    print('NOK - Part Charge:' + str(Test['Charge'][ind]))
    continue
   if not x['Temperature'].values == Test['Temperature'][ind]:
       print("NOK - temperature Charge:" + str(Test['Charge'][ind]))

# Ending messagebox
messagebox.showinfo(title="Message", message="Checking is done")