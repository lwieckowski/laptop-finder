from functools import cache
from model import Laptop
from model import Filters, FormData


def parse_form_data(form_data: dict[str, list[str]]) -> FormData:
    """Parse form data."""
    return FormData(
        filters=Filters(
            *(
                parse_filter(form_data, filter_name)
                for filter_name in Filters.__annotations__
            )
        ),
        search_term=form_data.get("search", [""])[0],
    )


def parse_filter(filters: dict[str, list[str]], filter_name: str) -> tuple[str, ...]:
    """Parse a filter by name."""
    return tuple(stripped(filters.get(filter_name, [])))


@cache
def apply_filters(filters: Filters, laptops: tuple[Laptop, ...]) -> tuple[Laptop, ...]:
    """Filter laptops by producer, screen size, and disk size."""
    filtered_laptops = laptops
    for filter_name in filters.__dict__:
        filter_values = getattr(filters, filter_name)
        if filter_values:
            filtered_laptops = apply_filter(
                filter_values, filter_name, filtered_laptops
            )
    return tuple(filtered_laptops)


@cache
def apply_search(search_term: str, laptops: tuple[Laptop, ...]) -> tuple[Laptop, ...]:
    """Filter laptops by search term."""
    if not search_term:
        return laptops
    return tuple(lap for lap in laptops if search_term.lower() in lap.model.lower())


@cache
def apply_filter(
    filter_values: tuple[str, ...], filter_name: str, laptops: tuple[Laptop, ...]
) -> tuple[Laptop, ...]:
    """Filter laptops by a given field."""
    if not filter_values:
        return laptops
    return tuple(lap for lap in laptops if getattr(lap, filter_name) in filter_values)


def stripped(sequence: list[str]) -> list[str]:
    """Strip whitespace from a list of strings."""
    if sequence is None:
        return []
    return [s.strip() for s in sequence]


def paginate(
    laptops: tuple[Laptop, ...], page: int, per_page: int
) -> tuple[Laptop, ...]:
    """Paginate laptops."""
    start = (page - 1) * per_page
    end = start + per_page
    return laptops[start:end]
