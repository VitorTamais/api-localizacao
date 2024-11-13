from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"

# Criar a pasta para armazenar os arquivos
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return "Nenhum arquivo enviado.", 400
    
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, "localizados.txt")
    file.save(file_path)
    
    print("Arquivo recebido e salvo com sucesso.")
    return "Arquivo salvo com sucesso.", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
