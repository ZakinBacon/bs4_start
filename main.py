from bs4 import BeautifulSoup
import requests

news = requests.get("https://news.ycombinator.com/")
yc_webpage = news.text

# Creating our Soup
soup = BeautifulSoup(yc_webpage, "html.parser")

# Creating lists to store all the stories
article_titles = []
article_links = []
for article_tag in soup.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])

# List for the upvotes
article_upvotes = []
# Looping through to get the scores
for article in soup.find_all(name="td", class_="subtext"):
    if article.span.find(class_="score") is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

# Finds the largest score in all of the scores stored in article_upvotes
max_points_index = article_upvotes.index(max(article_upvotes))
print(
    f"{article_titles[max_points_index]}, "
    f"{article_upvotes[max_points_index]} points, "
    f"available at: {article_links[max_points_index]}."
)



# ----------------------- Notes ---------------- #


# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# # print(soup.title.string)
# # print(soup.prettify())
# #print(soup.prettify())\
#
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:2
#     #print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading.getText())
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
#
# company_url = soup.select_one(selector="p a")
# # Different selectors
# # elements with spaces
# # ID you use # so #name
# # Class uses . so .heading
# print(company_url)
#
# heading = soup.select(".heading")
# print(heading)

