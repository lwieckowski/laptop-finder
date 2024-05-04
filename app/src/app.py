from flask import Flask, render_template, request

from data import FILTERS, LAPTOPS, NAVLINKS
from filtering import apply_filters, apply_search, parse_form_data

app = Flask(__name__)


@app.route("/")
def index():
    """Render the index page."""
    return render_template(
        "index.jinja", laptops=LAPTOPS, navlinks=NAVLINKS, filters=FILTERS
    )


@app.route("/filter", methods=["POST"])
def filter():
    """Filter laptops by producer, screen size, and disk size and search term."""
    form_data = request.form.to_dict(flat=False)
    if not form_data:
        return render_template("features/table_body.jinja", laptops=LAPTOPS)
    form_data = parse_form_data(form_data)
    print(form_data.search_term)
    res = apply_filters(form_data.filters, LAPTOPS)
    res = apply_search(form_data.search_term, res)
    return render_template("features/table_body.jinja", laptops=res)


if __name__ == "__main__":
    app.run(debug=True)
