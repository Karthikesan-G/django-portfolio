from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
from django.core.mail import send_mail
import time


def contact(request):
    contact_details = {
        'address1': 'No.02 Perumal Kovil Street, Kurumbagaram,',
        'address2': 'Nedungadu, Karaikal - 609603',
        'telephone': '+91 7708243662',
        'telephone_for': '+917708243662',
        'email': 'karthikesan.in@gmail.com',
    }
    if request.method == 'POST':
        from_email = request.POST.get('email')
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Email configuration
        to_email = "karthikesan.in@gmail.com"
        email_subject = "You have a message from your Bitmap Photography."
        email_body = f"""
        <html>
        <body>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {from_email}</p>
            <p><strong>Subject:</strong> {subject}</p>
            <p><strong>Message:</strong></p>
            <p>{message}</p>
        </body>
        </html>
        """
        try:
            send_mail(
                email_subject,
                '',
                from_email,
                [to_email],
                fail_silently=False,
                html_message=email_body,
            )
            return HttpResponse("Email sent successfully!")
        except Exception as e:
            return HttpResponse(f"Failed to send email: {str(e)}")
        finally:
            time.sleep(2)
            return render(request,"contact.html",{'contact_details': contact_details})
    return render(request,"contact.html",{'contact_details': contact_details})
