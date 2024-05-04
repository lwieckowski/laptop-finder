from model import Laptop


NAVLINKS = [
    {"text": "Do gier", "url": "/"},
    {"text": "Do pracy", "url": "/"},
    {"text": "Wszystkie", "url": "/"},
]
FILTERS = [
    {
        "type": "producer",
        "label": "Producent",
        "options": [
            {"label": "Apple", "value": "Apple"},
            {"label": "Dell", "value": "Dell"},
            {"label": "HP", "value": "HP"},
            {"label": "Lenovo", "value": "Lenovo"},
            {"label": "Asus", "value": "Asus"},
            {"label": "Microsoft", "value": "Microsoft"},
            {"label": "Acer", "value": "Acer"},
            {"label": "Razer", "value": "Razer"},
            {"label": "MSI", "value": "MSI"},
            {"label": "Gigabyte", "value": "Gigabyte"},
        ],
    },
    {
        "type": "screen",
        "label": "Ekran",
        "options": [
            {"label": "13.1", "value": "13.1"},
            {"label": "13.4", "value": "13.4"},
            {"label": "13.3", "value": "13.3"},
            {"label": "14", "value": "14"},
            {"label": "15.6", "value": "15.6"},
        ],
    },
    {
        "type": "disk",
        "label": "Dysk",
        "options": [
            {"label": "128GB", "value": "128GB"},
            {"label": "256GB", "value": "256GB"},
            {"label": "512GB", "value": "512GB"},
            {"label": "1TB", "value": "1TB"},
        ],
    },
]

LAPTOPS = tuple(
    [
        Laptop(
            model="MacBook Pro 13 M1",
            screen="13.3",
            disk="256GB",
            ram="8GB",
            weight="1.4",
            performance="5",
            price="5999",
            producer="Apple",
        ),
        Laptop(
            model="Dell XPS 13",
            screen="13.4",
            disk="512GB",
            ram="16GB",
            weight="1.2",
            performance="4",
            price="5999",
            producer="Dell",
        ),
        Laptop(
            model="HP Spectre x360",
            screen="13.3",
            disk="512GB",
            ram="16GB",
            weight="1.3",
            performance="4",
            price="5999",
            producer="HP",
        ),
        Laptop(
            model="Lenovo ThinkPad X1 Carbon",
            screen="14",
            disk="512GB",
            ram="16GB",
            weight="1.1",
            performance="4",
            price="5999",
            producer="Lenovo",
        ),
        Laptop(
            model="Asus ZenBook 14",
            screen="14",
            disk="512GB",
            ram="16GB",
            weight="1.2",
            performance="4",
            price="5999",
            producer="Asus",
        ),
        Laptop(
            model="Microsoft Surface Laptop 4",
            screen="13.5",
            disk="512GB",
            ram="16GB",
            weight="1.3",
            performance="4",
            price="5999",
            producer="Microsoft",
        ),
        Laptop(
            model="Acer Swift 5",
            screen="14",
            disk="512GB",
            ram="16GB",
            weight="1",
            performance="4",
            price="5999",
            producer="Acer",
        ),
        Laptop(
            model="Razer Blade Stealth 13",
            screen="13.3",
            disk="512GB",
            ram="16GB",
            weight="1.4",
            performance="5",
            price="5999",
            producer="Razer",
        ),
        Laptop(
            model="MSI Prestige 14",
            screen="14",
            disk="512GB",
            ram="16GB",
            weight="1.3",
            performance="4",
            price="5999",
            producer="MSI",
        ),
        Laptop(
            model="Gigabyte Aero 15",
            screen="15.6",
            disk="512GB",
            ram="16GB",
            weight="2",
            performance="5",
            price="5999",
            producer="Gigabyte",
        ),
        Laptop(
            model="MacBook Pro 16",
            screen="16",
            disk="512GB",
            ram="16GB",
            weight="2",
            performance="5",
            price="9999",
            producer="Apple",
        ),
        Laptop(
            model="Dell XPS 15",
            screen="15.6",
            disk="1TB",
            ram="32GB",
            weight="2",
            performance="5",
            price="9999",
            producer="Dell",
        ),
        Laptop(
            model="HP Spectre x360 15",
            screen="15.6",
            disk="1TB",
            ram="32GB",
            weight="2",
            performance="5",
            price="9999",
            producer="HP",
        ),
        Laptop(
            model="Lenovo ThinkPad X1 Extreme",
            screen="15.6",
            disk="1TB",
            ram="32GB",
            weight="2",
            performance="5",
            price="9999",
            producer="Lenovo",
        ),
        Laptop(
            model="Asus ZenBook Pro Duo",
            screen="15.6",
            disk="1TB",
            ram="32GB",
            weight="2",
            performance="5",
            price="9999",
            producer="Asus",
        ),
        Laptop(
            model="Microsoft Surface Book 3",
            screen="15",
            disk="1TB",
            ram="32GB",
            weight="2",
            performance="5",
            price="9999",
            producer="Microsoft",
        ),
        Laptop(
            model="Acer Predator Helios 300",
            screen="15.6",
            disk="1TB",
            ram="32GB",
            weight="2",
            performance="5",
            price="9999",
            producer="Acer",
        ),
    ]
)


if __name__ == "__main__":
    a = LAPTOPS * 10
    print()
