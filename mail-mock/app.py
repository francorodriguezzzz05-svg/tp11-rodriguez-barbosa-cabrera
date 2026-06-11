from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/send", methods=["POST"])
def send_mail():
    data = request.json

    print("=== MAIL SIMULADO ===")
    print(f"Para: {data.get('email')}")
    print(f"Nombre: {data.get('nombre')}")
    print(f"Tipo: {data.get('tipo')}")

    return jsonify({
        "mensaje": "Mail enviado correctamente"
    })

@app.route("/")
def home():
    return jsonify({
        "status": "mail-mock funcionando"
    })

app.run(host="0.0.0.0", port=9000)
