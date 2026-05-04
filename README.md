Billing System
A professional, full-stack billing application built for iBots Technology Solutions, Coimbatore. Enables fast invoice generation with automatic product lookup from a PDF catalog, manual entry support, GST calculation, and print-to-PDF output.

Features

PDF Catalog Integration — Upload any product catalog PDF and the system automatically extracts product names and prices using pdfplumber
Live Product Search — Real-time search with instant suggestions as you type, with matched text highlighted
Manual Entry — Add any product not in the catalog with a custom name and price
Auto GST Calculation — Subtotal, 18% GST, and grand total calculated automatically
Professional Invoice — Print a formatted, branded invoice as PDF with one click
Live Clock — Bill date and time update in real time
Any PDF Support — Replace the catalog PDF and restart the server — no code changes needed


Tech Stack
LayerTechnologyPurposeBackendPython + FlaskREST API serverPDF ParsingpdfplumberExtract products from PDFFrontendHTML + CSS + JavaScriptUser interfaceAPI CommunicationFetch APIBrowser-to-server callsPrintBlob URL + window.print()Generate PDF invoices

Project Structure
ibots-billing/
├── app.py                 # Flask backend server
├── catalog.pdf            # Product catalog (replace to update)
├── requirements.txt       # Python dependencies
├── uploads/               # Uploaded PDF storage
└── static/
      └── index.html       # Frontend application

Getting Started
Prerequisites

Python 3.8 or higher
pip

Installation
1. Clone the repository
bashgit clone https://github.com/samzuiiii/ibots-billing.git
cd ibots-billing
2. Install dependencies
bashpip install flask flask-cors pdfplumber
3. Add your product catalog
Place your product catalog PDF in the root folder and name it catalog.pdf.
The PDF should contain product names and prices — table format or plain list both work.
4. Run the server
bashpython app.py
5. Open the app
Visit http://localhost:5000 in your browser.
You should see:
[OK] Loaded 90 products from catalog.pdf
Running on http://127.0.0.1:5000

How It Works
1. Server Startup
When python app.py runs, Flask reads catalog.pdf using pdfplumber. It extracts all product names and prices and stores them in memory. The terminal confirms how many products were loaded.
2. Page Load
The browser opens the billing interface and immediately calls the /products API endpoint. The green status bar confirms the catalog is ready.
3. Product Search
As the user types in the search box, JavaScript filters the in-memory product list and shows matching results instantly — no additional server calls needed. Matched characters are highlighted in blue.
4. Adding Products

From catalog — Click a suggestion to add it to the bill with price auto-filled
Manually — Click "Add Manually" to enter a custom product name and price

5. Bill Generation
Quantities can be adjusted with + / − controls. Subtotal, GST (18%) and total update automatically. Clicking "Print Bill as PDF" opens a formatted invoice in a new tab and triggers the browser print dialog.
6. Updating the Catalog
To use a different product catalog:

Replace catalog.pdf in the project root with the new PDF
Restart the server — Ctrl+C then python app.py
The new products load automatically


API Endpoints
MethodEndpointDescriptionGET/Serves the frontend applicationGET/productsReturns full product list from catalogGET/search?q=queryReturns filtered products matching query

Screenshots

Bill ID, date and time are auto-generated on every session.
The search bar provides instant suggestions from the loaded catalog.
The printed invoice includes the iBots logo, customer details, itemized products, GST breakdown and total.


Updating Prices
All prices are read directly from catalog.pdf. To update any price:

Edit the PDF catalog with the new prices
Replace catalog.pdf in the project folder
Restart the server


Built With

Flask — Python web framework
pdfplumber — PDF text and table extraction
Plus Jakarta Sans — UI typography
Google Fonts — Font delivery
