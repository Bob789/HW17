
israel = {
    "name": "Israel",
    "birth": 1948,
    "population_millions": 9.3,
    "capital": "Jerusalem",
    "language": "Hebrew",
    "cities": ["Jerusalem", "Tel Aviv", "Haifa", "Rishon LeZion", "Petah Tikva", "Ashdod"],
    "currency": "ILS",
    "area_kilometer": 22145,
    "gdp_billion": 450
}
# כלומר- קלוט את שם המדינה , לאחר מכן את שנת ה לידה של המדינה וכו'
# )עבור שדה הערים: קלוט 3 מחרוזות לשמות ערים ואח סן אותם ברשימה(
# לאחר סיום הקלט, הדפס את המילון שנוצר עם כל ה ערכים בתוכו
print(israel.get("capital"))
print(israel.keys())
print(israel.values())
print(israel.items())
israel_copy = israel.copy()
name = israel_copy.pop("gdp_billion")
print(name)
print(israel_copy)
israel_key = dict.fromkeys(israel.keys(), 0)
print(israel_key)
cities_list = []
for k in israel_key.keys():
    if k != 'cities':
        value: str = str(input("Input value for key :"))
        israel_key[k] = value
    else:
        for _ in range(3):
            city: str = str(input("Input city name :"))
            cities_list.append(city)
        israel_key[k] = cities_list
print(israel_key)


