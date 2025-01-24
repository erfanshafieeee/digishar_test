# Demoblaze Testing Report

## Introduction
### Website Overview: Demoblaze
1. **Website URL**: [https://www.demoblaze.com/index.html](https://www.demoblaze.com/index.html)  
2. **Purpose of the Website**:
   - Demoblaze is a simple online store showcasing various products such as laptops, phones, and other electronic devices.
3. **Key Features of the Website**:
   - Homepage displays a list of products with images, names, and prices.
   - Ability to add products to a shopping cart.
   - Separate pages to view product details.
   - User account registration and login functionality.
   - Ability to place orders.
   - Contact functionality for user inquiries.
4. **Testing Objectives**:
   - Functional evaluation, UI/UX assessment, and security analysis.
5. **Testing Tools Used**:
   - Web browsers: Chrome, Firefox, Edge (desktop and mobile modes).
   - Automation tools: Selenium.

---

## Bug Identification
To streamline the improvement process, the identified bugs have been categorized into **functional**, **UI**, and **security** issues.

### Functional Bugs
#### **Bug 1:** Additional product images are not displayed
- **Description:** When viewing a product's details, other product images are not displayed.
- **Steps to Reproduce:**
  1. Open the website.
  2. Click on a product.
  3. Try clicking on other product images.

#### **Bug 2:** Purchase without adding any products
- **Description:** Users can proceed with a purchase without adding any products to the cart.
- **Steps to Reproduce:**
  1. Open the website.
  2. Click on the "Cart" button.
  3. Click on "Place Order."
  4. Fill in the required details.
  5. Click on "Purchase."

#### **Bug 3:** Date inconsistency in the "Place Order" form
- **Description:** The entered date is ignored, and a fixed incorrect date (e.g., `24/0/2025`) is displayed.
- **Steps to Reproduce:**
  1. Open the website.
  2. Click on the "Cart" button.
  3. Click on "Place Order."
  4. Enter the required details and an invalid date.
  5. Click "Purchase."

#### **Bug 4:** 404 error on URL modification
- **Description:** Adding any text to the URL results in a 404 error with no navigation option back to the site.
- **Steps to Reproduce:**
  1. Open [https://www.demoblaze.com/](https://www.demoblaze.com/).
  2. Append any text (e.g., `/test`) to the URL.

#### **Bug 5:** Console error notification
- **Description:** When the console is opened in Chrome, the following error appears:

```
VIDEOJS: WARN: A plugin named "reloadSourceOnError" already exists.
(anonymous) @ video.min.js:12
...
```
- **Steps to Reproduce:**
  1. Open the website.
  2. Open the developer tools (F12).
  3. Check the "Console" tab.

---

### UI Bugs
#### **Bug 6:** Oversized username and password fields in mobile view
- **Description:** The fields in the "Sign up" form are larger than the form size in mobile view.
- **Steps to Reproduce:**
  1. Open the website in mobile view.
  2. Click on "Sign up."

#### **Bug 7:** Duplicate product details
- **Description:** Some product details, such as those for "Sony Vivo i7," are identical to another product (e.g., "Sony Vivo i5").
- **Steps to Reproduce:**
  1. Open the website.
  2. Locate "Sony Vivo i7" in the laptop section.
  3. Compare details with "Sony Vivo i5."

#### **Bug 8:** Oversized video in mobile view
- **Description:** The "About Us" section video exceeds the screen size in mobile view.
- **Steps to Reproduce:**
  1. Open the website in mobile view.
  2. Navigate to the "About Us" section.

#### **Bug 9:** Oversized fields in the "Contact" form
- **Description:** Fields like "Contact Email" and "Contact Name" are larger than the form in mobile view.
- **Steps to Reproduce:**
  1. Open the website in mobile view.
  2. Click on "Contact."

#### **Bug 10:** Poor UI in the "Cart" section (mobile view)
- **Description:** Text and buttons in the "Cart" section, especially "Log in" and "Sign up," are not user-friendly in mobile view.
- **Steps to Reproduce:**
  1. Open the website in mobile view.
  2. Go to the "Cart" section.

#### **Bug 11:** Oversized fields in the "Place Order" form
- **Description:** All fields in the "Place Order" form are oversized in mobile view.
- **Steps to Reproduce:**
  1. Open the website in mobile view.
  2. Go to the "Cart" section.
  3. Click on "Place Order."

#### **Bug 12:** Date format in "Place Order" form
- **Description:** The current date format is not user-friendly. Suggestions include:
   - Automatically filling the date if it’s always today.
   - Providing a date picker for manual selection.

#### **Bug 13:** Purchase without login
- **Description:** Users can complete a purchase without logging in.
- **Steps to Reproduce:**
  1. Open the website.
  2. Add a product to the cart.
  3. Go to the "Cart" section and click on "Place Order."
  4. Complete the purchase form and click "Purchase."

---

### Security Bugs
#### **Bug 14:** Logging in as Admin
- **Description:** It is possible to log in as an admin with the credentials `Username: admin` and `Password: admin`.
- **Steps to Reproduce:**
  1. Open the website.
  2. Click on "Log in."
  3. Enter `admin` for both username and password.
  4. Click on "Log in."

---

## Test Plan
### Objectives
- Identify and report functional, UI, and security issues on the website.

### Scope
Includes:
- Homepage functionality
- User registration and login
- Adding products to the cart
- Purchase workflow
- Contact form functionality

Excludes:
- Server-side functionality
- Backend performance tests

### Test Strategy
- **Manual Testing:**
  - Exploratory and intuitive testing for detailed UI inspection.
  - Black-box techniques like equivalence partitioning and decision tables.
- **Automated Testing:**
  - Selenium for repetitive tasks.

### Tools
- Selenium
- Chrome (desktop and mobile modes)
- Firefox (desktop and mobile modes)
- Edge

### Success/Failure Criteria
- Registration form accepts only valid inputs.
- Purchase workflow works seamlessly across browsers.
- Contact form successfully sends messages.
- Login functionality works correctly with valid credentials.

### Deliverables
- Bug reports
- Test case documentation
- Overall site performance report

---

## Test Cases
### **Test Case 1: Add to Cart Button**
- **Objective:** Verify the functionality of the "Add to Cart" button.
- **Preconditions:** Browser is open, and the website is loaded.
- **Steps:**
  1. Navigate to the website.
  2. Select a product.
  3. Click on "Add to Cart."
- **Expected Result:** A message "Product added" is displayed, and the product is added to the cart.

### **Test Case 2: User Registration**
- **Objective:** Verify the "Sign up" form functionality.
- **Preconditions:** A unique email address is available.
- **Steps:**
  1. Click on "Sign up."
  2. Enter user details.
  3. Submit the form.
- **Expected Result:** A success message confirming registration is displayed.

### **Test Case 3: User Login**
- **Objective:** Verify the login functionality.
- **Preconditions:** A valid user account exists.
- **Steps:**
  1. Click on "Log in."
  2. Enter valid credentials.
  3. Click "Log in."
- **Expected Result:** User is logged in, and their username is displayed on the homepage.

### **Test Case 4: Remove from Cart**
- **Objective:** Verify the functionality of the "Delete" button in the cart.
- **Preconditions:** A product is added to the cart.
- **Steps:**
  1. Go to the "Cart" section.
  2. Click "Delete" next to a product.
- **Expected Result:** Product is removed from the cart, and the total price is updated.

### **Test Case 5: 404 Error Page**
- **Objective:** Verify the 404 error handling.
- **Preconditions:** Browser is open.
- **Steps:**
  1. Append random text to the website URL (e.g., `/test`).
- **Expected Result:** A 404 error is displayed with a button to return to the homepage.

### **Test Case 6: Logout**
- **Objective:** Verify the "Log out" functionality.
- **Preconditions:** User is logged in.
- **Steps:**
  1. Click on "Log out."
- **Expected Result:** User is logged out, and the "Log in" button is displayed.
