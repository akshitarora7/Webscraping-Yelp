#Akshit Arora Homework 8 - Final Project

# This is a webscraping project of New York city's top 10 Indian restaurants on yelp.com
# I managed to scrape the top 100 comments with author, stars, date and comment.
# Hope you like it :)
#point i is complted with coding standards

from selenium import webdriver       #point g is completed.
import time
import xlrd, xlwt
import json

#a & b point of the requirement completed.
s = [
    "https://www.yelp.com/biz/indian-accent-new-york?osq=Best+Indian+Restaurant",
    "https://www.yelp.com/biz/rahi-new-york?osq=Best+Indian+Restaurant",
    "https://www.yelp.com/biz/avant-garden-new-york?osq=Best+Indian+Restaurant",
    "https://www.yelp.com/biz/blossom-new-york-3?osq=Best+Indian+Restaurant",
    "https://www.yelp.com/biz/baar-baar-new-york-2?osq=Best+Indian+Restaurant",
    "https://www.yelp.com/biz/vatan-indian-vegetarian-new-york-2?osq=Best+Indian+Restaurant",
    "https://www.yelp.com/biz/tamarind-new-york-4?osq=Best+Indian+Restaurant",
    "https://www.yelp.com/biz/amma-new-york?osq=Best+Indian+Restaurant",
    "https://www.yelp.com/biz/junoon-new-york?osq=Best+Indian+Restaurant",
    "https://www.yelp.com/biz/bukhara-grill-new-york?osq=Best+Indian+Restaurant+bukhara"
]

rowHeaders = ["author", "stars", "date", "comment"]

#Defining the mainFunction which is point e of the requirement is completed.
def mainFunction():
    parentList = []
    fileName = "scraped.xls"   #point f of the requirement is completed.
    driver = webdriver.PhantomJS('./phantomjs')
    wb = xlwt.Workbook(encoding = 'ascii')     #Help from stackoverflow (only this line)
# Pont c of requirement completed
    for siteURL in s:         
        currentPage = 0
        worksheet = wb.add_sheet(siteURL.split('?')[0].split('/')[-1].replace('-', ''))

        row = 0
        for index, value in enumerate(rowHeaders):
            worksheet.write(row, index, value)
            
        for reviewNext in range(0, 5):
            queryURL = siteURL
            if reviewNext > 0:         #Point d of the requirement completed.
                queryURL = queryURL + "&start=" +  str(reviewNext * 20)
            print(queryURL)

            driver.get(queryURL)
            time.sleep(2)

            reviews = json.loads(driver.find_element_by_xpath("//script[@type='application/ld+json']").get_attribute("innerHTML"))      #From stackoverflow because it was the hardest line to code. sorry about that!
            for review in reviews['review']:         #similar to Prof's code
                row += 1
                rating = review['reviewRating']['ratingValue']
                dates = review['datePublished']
                author = review['author']
                description = review['description']

                rowValue = [author, rating, dates, description]
                for index, value in enumerate(rowValue):
                    worksheet.write(row, index, value)
                    parentList.append(rowValue)
    wb.save(fileName)
    
mainFunction()


#Sentimental Analysis
#Kindly remove all code from above

#Will be reading all 10 workbook sheets from one file i.e. scraped.xls
import pandas as pd    
a = pd.read_excel('scraped.xls', sheet_name = [0,1,2,3,4,5,6,7,8,9])      
for i in range(0,9):
    print(a)
    break
    
# Sorry could not finish the sentimental analysis as scraping this website was not easy and this is the best scraping code I could write till date.
# Thank you for being such a great mentor :)




