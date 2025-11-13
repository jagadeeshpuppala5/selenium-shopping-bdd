```markdown
# 🛍️ Selenium Shopping - BDD Automation Project

This project automates end-to-end test cases for [AutomationExercise](https://automationexercise.com/) using **Selenium**, **Behave (BDD Framework)**, and **Python**.  
It follows the **Page Object Model (POM)** design for better maintainability and readability.

---

## 🧩 Tech Stack
- **Language:** Python  
- **Automation Tool:** Selenium WebDriver  
- **Framework:** Behave (BDD)  
- **Design Pattern:** Page Object Model (POM)  
- **Reporting:** HTML Report (behave-html-formatter)  
- **Version Control:** Git & GitHub  
- **IDE:** VS Code / PyCharm  

---

## 📂 Project Folder Structure
```

Selenium_shopping/
│
├── features/
│   ├── login_valid.feature
│   ├── login_invalid.feature
│   └── environment.py
│
├── pages/
│   ├── Home_page.py
│   ├── Login_page.py
│   ├── Signup_page.py
│
├── steps/
│   ├── common_steps.py
│   ├── login_valid_steps.py
│   ├── login_invalid_steps.py
│
├── utilities/
│   ├── driver_setup.py
│   ├── common_utils.py
│
├── config/
│   └── config.json
│
├── reports/
│   ├── report.html
│   └── screenshots/
│
└── README.md

````

---

## ⚙️ Configuration File
`config/config.json`
```json
{
  "base_url": "https://automationexercise.com/",
  "user": {
    "name": "chinna",
    "email": "chinna@test.com",
    "password": "Test@123"
  }
}
````

---

## 🚀 How to Run Tests

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

*(Create `requirements.txt` with below libraries)*

```
behave
selenium
behave-html-formatter
```

---

### Step 2: Run test normally

```bash
behave
```

### Step 3: Run test with HTML Report

```bash
behave -f behave_html_formatter:HTMLFormatter -o reports/report.html
```

Then open:

```
reports/report.html
```

---

## 🧠 Scenarios Covered

### ✅ **Login with Valid Credentials**

* Navigate to home page
* Click **Signup/Login**
* Enter valid credentials
* Verify successful login as user

### ❌ **Login with Invalid Credentials**

* Navigate to home page
* Click **Signup/Login**
* Enter invalid credentials
* Verify error message “Your email or password is incorrect!”

---

## 🧰 Utilities

* **driver_setup.py:** Initializes and manages WebDriver
* **common_utils.py:** Handles screenshots on failure
* **environment.py:** Controls browser setup and teardown before/after scenarios

---

## 📸 Screenshots

All failed step screenshots will be saved in:

```
reports/screenshots/
```

---

## 👨‍💻 Author

**Chinna**
Python | Selenium | BDD | Playwright | API | Manual Testing
🔗 [GitHub Profile](https://github.com/yourusername)
📧 [your.email@example.com](mailto:your.email@example.com)

---

## 🌟 Future Enhancements

* Integrate Allure Report
* Parallel Execution setup
* Jenkins CI/CD pipeline integration
* Add more modules like Registration, Cart, Checkout

---

```
