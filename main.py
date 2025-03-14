import sys
import pypdfium2 as pdfium

# コマンドライン引数からファイル名を取得
if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# PDFファイルを読み込む
try:
    pdf = pdfium.PdfDocument(filename)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)

# PDFのテキストを抽出して表示
for page in pdf:
    textpage = page.get_textpage()
    text = textpage.get_text_range()
    print(text)

