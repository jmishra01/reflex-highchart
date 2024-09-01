# reflex-highchart

reflex-highcharts is a powerful component designed to integrate the popular charting library,
[Highcharts](https://www.highcharts.com), into your [Reflex](https://reflex.dev) web applications.
This integration allows you to create visually appealing and interactive charts with ease.

## Installation

```bash
pip install reflex-highchart
```

## Example

```python
import reflex as rx
from reflex_highchart import reflex_highchart


def highchart_example():
    return {
        "title": {
            "text": "Sales by Month"
        },
        "xAxis": {
            "title": {
                "text": "Month",
            },
            "categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        },
        "yAxis": {
            "title": {
                "text": "Total Sales"
            }
        },
        "series": [
            {"type": "column",
             "name": "Total Sales",
             "data": [
             [0, 30],
             [1, 17],
             [2, 20],
             [3, 12],
             [4, 23],
             [5, 14],
             [6, 16],
             [7, 19],
             [8, 22],
             [9, 13],
             [10, 16],
             [11, 15]
             ]}
        ]
    }

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            reflex_highchart(
                options=highchart_example(),
            )
        )
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
```
