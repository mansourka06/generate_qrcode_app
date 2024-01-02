import qrcode
from PIL import Image
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def generate_qr_code(mail, phone, firstname, lastname, entity, crypted_info):
    # Combine information into a string
    info_str = f"Mail: {mail}\nPhone: {phone}\nFirst Name: {firstname}\nLast Name: {lastname}\nEntity: {entity}\nInfo: {crypted_info}"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data("Bassirou Faye\n069977656\nbassiroufaye815@gmail.com")
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save("user_qr_code.png")

    return "user_qr_code.png"

def send_email(receiver_email, attachment_filename):
    # Your email credentials
    sender_email = "kamansour06@gmail.com"
    sender_password = "xxxxxxxxxxxxxxxxxxxxxx"

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "QR Code Validation"

    # Attach the image
    with open(attachment_filename, "rb") as attachment:
        image_part = MIMEImage(attachment.read(), name="user_qr_code.png")
    message.attach(image_part)

# Add a personalized message to the email body
    body_message = f"""
    Dear {user_firstname},

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
    # Replace these with the actual user information
    user_mail = "bassiroufaye815@gmail.com"
    user_phone = "0664379518"
    user_firstname = "Mansour"
    user_lastname = "KA"
    user_entity = "DSTI"
    info = "Hello this a scripted info from Security Team"

    # Generate and save the QR code
    qr_code_path = generate_qr_code(user_mail, user_phone, user_firstname, user_lastname, user_entity, info)

    # Send the email with the QR code as an attachment
    send_email(user_mail, qr_code_path)
