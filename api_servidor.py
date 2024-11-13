from flask import Flask, request
import os

app = Flask(__name__)

# Rota para receber o arquivo
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "Nenhum arquivo enviado", 400
    
    file = request.files["file"]
    if file.filename == "":
        return "Nome do arquivo vazio", 400
    
    # Salvar o arquivo na pasta logs
    save_path = os.path.join("logs", file.filename)
    os.makedirs("logs", exist_ok=True)
    file.save(save_path)

    return "Arquivo recebido com sucesso", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Usa a porta definida pelo Render ou 5000 como fallback
    app.run(host="0.0.0.0", port=port)
