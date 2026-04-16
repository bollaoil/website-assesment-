from flask import Flask, render_template, request, redirect, url_for, session, send_file

app = Flask(__name__)
app.secret_key = "xcompany_secret"

USERNAME = "admin"
PASSWORD = "1234"

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        session["user"] = username
        return redirect(url_for("dashboard"))
    else:
        return render_template("login.html", error="Invalid credentials")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("dashboard.html")

@app.route("/reports")
def reports():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("reports.html")

@app.route("/download")
def download():
    if "user" not in session:
        return redirect(url_for("home"))
    return send_file("sample_report.csv", as_attachment=True)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)