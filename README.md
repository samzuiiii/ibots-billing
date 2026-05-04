# Billing System

A professional full-stack billing application built for **iBots Technology Solutions, Coimbatore**. Enables fast invoice generation with automatic product lookup from a PDF catalog, manual entry support, GST calculation, and print-to-PDF output.

---

## Features

- **PDF Catalog Integration** — Reads any product catalog PDF automatically on server startup using pdfplumber
- **Live Product Search** — Real-time search with instant suggestions as you type, matched text highlighted in blue
- **Manual Entry** — Add any product not in the catalog with a custom name and price
- **Auto GST Calculation** — Subtotal, 18% GST and grand total calculated automatically
- **Professional Invoice** — Print a fully formatted, branded invoice as PDF with one click
- **Live Clock** — Bill ID, date and time auto-generated on every session
- **Any PDF Support** — Replace the catalog PDF and restart the server, no code changes needed

---

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Backend | Python + Flask | REST API server |
| PDF Parsing | pdfplumber | Extract products from PDF catalog |
| Frontend | HTML + CSS + JavaScript | User interface |
| API Communication | Fetch API | Browser to server communication |
| Print | Blob URL + window.print() | Generate formatted PDF invoices |

---

## Project Structure
ibots-billing/
├── app.py                 # Flask backend server
├── catalog.pdf            # Product catalog — replace to update
├── requirements.txt       # Python dependencies
├── uploads/               # PDF storage
└── static/
└── index.html       # Frontend application

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/samzuiiii/ibots-billing.git
cd ibots-billing
```

**2. Install dependencies**
```bash
pip install flask flask-cors pdfplumber
```

**3. Add your product catalog**

Place your PDF in the root folder and rename it to `catalog.pdf`

**4. Run the server**
```bash
python app.py
```

**5. Open in browser**
http://localhost:5000
---

## How It Works

**1. Server Startup**
When `python app.py` runs, Flask reads `catalog.pdf` using pdfplumber, extracts all product names and prices, and stores them in memory. The terminal confirms how many products were loaded.

**2. Page Load**
The browser calls the `/products` API on load. The green status bar confirms the catalog is ready with the product count.

**3. Product Search**
As the user types, JavaScript filters the in-memory product list instantly — no extra server calls. Matched characters are highlighted in blue in the dropdown.

**4. Adding Products**
- From catalog → click a suggestion, price is auto-filled
- Not in catalog → click Add Manually, enter name and price

**5. Bill Generation**
Quantities adjusted with + / − controls. Subtotal, GST (18%) and total update live. Print Bill opens a formatted invoice in a new tab and triggers the browser print dialog.

**6. Updating the Catalog**
Replace `catalog.pdf` → restart server → new products load automatically.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Serves the frontend |
| GET | `/products` | Returns full product list from catalog |
| GET | `/search?q=query` | Returns filtered products matching query |

---

## Built With

- [Flask](https://flask.palletsprojects.com/) — Python web framework
- [pdfplumber](https://github.com/jsvine/pdfplumber) — PDF extraction
- [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans) — UI typography

---


