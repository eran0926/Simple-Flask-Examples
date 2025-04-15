from flask import Flask, request, send_file, render_template

app = Flask(__name__)


@app.route("/send_file")  # This is unsafe
def a():
    file_name = request.args.get("file", "index.html")
    return send_file(file_name)


@app.route("/render_template")  # This is safe
def b():
    template_name = request.args.get("page", "index.html")
    return render_template(template_name)
