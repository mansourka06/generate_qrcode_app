import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import qrcode[pil]
#from PIL import Image


def generate_qr_code(mail, phone, firstname, lastname):
    # Combine information into a string
    info_str = f"Mail: {mail}\nPhone: {phone}\nFirst Name: {firstname}\nLast Name: {lastname}"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(info_str)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save("client_qr_code.png")

    return "client_qr_code.png"

def send_email(receiver_email, firstname, attachment_filename):
    # Your email credentials
    sender_email = "kamansour06@gmail.com"
    sender_password = "xxxxxxxxxxxxxxxxxxx"

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "[DEVOPS MEETING] 31/12/2023"

    # Attach the image
    with open(attachment_filename, "rb") as attachment:
        image_part = MIMEImage(attachment.read(), name="client_qr_code.png")
    message.attach(image_part)

    # Add a personalized message to the email body
    body_message = f"""
    Dear {firstname},

    We are delighted to inform you that you have 
    received the QR code ticket for the DevOps
    meeting.
    
    Please be ready for the upcoming session.

    Save the date!

    Regards,

    AMBB Technologies
    """
    message.attach(MIMEText(body_message, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    # Replace these with the actual client information
    client_mail = "mailmansour@gmx.fr"
    client_phone = "0664379518"
    client_firstname = "Mansour"
    client_lastname = "KA"
    # Generate and save the QR code
    qr_code_path = generate_qr_code(client_mail, client_phone, client_firstname, client_lastname)

    # Send the email with the QR code as an attachment
    send_email(client_mail, client_firstname, qr_code_path)
