
# Text-Based Invoice Data Extraction

invoices = [
    "P101,2,500",
    "P102,5,1200",
    "P103,3,750",
    "P104,abc,900",
    "P105,2",
    "P106,4,1000"
]

print("------ INVOICE DATA REPORT ------")

for invoice in invoices:
    parts = invoice.split(",")

    # Check the number of fields
    if len(parts) != 3:
        print(invoice, "-> Malformed record")
        continue

    code = parts[0].strip()
    quantity = parts[1].strip()
    amount = parts[2].strip()

    # Validate extracted data
    if not code.startswith("P") or not code[1:].isdigit():
        print(invoice, "-> Invalid product code")
        continue

    if not quantity.isdigit() or not amount.isdigit():
        print(invoice, "-> Invalid quantity or amount")
        continue

    quantity = int(quantity)
    amount = float(amount)

    if quantity <= 0 or amount < 0:
        print(invoice, "-> Invalid values")
        continue

    print("Product Code:", code)
    print("Quantity:", quantity)
    print("Amount: Rs.", amount)
    print("Status: Valid")
    print()
