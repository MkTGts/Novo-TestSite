from flask import Flask, render_template, request

app = Flask(__name__)

PRODUCTS = [
    {"brand": "LB CERAMICS", "title": "Керамогранит · мат · 60×60", "type": "Керамогранит", "brand_key": "lb", "usage": "Пол", "format": "60×60", "surface": "Мат", "color": "Серый", "style": "Современный", "price": "от 1 299 ₽/м²", "stock": "В наличии", "swatch": "stone"},
    {"brand": "NEFRIT KERAMIKA", "title": "Плитка для стен · глянец · 60×120", "type": "Для стен", "brand_key": "nephrite", "usage": "Ванная", "format": "60×120", "surface": "Глянец", "color": "Светлый", "style": "Современный", "price": "от 1 074 ₽/м²", "stock": "Под заказ", "swatch": "marble"},
    {"brand": "AZORI CERAMICA", "title": "Керамогранит · структура · 120×20", "type": "Керамогранит", "brand_key": "azori", "usage": "Кухня", "format": "120×20", "surface": "Структура", "color": "Тёплый", "style": "Текстурный", "price": "от 1 650 ₽/м²", "stock": "Под заказ", "swatch": "wood"},
    {"brand": "GRACIA CERAMICA", "title": "Плитка для пола · мат · 60×60", "type": "Для пола", "brand_key": "gracia", "usage": "Пол", "format": "60×60", "surface": "Мат", "color": "Серый", "style": "Классический", "price": "Цена по запросу", "stock": "Под заказ", "swatch": "cement"},
    {"brand": "BELLEZA", "title": "Плитка для стен · мрамор · 30×90", "type": "Для стен", "brand_key": "belleza", "usage": "Ванная", "format": "30×90", "surface": "Глянец", "color": "Светлый", "style": "Классический", "price": "от 1 420 ₽/м²", "stock": "В наличии", "swatch": "marble"},
    {"brand": "LASSELSBERGER", "title": "Керамогранит · камень · 60×120", "type": "Керамогранит", "brand_key": "lb", "usage": "Кухня", "format": "60×120", "surface": "Мат", "color": "Серый", "style": "Современный", "price": "от 1 890 ₽/м²", "stock": "Под заказ", "swatch": "stone"},
    {"brand": "GRANIT", "title": "Плитка для пола · дерево · 20×120", "type": "Для пола", "brand_key": "gracia", "usage": "Кухня", "format": "20×120", "surface": "Структура", "color": "Тёплый", "style": "Текстурный", "price": "от 1 560 ₽/м²", "stock": "В наличии", "swatch": "wood"},
    {"brand": "Нефрит-Керамика", "title": "Плитка для стен · мат · 25×75", "type": "Для стен", "brand_key": "nephrite", "usage": "Ванная", "format": "25×75", "surface": "Мат", "color": "Светлый", "style": "Современный", "price": "от 990 ₽/м²", "stock": "Под заказ", "swatch": "cement"},
]

@app.get("/")
def index():
    return render_template("index.html", products=PRODUCTS, sent=request.args.get("sent") == "1")

@app.post("/booking")
def booking():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    if not name or not phone or request.form.get("consent") != "on":
        return render_template("index.html", products=PRODUCTS, error="Заполните имя и телефон и подтвердите согласие на обработку данных."), 400
    # This demo confirms the request without storing personal data or sending it anywhere.
    return render_template("index.html", products=PRODUCTS, sent=True)

if __name__ == "__main__":
    app.run(debug=True)
