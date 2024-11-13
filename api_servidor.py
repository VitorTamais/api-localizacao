from flask import Flask, request, send_from_directory, abort
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

# Rota para visualizar ou baixar o arquivo
@app.route("/logs/<filename>", methods=["GET"])
def get_file(filename):
    try:
        return send_from_directory("logs", filename)
    except FileNotFoundError:
        abort(404, description="Arquivo não encontrado")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
