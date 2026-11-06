# Restaurant Sales Dashboard

**PS No:** 85
**Project Title:** Restaurant Sales Dashboard
**University:** Rungta International Skills University, School of Information Technology
**Course:** Bachelor of Computer Application

## Problem Statement
Read restaurant_sales.csv with Pandas. Sales = Quantity x Price.
Use GroupBy to show sales by category, by date and the top item
by quantity and by revenue, with charts. Skip invalid rows.

**Language:** Python 3
**Concepts:** Pandas, Matplotlib, CSV, GroupBy

**Sample Data (5 columns, 8 rows):**
Date, Item, Category, Quantity, Price

## Test Cases / Case Statements (4 cases)

### Test Case 1: Normal Input
File: restaurant_sales.csv
Expected Output:
- Main : Rs. 6300
- Starter : Rs. 4840
- Dessert : Rs. 3600
- Total sales: Rs. 14740
Result: PASSED

### Test Case 2: Boundary / Minimum Input
File: 2026-10-01, Paneer Tikka, Starter, 1, 220
Expected Output:
- Total sales: Rs. 220
- Top item by quantity: Paneer Tikka (1 unit)
- Top item by revenue: Paneer Tikka (Rs. 220)
Result: PASSED

### Test Case 3: Invalid Input
(a) Extra row in file: 2026-10-03, Lassi, Drink, five, 60
(b) File: sales2025.csv (does not exist)
Expected Output:
(a) Warning: Row 8 skipped - Quantity must be a number
(b) Error: File 'sales2025.csv' not found
Result: PASSED

### Test Case 4: Different Scenario
File: restaurant_sales.csv
Menu: Top items and daily sales
Expected Output:
- Top item by quantity: Gulab Jamun (45 units)
- Top item by revenue: Paneer Tikka (Rs. 4840)
- 2026-10-01 : Rs. 7700
- 2026-10-02 : Rs. 7040
- Best day: 2026-10-01
Result: PASSED

## Bare Minimum Requirements
1. Write the solution in Python 3 (one.py file) and run it from the console.
2. Load the CSV with Pandas and compute Sales (Quantity x Price).
3. Skip invalid rows and handle a missing file.
4. Use GroupBy to total sales by category, item and date.
5. Test the program with all four test cases.

## Files in this Repository
- `one.py` / `main.py` - Main Python code
- `restaurant_sales.csv` - Main data
- `one_row.csv` - Test Case 2 data
- `invalid.csv` - Test Case 3 data
- `Test_cases_passed.pdf` - Proof of all 4 test cases passed
- `PS_No_Screenshot.png` - Project Allocation Proof (PS No. 85)

## How to Run
py main.py