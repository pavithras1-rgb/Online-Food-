# QuickBite – Online Food Ordering System

## 1. Project title and brief description
QuickBite is a beginner-friendly web application for ordering food online. Customers can browse a menu, filter food by category, add items to a cart, change quantities, enter delivery details and place a demo order. Orders are stored in a local SQLite database.

## 2. Problem statement and objectives
**Problem statement:** Ordering food through an unstructured manual process can make it difficult for customers to browse available items, calculate totals and keep order details together.

**Objectives:**
- Provide a simple digital food menu.
- Allow customers to add and remove items from a shopping cart.
- Calculate the order total automatically.
- Validate customer and delivery information.
- Save placed orders in a database.

## 3. Features/modules implemented
- Food menu with six sample items and category filters.
- Shopping cart with quantity controls and automatic total calculation.
- Checkout form with name, phone number and address validation.
- Order confirmation with a generated order number.
- Recent orders page showing the latest 20 orders.
- SQLite database storage.

## 4. Technology stack and tools used
- Python 3
- Flask (Python web framework)
- HTML5 and CSS3
- JavaScript
- SQLite
- Git and GitHub
- Visual Studio Code (recommended editor)

## 5. Prerequisites and installation steps
1. Install Python 3.10 or newer.
2. Install Git.
3. Extract the ZIP file.
4. Open a terminal in the `Food-Ordering-System` folder.
5. Create and activate a virtual environment:

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

6. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 6. Instructions to run the application
Run:
```bash
python app.py
```
Open the address shown in the terminal (normally `http://127.0.0.1:5000`) in a browser. The SQLite database is created automatically on the first run.

To stop the server, press `Ctrl+C` in the terminal.

## 7. Sample inputs and outputs
**Sample input**
- Customer name: Anu
- Phone number: 9876543210
- Delivery address: 12, Main Road, Coimbatore
- Cart: 1 Margherita Pizza (₹249) and 2 Masala Dosa (₹90 each)

**Expected output**
- Order confirmation page displays an order number.
- Order total: ₹429.
- The order appears on the Recent orders page.

## 8. Testing performed and results
Use this checklist during your local test and record the actual result before submission:

| Test case | Expected result |
|---|---|
| Open home page | Food menu is displayed |
| Filter by category | Only matching food cards are shown |
| Add food to cart | Cart count and total update |
| Increase/decrease quantity | Quantity and total update |
| Place order with valid details | Confirmation page and database record are created |
| Submit empty cart | Order is not accepted |
| Enter invalid phone number | Validation message is displayed |
| Open Recent orders | Saved orders are listed |

**Important:** Mark tests as Pass/Fail only after running them on your computer.

## 9. Team member details and individual contributions
Fill this section before submission.

| Name | Register number | Contribution |
|---|---|---|
| Student name | Register number | UI, application logic, testing and Git documentation |

For a team project, add every member and describe their genuine contribution.

## 10. Known limitations and possible future enhancements
**Limitations**
- Sample menu items are currently defined in the Python source code.
- This is a local demonstration; it does not send real delivery requests.
- No real payment gateway or user login is included.
- The application is intended for local academic demonstration, not public production deployment.

**Future enhancements**
- Add customer registration and login.
- Add an administrator page to manage food items.
- Add order status tracking.
- Integrate a secure payment gateway.
- Deploy the application online.

## Project folder structure
```text
Food-Ordering-System/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── success.html
│   └── orders.html
├── static/
│   ├── css/style.css
│   └── js/app.js
└── screenshots/
```

## Git and GitHub submission workflow
Run these commands from the project folder. Use meaningful commits as you develop; do not put all work into one final commit.

```bash
git init
git add README.md requirements.txt .gitignore
git commit -m "Add project documentation and setup"

git add app.py templates/
git commit -m "Build food menu and order routes"

git checkout -b feature-shopping-cart
git add static/
git commit -m "Add shopping cart and responsive styling"

git checkout main
git merge feature-shopping-cart

git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

If your default branch is named `master`, rename it to `main` before following the commands:
```bash
git branch -M main
```

After testing, make another commit for any fixes and documentation updates, then push:
```bash
git add .
git commit -m "Add test results and final documentation"
git push
```

Take screenshots of the running application, GitHub repository, commit history and feature branch merge for the faculty report. Follow the faculty's instruction for repository visibility and PDF naming.
