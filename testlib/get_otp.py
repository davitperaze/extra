import requests


import calendar
from datetime import datetime, timezone, timedelta


class GetOtp():
    def __init__(self) -> None:
        pass

    def check_mail(self, email, ts):
        url = "https://api.testmail.app/api/json?apikey=1b069fbb-ad44-4ae1-ba7b-bb560f356503&namespace=22vzm&headers=false&tag="+email+"&limit=1&timestamp_from="+str(ts)+"&livequery=true"
        print(url)

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        res = response.json()
        emails = res.get("emails")[0]
        email_text = emails.get("text")
        print(res)
        otp = email_text.split()[-1]
        print(otp)
        return otp
