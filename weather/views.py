from django.shortcuts import render
import requests

API_KEY = "4fdcfccc0489ef6de8ae5b1053c25ad3"


def home(request):
    weather = None
    error = None

    if request.method == "POST":
        city = request.POST.get("city")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            print(data)

            if str(data.get("cod")) == "200":
                weather = {
                    "city": data["name"],
                    "country": data["sys"]["country"],
                    "temperature": data["main"]["temp"],
                    "feels_like": data["main"]["feels_like"],
                    "humidity": data["main"]["humidity"],
                    "pressure": data["main"]["pressure"],
                    "wind": data["wind"]["speed"],
                    "description": data["weather"][0]["description"].title(),
                    "icon": data["weather"][0]["icon"],
                    "condition": data["weather"][0]["main"].lower(),
                }
            else:
                error = data.get("message", "City Not Found")

        except Exception as e:
            error = f"Something went wrong: {e}"

    return render(request, "weather/home.html", {
        "weather": weather,
        "error": error,
    })