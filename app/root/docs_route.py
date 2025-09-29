from flask import Blueprint, current_app

docs_bp = Blueprint("docs", __name__)

@docs_bp.route("/docs", methods=["GET"])
def docs():
    rows = []
    for rule in current_app.url_map.iter_rules():
        if rule.endpoint == "static":
            continue
        methods = ",".join(sorted(m for m in rule.methods if m in {"GET","POST","PUT","PATCH","DELETE"}))
        rows.append((str(rule), methods))
    rows.sort()
    html = (
        "<h1>API endpoints</h1>"
        "<table border='1' cellpadding='6'><tr><th>Path</th><th>Methods</th></tr>"
        + "".join(f"<tr><td>{p}</td><td>{m}</td></tr>" for p, m in rows)
        + "</table>"
    )
    return html
