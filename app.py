from flask import Flask, request, send_file
import fitz  # PyMuPDF
from io import BytesIO

app = Flask(__name__)

@app.route('/merge-pdfs', methods=['POST'])
def merge_pdfs():
    files = request.files.getlist("files")
    filename = request.form.get("filename", "merged.pdf")

    if not files:
        return {"error": "No files uploaded"}, 400

    merger = fitz.open()

    for file in files:
        pdf = fitz.open(stream=file.read(), filetype="pdf")
        merger.insert_pdf(pdf)

    output = BytesIO()
    merger.save(output)
    output.seek(0)

    return send_file(output, download_name=filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
