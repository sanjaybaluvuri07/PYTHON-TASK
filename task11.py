
# Multi-Branch Sales Matrix Comparison

branches = ["Branch A", "Branch B", "Branch C"]
products = ["Laptop", "Mobile", "Tablet"]

# Sales data: branches -> products -> daily sales
sales = [
    [[10, 12, 8], [15, 10, 12], [5, 7, 6]],
    [[8, 10, 9], [20, 15, 18], [7, 6, 8]],
    [[12, 14, 10], [10, 12, 11], [9, 8, 10]]
]

# Calculate total sales of each product
print("PRODUCT-WISE TOTAL SALES")

for p in range(len(products)):
    total = 0

    for b in range(len(branches)):
        for d in range(3):
            total += sales[b][p][d]

    print(products[p], ":", total)

# Calculate total sales of each branch
print("\nBRANCH-WISE TOTAL SALES")

branch_totals = []

for b in range(len(branches)):
    total = 0

    for p in range(len(products)):
        for d in range(3):
            total += sales[b][p][d]

    branch_totals.append(total)
    print(branches[b], ":", total)

# Identify the best-performing branch
best_branch = branch_totals.index(max(branch_totals))

print("\nBest-performing branch:", branches[best_branch])

# Identify the best product in each branch
print("\nBEST PRODUCT IN EACH BRANCH")

for b in range(len(branches)):
    product_totals = []

    for p in range(len(products)):
        total = sum(sales[b][p])
        product_totals.append(total)

    best_product = product_totals.index(max(product_totals))

    print(branches[b], ":", products[best_product],
          "- Sales:", product_totals[best_product])
