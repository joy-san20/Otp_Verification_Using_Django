
from django.shortcuts import redirect, render
from django.contrib import messages
import smtplib
import ssl
import numpy as np

name = ''
email = ''
password = ''
otp = 0

def reg(request):
        return render(request, 'registration.html')

def reg_verification(request):
    global otp
    global name
    global email
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        otp = np.random.randint(111111, 999999)
        smtp_server = "smtp.outlook.com"
        port = 587  # For starttls# outlook PORT = 587
        sender_email = "example@example.com" # Write the sender email 
        sender_password = '***********' # Write the password
        receiver_email = email
        message = """\
                    Subject: OTP Verification

                    Sanjoy is asking for the OTP\n Your OTP is {}.""".format(otp)

        # Create a secure SSL context
        context = ssl.create_default_context()
        print("OTP1=", otp)
        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.starttls(context=context)  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)

        except Exception as e:
            # Print any error messages to stdout
            print(e)
            print("Invalid Email Address")

        finally:
            server.quit()

        context = {
            email : email
        }
        return render(request, 'otp_verification.html', context)

def verify(request):
    print("OTP2 = ", otp)
    i = request.POST.get("otp")
    print("Printing I", i)
    if int(i) == int(otp):
        messages.success(request, "Login Successfuly")
        content = {
            name: name,
        }
        print("Success ")
        return render(request, 'home.html', content)
    else:
        print("failure ")
        messages.error(request, "Wrong OTP")
        return redirect("otp_verification.html")
