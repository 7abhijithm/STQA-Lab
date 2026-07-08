from openpyxl import Workbook

wb = Workbook()

ws = wb.active

ws.append(["EmpID","Name","Department","Salary"])

for i in range(1,11):

    ws.append([

        i,

        "Employee"+str(i),

        "IT",

        30000+i*1000

    ])

wb.save("employees.xlsx")

print("Excel file created.")