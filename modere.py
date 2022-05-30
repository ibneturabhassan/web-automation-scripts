import csv

from selenium import webdriver
import time


driver=webdriver.Chrome()
driver.get("https://www.modere.com.au/Shop/collections")
time.sleep(10)
names=[]
item_numbers=[]
prices=[]
quantities=[]
descriptions=[]
images=[]
abouts=[]
ingris=[]
for i in range(17,49,1):

 driver.find_element_by_xpath('//*[@id="products-list"]/ul/li['+str(i)+']').click()

 time.sleep(8)

 name=(driver.find_element_by_xpath('//*[@id="product-detail-div"]/div[1]/div/section/ul/li[4]/a'))

 names.append(name.text)

 description=driver.find_element_by_xpath('//*[@id="products-details"]/form/p[2]')

 descriptions.append(description.text)

 item_number = (driver.find_element_by_xpath('//*[@id="products-details"]/form/p[1]'))

 item_numbers.append(item_number.text)

 image=driver.find_element_by_css_selector('#products-details > div > a.desktop-only.fill > img')

 images.append(image.get_attribute('src'))

 price=driver.find_element_by_xpath('//*[@id="products-details"]/form/fieldset[1]/div[1]/p[2]/span')

 prices.append(price.text)

 quantity=driver.find_element_by_xpath('//*[@id="products-details"]/form/fieldset[1]/div[1]/p[1]/span[1]')

 quantities.append(quantity.text)

 about=driver.find_element_by_xpath('//*[@id="key-benefits"]/div[1]')

 abouts.append(about.text)

 driver.find_element_by_xpath('//*[@id="product-detail-div"]/div[2]/div/div[2]/header/ul/li[3]/a').click()

 ingri=driver.find_element_by_css_selector('#usage > div')

 ingris.append(ingri.text)

 ingris.append(ingri.text)

 driver.get("https://www.modere.com.au/Shop/collections")

 time.sleep(8)
driver.close()

try:
        with open('Collections.csv', 'w', encoding="utf-8", newline='') as file:
            writer = csv.writer(file)

            writer.writerow(["Product","Item Number","Image","Description","Price","Quantity","About","Ingredients"])

            for i in range(0, len(names), 1):

              writer.writerow([names[i],item_numbers[i],images[i],descriptions[i],prices[i],quantities[i],abouts[i],ingris[i]])
except:
          print('\nSomething went wrong')
          time.sleep(5)
else:
        print("\nFile is created as ")
        time.sleep(3)
# print(descriptions)
# print(images)
# print(abouts)
# print(ingris)
