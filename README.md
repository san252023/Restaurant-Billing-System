# Restaurant-Billing-System


## Overview

This project is a Python-based command-line application that simulates a simple restaurant order system. It allows users to view a menu, place orders, apply discounts for students, add delivery charges, and include tips. The final bill is generated with all the details neatly formatted.

## Features

- **Menu Display:** The menu lists items with their corresponding prices in a user-friendly format.
- **Order Placement:** Users can select items from the menu and specify the quantity.
- **Student Discount:** A 20% discount is applied to the total order if the user is a student.
- **Delivery Option:** A 5% delivery charge is added if the user opts for delivery.
- **Tipping:** The user can choose to add a tip to the final bill.
- **Formatted Bill:** The final bill is displayed with clear alignment for easy reading.

## Code Highlights

- **Menu Listing:** Items are displayed with proper alignment using string formatting.
- **Order Logic:** The program handles user inputs for item selection, quantity, discounts, delivery, and tips.
- **Dynamic Pricing:** The total price is dynamically calculated based on the selected options.
- **Formatted Output:** The bill is printed with neat alignment, ensuring that prices, quantities, and totals are easy to read.

## How to Use

1. **Run the Program:** Execute the Python script in your command line.
2. **View the Menu:** The menu will be displayed with item numbers, names, and prices.
3. **Place Your Order:** Enter the number corresponding to the menu item, specify the quantity, and answer the prompts for student status, delivery, and tips.
4. **Review the Bill:** The final bill will be displayed with all charges, discounts, and tips applied.

## Example Output

```plaintext
Menu:
sr.  name           price
1.   aloo tikki       5$
2.   maharaja        10$
3.   mac special     15$

Enter the number of the item you want to order: 2
Enter the quantity: 3
Are you a student? (yes/no): yes
Do you want delivery (yes/no): yes
Do you want to give a tip? (yes/no): yes
Enter the tip amount (2/5/10): 5

******* Final Bill ********
sr.  name           price  quantity  total_price
1.   maharaja         10$   3        30$

------------------------------------------
                                 30$
Student discount 20%           -6.00$
Delivery charge 5%             +1.50$
Tip                            +5.00$
---------------------------------------
Total bill                     30.50$

## Requirements

- **Python 3.x:** This script is written in Python and requires Python 3.x to run.

## Contribution

Feel free to fork this repository and submit pull requests if you have improvements or additional features to suggest!

