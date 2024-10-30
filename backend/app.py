from flask import Flask, request, jsonify, send_file
import pymupdf4llm
import pandas as pd
import io
import tempfile

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload_pdf():
    file = request.files['file']
    print(file)

    # 一時ファイルとして保存
    with tempfile.NamedTemporaryFile(delete=True) as temp_pdf:
        file.save(temp_pdf.name)
        md_text = pymupdf4llm.to_markdown(temp_pdf.name)  # ファイルパスを渡す

    # MarkdownテキストをJSONで返す
    return jsonify({"markdown": md_text}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
