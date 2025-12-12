

# ⚡Final Project - Testing Automation

In this project we use **Pytest**, **Selenium WebDriver** & **Request** to test **SauceDemo** website and **Reqres** API applying **POM**, **HTML Reports**, **Auto-Screnshots** & **External Data Managment**.

## 🎯 Objective

This project automates repetitive tests to save time and resources, optimizing the following workflow:
- Login with valid and invalid credentials
- Verify the product catalog
- Interact with the cart: add products and verify content

## 🛠️ Technologies

- **Python 3.x**: Main programming language  
- **Pytest**: Testing framework to execute tests  
- **Selenium WebDriver**: Automates the web interface  
- **Git/GitHub**: Code sharing and version control  
- **Request**: 
- **Logging**:
- **Faker**:
- **CSV / JSON**:
- **Git/GitHub**:
- **GitHub Actions**:    

## 📁 Project Structure

```
📁 ENTREGA_FINAL_AUTOMATION/
│
├──📁 .github/                                      # Github folder
│   └──📁 workflows/                                # Workflows folder
│       └──📄 ci.yml                                # Config file
│
│
├──📁 data/                                         # Data folder
│   ├──📁 reqres/                                   # Reqres data folder
│   │  ├──📄 api.json                               # Api data
│   │  └──📄 payload.json                           # Payload data
│   │
│   └──📁 saucedemo/                                # Saucedemo data folder
│       ├──📄 links.json                            # Links data
│       ├──📄 login.csv                             # Users data
│       └──📄 products.json                         # Products data
│
│
├──📁 pages/                                        # Pages folder
│   ├──📄 cart_page.py                              # Cart page locators
│   ├──📄 inventory_page.py                         # Inventory page locators
│   └──📄 login_page.py                             # Login page locators
│
│
├──📁 reports/                                      # Reports folder (auto-generated)
│   └──📁 run_Y-M-D_h-m-s/                          # Test run folder (auto-generated)
│       │
│       ├──📁 assets/                               # CSS folder (auto-generated)
│       │   └──📄 style.css                         # CSS for report (auto-generated)
│       │
│       ├──📁 screenshots/                          # Screenshots folder (auto-generated)
│       │   └──📸 test_failed[user-password].png    # Screenshot of the fail (auto-generated)
│       │
│       └──📄 report.html                           # Test report (auto-generated)
│
│
├──📁 tests/                                        # Test cases folder
│   ├──📄 test_api.py                               # Run Reqres test
│   ├──📄 test_cart.py                              # Run cart page ui test
│   ├──📄 test_inventory.py                         # Run inventory page ui test
│   ├──📄 test_login_faker.py                       # Run login page ui test with faker func.
│   ├──📄 test_login.py                             # Run login page ui test
│   └──📄 test_screenshot.py                        # Run Screenshot functionality test (actually skipped)
│
│
├──📁 utils/                                        # Functions to avoid code repetition folder
│   ├──📄 helpers.py                                # Reutilizable functions
│   └──📄 logger.py                                 # Loggin function
│
│
├──📄 conftest.py                                   # Fixtures & Functions
├──📄 pytest.ini                                    # Pytest launch options
├──📄 README.md                                     # You are here 📌
└──📄 requirements.txt                              # Dependencies
```

## ⚙️ Dependencies Installation

- Install Python 3.x or newer.

Install dependencies:

```
pip install requirements.txt
```

## ▶️ To run the tests and generate a report, execute:

```
python -m run_test.py
```

## ✅ Test Functions

▶️ Automated login

- With valid credentials

- With invalid credentials

▶️ Automated login with Faker

- With valid credentials

- With invalid credentials

▶️ Catalog verification

- Page title

- Products verification

- Check page elements

▶️ Cart verification

- Add products

- Verify cart badge

- Navigate to cart

- Verify the product

▶️ API test (Reqres)

- GET users

- POST to create a user

- PUT to overwrite posted user

- PATCH to modify user

- DELETE to erase user.

- VALIDATE HTTP codes and JSON structure

## ✨ Additional Features

- 📜 HTML-Report: Create a HTML-Report with test info in:

```reports/run_Y-M-D_h_m_s/```

- 📷 Auto-screenshots: If a test fails, Selenium takes a screenshot of the error in:

```reports/run_Y-M-D_h_m_s/```

- 📋 Logger: Create a Log file with datailed info of the test run in:

```logs/suite.log```


## 👤 Author: Kalen Vota

## 📝 Notes
This project was designed using the SauceDemo & Reqres version available in December 2025.