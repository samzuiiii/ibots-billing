from flask import Flask, request, jsonify
from flask_cors import CORS
import pdfplumber
import os

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# ── Load catalog PDF on startup ────────────────────
# Just place any PDF named "catalog.pdf" in the project root
# If you want to use a different PDF, replace the file and restart

CATALOG_PATH = 'catalog.pdf'
catalog = []

def load_catalog():
    global catalog
    if not os.path.exists(CATALOG_PATH):
        print(f'[WARNING] {CATALOG_PATH} not found. Place your product PDF in the project root.')
        return

    products = []
    skip_words = {
        'product', 'name', 'item', 'description',
        'price', 'rate', 's.no', 'sno', 'sl', 'sr',
        'no', 'qty', 'quantity', 'total', 'amount', 'none'
    }

    with pdfplumber.open(CATALOG_PATH) as pdf:
        for page in pdf.pages:

            # ── Method 1: Table extraction ──
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    if not row:
                        continue
                    cells = [str(c).strip() for c in row if c and str(c).strip() and str(c).strip().lower() != 'none']
                    if len(cells) < 2:
                        continue

                    name  = None
                    price = None

                    for i in range(len(cells) - 1, -1, -1):
                        cleaned = cells[i].replace('₹','').replace('$','').replace(',','').strip()
                        try:
                            val = float(cleaned)
                            if val > 0:
                                price = val
                                for j in range(i - 1, -1, -1):
                                    t = cells[j].strip()
                                    if (t.lower() not in skip_words
                                            and not t.replace('.','').isdigit()
                                            and len(t) > 1):
                                        name = t
                                        break
                                break
                        except ValueError:
                            continue

                    if name and price:
                        if not any(p['name'].lower() == name.lower() for p in products):
                            products.append({'name': name, 'price': price})

            # ── Method 2: Line by line fallback ──
            if not products:
                text = page.extract_text()
                if not text:
                    continue
                for line in text.split('\n'):
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split()
                    if len(parts) < 2:
                        continue
                    last = parts[-1].replace('₹','').replace('$','').replace(',','')
                    try:
                        price = float(last)
                        if price <= 0:
                            continue
                        name_parts = parts[:-1]
                        if name_parts and name_parts[0].rstrip('.').isdigit():
                            name_parts = name_parts[1:]
                        name = ' '.join(name_parts).strip()
                        if name and name.lower() not in skip_words and len(name) > 1:
                            if not any(p['name'].lower() == name.lower() for p in products):
                                products.append({'name': name, 'price': price})
                    except ValueError:
                        continue

    catalog = products
    print(f'[OK] Loaded {len(catalog)} products from {CATALOG_PATH}')


# Load when server starts
load_catalog()


# ── Routes ─────────────────────────────────────────

@app.route('/')
def index():
    return app.send_static_file('index.html')


# Returns all products (called once when page loads)
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({'products': catalog, 'count': len(catalog)})


# Search products by name
@app.route('/search', methods=['GET'])
def search():
    q = request.args.get('q', '').strip().lower()
    if not q:
        return jsonify({'results': []})
    results = [p for p in catalog if q in p['name'].lower()]
    return jsonify({'results': results[:8]})


if __name__ == '__main__':
    app.run(debug=True, port=5000)