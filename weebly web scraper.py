import requests
import bs4

result = requests.get("https://rorylalor.weebly.com/guest-food-gallery.html")
soup = bs4.BeautifulSoup(result.text, "lxml")
mystring = soup.select('a[href$="_orig.jpg"]')
clean_list = []
for item in mystring:
    clean_list.append(item['href'])

prefix = "https://rorylalor.weebly.com"
clean_list = [prefix + item for item in clean_list]

counter = 1

for item in clean_list:
    response = requests.get(item)
    if response.status_code == 200:
        filename = f"image_{counter}.jpg"

        with open(filename, 'wb') as f:
            f.write(response.content)

        counter += 1

    else:
        print(f"failed to get {item}. Status code: {response.status_code}")
