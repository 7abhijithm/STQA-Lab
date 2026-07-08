from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.append(["ProductID","Name","Category","Price"])

employees = [
[101,"Laptop","Electronics",55000],
[102,"Mouse","Electronics",600],
[103,"Keyboard","Electronics",1200],
[104,"Monitor","Electronics",15000],
[105,"Printer","Electronics",8500],
[106,"Chair","Furniture",2500],
[107,"Table","Furniture",5000],
[108,"Bottle","Accessories",350],
[109,"Bag","Accessories",1200],
[110,"Notebook","Stationery",80]
]

for e in employees:
    ws.append(e)

wb.save("employee.xlsx")

print("10 Product Records Inserted Successfully")