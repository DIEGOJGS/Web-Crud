from flask import Flask, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Autenticación y conexión a Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/google.json", scope)
client = gspread.authorize(creds)

# Selecciona tu Google Sheet
sheet = client.open("DATA").sheet1

@app.route("/")
def index():
    # Extraer todos los datos de la hoja
    data = sheet.get_all_records()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
