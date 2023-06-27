from bs4 import BeautifulSoup


with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title.string)
# print(soup.prettify())
#print(soup.prettify())\

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    #print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.getText())

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)


company_url = soup.select_one(selector="p a")
# Different selectors
# elements with spaces
# ID you use # so #name
# Class uses . so .heading
print(company_url)

heading = soup.select(".heading")
print(heading)