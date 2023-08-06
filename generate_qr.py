import qrcode
qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,)
qr.add_data(input("Enter The Message Or Link To Generate its QR Code : "))
qr.make(fit=True)
img = qr.make_image()
Name = input("Name of the QR Code : ")
img.save(Name+".png")