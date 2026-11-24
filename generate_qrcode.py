import segno

def generate_qrcode(text, output_file):
    qrcode = segno.make_qr(text)
    qrcode.save(output_file)
    print(f"QR код успешно сохранен в {output_file}")

if __name__ == "__main__":
    text = input("Введите текст для генерации QR-кода: ")
    output_file = "qrcode.png"
    generate_qrcode(text, output_file)
