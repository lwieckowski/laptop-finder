from flask import Flask, render_template, request

from data import FILTERS, LAPTOPS, NAVLINKS

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.jinja", laptops=LAPTOPS, navlinks=NAVLINKS, filters=FILTERS
    )


@app.route("/filter", methods=["POST"])
def filter():
    form_data = request.form.to_dict(flat=False)
    if not form_data:
        return render_template("features/table_body.jinja", laptops=LAPTOPS)
    res = apply_filters(form_data, LAPTOPS)
    res = apply_search(form_data, res)
    return render_template("features/table_body.jinja", laptops=res)


def apply_search(filters, laptops):
    search_term = str(filters.get("search")[0]).strip()
    print(search_term)
    if not search_term:
        return laptops
    return [lap for lap in laptops if search_term.lower() in lap["model"].lower()]


def apply_filters(filters, laptops):
    prd = filters.get("producer")
    screen = filters.get("screen")
    disk = filters.get("disk")
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
