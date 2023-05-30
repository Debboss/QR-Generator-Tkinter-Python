import qrcode
import tkinter as tk

def generate_qrcode():
    data = entry.get()
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 100,
        border = 10,
    )

    qr.add_data(data);
    qr.make(fit = True);
    image = qr.make_image(fill_color = "black", back_color = "white");
    image.save("qrcode.png");
    status_label.config(text="QR code generated and saved as qrcode.png");


# Create the main window
window = tk.Tk();
window.title("QR Code Generator");
window.geometry("300x200");

entry = tk.Entry(window);
entry.pack(pady=10);

# Create a button to generate the QR code
generate_button = tk.Button(window, text = "Generate QR code", command = generate_qrcode);
generate_button.pack(pady=10);

status_label = tk.Label(window, text="");
status_label.pack(pady=10);

window.mainloop();