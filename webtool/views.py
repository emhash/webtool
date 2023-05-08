from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
import gspread
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()


credentials = {
    "type": os.getenv("GOOGLE_TYPE"),
    "project_id": os.getenv("GOOGLE_PROJECT_ID"),
    "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("GOOGLE_PRIVATE_KEY").replace('\\n' , '\n'),
    "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
    "client_id": os.getenv("GOOGLE_CLIENT_ID"),
    "auth_uri": os.getenv("GOOGLE_AUTH_URI"),
    "token_uri": os.getenv("GOOGLE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("GOOGLE_AUTH_PROVIDER_CERT_URL"),
    "client_x509_cert_url": os.getenv("GOOGLE_CLIENT_CERT_URL")
}

# personal
gc = gspread.service_account_from_dict(credentials)
THE_KEY = os.getenv('SHEET_API_KEY')
sh = gc.open_by_key(THE_KEY)
worksheet  = sh.sheet1 



from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie
def temp(request):

    current_time = datetime.now().strftime("%I:%M:%S %p")
    date = datetime.now().strftime('%Y-%m-%d')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not name or not email:

            messages.error(request,
                           "Please Enter Both A Name and Email Address ! ",
                           extra_tags='errors')
            return HttpResponseRedirect('/#tell')

        else:

            # SENDING MESSAGE TO SHEET
            new_data = [
                f"{name}", f"{email}", f"{message}", f"{date}",
                f"{current_time}"
            ]

            worksheet.insert_row(new_data, 3)

            # time.sleep(2)
            messages.success(request, "Ok, Thanks. I Got Your Message ! ")
            return HttpResponseRedirect('/#tell')

    else:
        return render(request, 'index.html', {'the_year': date})


#  I - ashiq

def ashiq(request):

    previous_url = request.META.get('HTTP_REFERER')
    # print(previous_url)
    # This helps to find the previous page, where user were.
    if previous_url is None:
        previous_url = '/'
        return render(request, 'dev.html', {'the_link': previous_url})

    else:
        return render(request, 'dev.html', {'the_link': previous_url})
