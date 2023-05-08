
import httpx
from django.shortcuts import HttpResponseRedirect,render
from django.contrib import messages
import gspread
from dotenv import load_dotenv
import os

 
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






# personal
my_key = worksheet.acell("A2").value

API_KEY = f"{my_key}".strip()


async def theShortner(user_url, custom_name):
    async with httpx.AsyncClient() as client:
            
        payload = {'key': API_KEY , 'short': user_url, 'name': custom_name}
        response = await client.get('https://cutt.ly/api/api.php', params=payload)
        response.raise_for_status()
        u_data = response.json()

        try:
            return {u_data['url']['shortLink']}
        except:
            return f"OOPS the ERROR is :  {u_data['url']['status']} "


import asyncio

# views here ==>


from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie
def LShome(request):
    if request.method == 'POST':
        the_url = request.POST.get('long_url')
        if not the_url:
            messages.error(request, "To Shorten Any Link You Need To Enter A Valid Link First ! " , extra_tags='errors') 
            return HttpResponseRedirect('/linkshortener/')
        else:
            async def main():
                result = await theShortner(f"{the_url}", "")
                return (result)
            short_url = list(asyncio.run(main()))[0]
            # messages.success(request, short_url) 
            # print(short_url)
            return render(request, 'linkshort.html', {'short_url': short_url})  
    return render(request, 'linkshort.html')


