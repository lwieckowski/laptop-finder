from flask import Flask, render_template, request

app = Flask(__name__)


NAVLINKS = [
    {"text": "Do gier", "url": "/"},
    {"text": "Do pracy", "url": "/"},
    {"text": "Wszystkie", "url": "/"},
]
LAPTOPS = [
    {
        "model": "Apple MacBook Air",
        "screen": "13.1",
        "disk": "128GB",
        "ram": "8GB",
        "weight": "2.5kg",
        "performance": "97%",
        "price": "4825PLN",
    },
    {
        "model": "Dell XPS 13",
        "screen": "13.4",
        "disk": "256GB",
        "ram": "16GB",
        "weight": "1.27kg",
        "performance": "95%",
        "price": "5899PLN",
    },
    {
        "model": "HP Spectre x360",
        "screen": "13.3",
        "disk": "512GB",
        "ram": "16GB",
        "weight": "1.27kg",
        "performance": "92%",
        "price": "6499PLN",
    },
    {
        "model": "Lenovo ThinkPad X1 Carbon",
        "screen": "14",
        "disk": "512GB",
        "ram": "16GB",
        "weight": "1.09kg",
        "performance": "90%",
        "price": "6999PLN",
    },
    {
        "model": "Asus ROG Zephyrus G14",
        "screen": "14",
        "disk": "1TB",
        "ram": "16GB",
        "weight": "1.6kg",
        "performance": "95%",
        "price": "7499PLN",
    },
    {
        "model": "Microsoft Surface Laptop 4",
        "screen": "13.5",
        "disk": "512GB",
        "ram": "16GB",
        "weight": "1.26kg",
        "performance": "93%",
        "price": "7999PLN",
    },
    {
        "model": "Acer Predator Helios 300",
        "screen": "15.6",
        "disk": "1TB",
        "ram": "16GB",
        "weight": "2.3kg",
        "performance": "96%",
        "price": "8499PLN",
    },
    {
        "model": "Razer Blade 15",
        "screen": "15.6",
        "disk": "512GB",
        "ram": "16GB",
        "weight": "2.09kg",
        "performance": "94%",
        "price": "8999PLN",
    },
    {
        "model": "MSI GS66 Stealth",
        "screen": "15.6",
        "disk": "1TB",
        "ram": "32GB",
        "weight": "2.1kg",
        "performance": "98%",
        "price": "9499PLN",
    },
    {
        "model": "Gigabyte Aero 15 OLED",
        "screen": "15.6",
        "disk": "1TB",
        "ram": "32GB",
        "weight": "2.2kg",
        "performance": "97%",
        "price": "9999PLN",
    },
    {
        "model": "HP Pavilion 15",
        "screen": "15.6",
        "disk": "512GB",
        "ram": "16GB",
        "weight": "1.85kg",
        "performance": "90%",
        "price": "4299PLN",
    },
    {
        "model": "Lenovo IdeaPad 5",
        "screen": "14",
        "disk": "256GB",
        "ram": "8GB",
        "weight": "1.6kg",
        "performance": "88%",
        "price": "3499PLN",
    },
    {
        "model": "Dell Inspiron 15",
        "screen": "15.6",
        "disk": "1TB",
        "ram": "8GB",
        "weight": "2.2kg",
        "performance": "85%",
        "price": "3799PLN",
    },
    {
        "model": "Asus VivoBook 15",
        "screen": "15.6",
        "disk": "512GB",
        "ram": "8GB",
        "weight": "1.8kg",
        "performance": "86%",
        "price": "2999PLN",
    },
    {
        "model": "Acer Swift 3",
        "screen": "14",
        "disk": "256GB",
        "ram": "8GB",
        "weight": "1.5kg",
        "performance": "89%",
        "price": "3799PLN",
    },
    {
        "model": "MSI Modern 14",
        "screen": "14",
        "disk": "512GB",
        "ram": "16GB",
        "weight": "1.3kg",
        "performance": "92%",
        "price": "4499PLN",
    },
    {
        "model": "HP Envy x360",
        "screen": "15.6",
        "disk": "1TB",
        "ram": "16GB",
        "weight": "2.1kg",
        "performance": "91%",
        "price": "5499PLN",
    },
    {
        "model": "Lenovo Legion 5",
        "screen": "15.6",
        "disk": "512GB",
        "ram": "16GB",
        "weight": "2.3kg",
        "performance": "93%",
        "price": "5799PLN",
    },
    {
        "model": "Dell G5 15",
        "screen": "15.6",
        "disk": "1TB",
        "ram": "16GB",
        "weight": "2.68kg",
        "performance": "88%",
        "price": "6499PLN",
    },
    {
        "model": "Asus TUF Gaming A15",
        "screen": "15.6",
        "disk": "512GB",
        "ram": "16GB",
        "weight": "2.3kg",
        "performance": "90%",
        "price": "5799PLN",
    },
    {
        "model": "Acer Nitro 5",
        "screen": "15.6",
        "disk": "1TB",
        "ram": "16GB",
        "weight": "2.3kg",
        "performance": "89%",
        "price": "5999PLN",
    },
    {
        "model": "HP EliteBook 840 G8",
        "screen": "14",
        "disk": "512GB",
        "ram": "16GB",
        "weight": "1.33kg",
        "performance": "95%",
        "price": "7499PLN",
    },
    {
        "model": "Lenovo Yoga C940",
        "screen": "14",
        "disk": "1TB",
        "ram": "16GB",
        "weight": "1.35kg",
        "performance": "92%",
        "price": "7999PLN",
    },
    {
        "model": "Dell Precision 5550",
        "screen": "15.6",
        "disk": "1TB",
        "ram": "32GB",
        "weight": "1.84kg",
        "performance": "98%",
        "price": "9999PLN",
    },
    {
        "model": "Asus ZenBook Pro Duo",
        "screen": "15.6",
        "disk": "1TB",
        "ram": "32GB",
        "weight": "2.5kg",
        "performance": "97%",
        "price": "10999PLN",
    },
    {
        "model": "MSI Prestige 14",
        "screen": "14",
        "disk": "512GB",
        "ram": "16GB",
        "weight": "1.29kg",
        "performance": "93%",
        "price": "4999PLN",
    },
    {
        "model": "HP Omen 15",
        "screen": "15.6",
        "disk": "1TB",
        "ram": "16GB",
        "weight": "2.36kg",
        "performance": "90%",
        "price": "6499PLN",
    },
    {
        "model": "Lenovo ThinkBook 14",
        "screen": "14",
        "disk": "512GB",
        "ram": "16GB",
        "weight": "1.5kg",
        "performance": "92%",
        "price": "4499PLN",
    },
    {
        "model": "New Laptop 1",
        "screen": "15.6",
        "disk": "1TB",
        "ram": "16GB",
        "weight": "2.2kg",
        "performance": "95%",
        "price": "7999PLN",
    },
    {
        "model": "New Laptop 2",
        "screen": "14",
        "disk": "512GB",
        "ram": "16GB",
        "weight": "1.3kg",
        "performance": "94%",
        "price": "6999PLN",
    },
    {
        "model": "New Laptop 3",
        "screen": "15.6",
        "disk": "1TB",
        "ram": "32GB",
        "weight": "2.1kg",
        "performance": "98%",
        "price": "8999PLN",
    },
    {
        "model": "New Laptop 4",
        "screen": "14",
        "disk": "1TB",
        "ram": "32GB",
        "weight": "2.2kg",
        "performance": "97%",
        "price": "9999PLN",
    },
    {
        "model": "New Laptop 5",
        "screen": "15.6",
        "disk": "512GB",
        "ram": "16GB",
        "weight": "2.3kg",
        "performance": "90%",
        "price": "5499PLN",
    },
    {
        "model": "New Laptop 6",
        "screen": "14",
        "disk": "256GB",
        "ram": "8GB",
        "weight": "1.6kg",
        "performance": "88%",
        "price": "3799PLN",
    },
    {
        "model": "New Laptop 7",
        "screen": "15.6",
        "disk": "1TB",
        "ram": "8GB",
        "weight": "2.2kg",
        "performance": "85%",
        "price": "4299PLN",
    },
    {
        "model": "New Laptop 8",
        "screen": "15.6",
        "disk": "512GB",
        "ram": "8GB",
        "weight": "1.8kg",
        "performance": "86%",
        "price": "2999PLN",
    },
    {
        "model": "New Laptop 9",
        "screen": "14",
        "disk": "256GB",
        "ram": "8GB",
        "weight": "1.5kg",
        "performance": "89%",
        "price": "3799PLN",
    },
    {
        "model": "New Laptop 10",
        "screen": "14",
        "disk": "512GB",
        "ram": "16GB",
        "weight": "1.3kg",
        "performance": "92%",
        "price": "4499PLN",
    },
]


@app.route("/")
def index():
    return render_template("index.jinja", laptops=LAPTOPS, navlinks=NAVLINKS)

@app.route("/search", methods=["POST"])
def search():
    search_term = str(request.form.get("search"))
    if not search_term:
        return render_template("features/table_body.jinja", laptops=LAPTOPS)
    res = [lap for lap in LAPTOPS if search_term.lower() in lap["model"].lower()]
    return render_template("features/table_body.jinja", laptops=res)
