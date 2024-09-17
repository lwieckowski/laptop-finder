from flask import Flask, render_template, request

from data import FILTERS, LAPTOPS, NAVLINKS
from filtering import apply_filters, apply_search, paginate, parse_form_data

app = Flask(__name__)

PER_PAGE = 20


@app.route("/")
def index():
    """Render the index page."""
    laptops = paginate(LAPTOPS, 1, PER_PAGE)
    return render_template(
        "index.jinja",
        laptops=laptops,
        navlinks=NAVLINKS,
        filters=FILTERS,
        page=1,
        per_page=PER_PAGE,
        total=len(LAPTOPS),
    )


@app.route("/laptops", methods=["GET", "POST"])
def filter():
    """Filter laptops by producer, screen size, and disk size and search term."""
    form_data = request.form.to_dict(flat=False)
    page = int(form_data.get("page", ["1"])[0])
    if not form_data:
        laptops = paginate(LAPTOPS, page, PER_PAGE)
        return render_template(
            "features/table_body.jinja",
            laptops=laptops,
            page=page,
            per_page=PER_PAGE,
            total=len(LAPTOPS),
        )
    form_data = parse_form_data(form_data)
    print(form_data.search_term)
    res = apply_filters(form_data.filters, LAPTOPS)
    res = apply_search(form_data.search_term, res)
    res_paged = paginate(res, page, PER_PAGE)
    return render_template(
        "features/table_body.jinja",
        laptops=res_paged,
        page=page,
        per_page=PER_PAGE,
        total=len(res),
    )


if __name__ == "__main__":
    app.run(debug=True)
