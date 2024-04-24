from flask import Flask, render_template, request

from data import FILTERS, LAPTOPS, NAVLINKS

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.jinja", laptops=LAPTOPS, navlinks=NAVLINKS, filters=FILTERS
    )


@app.route("/search", methods=["POST"])
def search():
    search_term = str(request.form.get("search"))
    if not search_term:
        return render_template("features/table_body.jinja", laptops=LAPTOPS)
    res = [lap for lap in LAPTOPS if search_term.lower() in lap["model"].lower()]
    return render_template("features/table_body.jinja", laptops=res)


@app.route("/filter", methods=["POST"])
def filter():
    filters = request.form.to_dict(flat=False)
    if not filters:
        return render_template("features/table_body.jinja", laptops=LAPTOPS)
    res = apply_filters(filters, LAPTOPS)
    return render_template("features/table_body.jinja", laptops=res)


def apply_filters(filters, laptops):
    prd = filters.get("Producent")
    screen = filters.get("Ekran")
    disk = filters.get("Dysk")
    res = laptops
    if prd:
        res = [lap for lap in res if lap["producer"] in stripped(prd)]
    if screen:
        res = [lap for lap in res if lap["screen"] in stripped(screen)]
    if disk:
        res = [lap for lap in res if lap["disk"] in stripped(disk)]
    return res


def stripped(sequence):
    if sequence is None:
        return []
    return [s.strip() for s in sequence]


if __name__ == "__main__":
    app.run(debug=True)
