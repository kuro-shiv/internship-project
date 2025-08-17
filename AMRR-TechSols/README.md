# AMRR TechSols – Item Listing Web App

This is a simple two-page web application developed for the AMRR TechSols internship assignment. The application allows users to add new items and view all submitted items with detailed information.

## 🔗 Live Demo

[GitHub Repository](https://github.com/kuro-shiv/AMRR-TechSols/tree/master)

[Hosted URL](https://23rrd7-3000.csb.app/index.html)

---

## 📄 Features

### 📥 Add Item Page (`Add Items`)
- Allows user to submit:
  - **Item Name**

  - **Item Type** (e.g., Shirt, Pant, Shoes, Sports Gear, etc.)
  - **Item Description**
  - **Cover Image**
  - **Additional Images**
- Displays a success message:  
  ✅ `Item successfully added` on successful submission.

### 👁️ View Items Page (`View Items`)
- Lists all items with:
  - **Item Name**
  - **Cover Image**
- Clicking on any item opens a **modal/lightbox** with:
  - Full **item description**
  - All **images displayed in a carousel**

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap (for modal & carousel)
- **Backend**: Node.js with Express *(Optional enhancement: can use localStorage or JSON for static simulation)*
- **Storage**: Currently uses a temporary in-memory/static list *(can be upgraded to a database)*

---

## 📁 Project Structure


![Screenshot 2025-06-22 033111](https://github.com/user-attachments/assets/ebcd0e30-1ab5-4ee9-9ad8-5a3a5f1f8192)



AMRR-TechSols/


index.html              # View Items page

add.html               # Add Items page

item-detail.html

CSS

JS

node_modules

server.js              # Express server (optional)

item.json

package.json              # JSON storage (optional enhancement)

package-lock.json 

README.md              # Project documentation



---

## 📦 How to Run Locally

1. Clone the repository:
      git clone https://github.com/kuro-shiv/AMRR-TechSols.git
   
      cd AMRR-TechSols

3. If it's a static project (HTML/CSS/JS only):
   Open index.html (View Items page) or add.html (Add Items page) directly in your browser. Or run a local server using Python:

      python -m http.server 8000

   Then visit:

      http://localhost:8000

4. If using Node.js/Express backend:

  * Install dependencies:
    
       npm install

  * Start the server:
    
       npm start

  * Open your browser and go to:
    
      http://localhost:3000



---
## 📜 License

&copy; 2025 Shivam Kumar Dubey. All rights reserved.


---
## 👨‍💻 Author

Shivam Dubey

GitHub: @kuro-shiv

Project submitted as part of the AMRR TechSols Internship Assignment
