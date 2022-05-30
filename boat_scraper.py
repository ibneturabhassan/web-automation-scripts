from selenium import webdriver
from csv import writer
import time
import datetime

date=datetime.date.today()
driver = webdriver.Firefox(executable_path="geckodriver.exe")
names=[]
links1=[]
quantity=[]
links=[]
driver.get("https://www.boteboard.com/collections/paddleboards")

driver.execute_script("window.scrollTo(0, 5000)")
with open('Stock' + str(date) + '.csv', 'w', newline='', encoding='utf-8') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(('Name','Link','Quantity'))
    f_object.close()

for i in range(1,25):
    try:
        link=driver.find_element_by_xpath('//*[@id="shopify-section-collection-template-boost-pfs-filter"]/div[3]/div[3]/div/div[2]/div['+str(i)+']/div/div[2]/a').get_attribute('href')
        links.append(link)
    except:
        continue
    if i==24:
        for j in range(2,5):
           try:
            driver.get('https://www.boteboard.com/collections/paddleboards?page='+str(j))
           except:
               break
           for k in range(1, 25):
                try:
                    link = driver.find_element_by_xpath(
                        '//*[@id="shopify-section-collection-template-boost-pfs-filter"]/div[3]/div[3]/div/div[2]/div[' + str(
                            k) + ']/div/div[2]/a').get_attribute('href')
                    links.append(link)
                except:
                    continue

    else:
        continue
for i in links:
    driver.get(i)
    driver.find_element_by_xpath('//*[@id="root"]/div[1]/section/div[2]/div/div[1]/div[2]/form/div[2]/div/div/input').send_keys('1000')
    time.sleep(5)
    try:
        check=driver.find_element_by_xpath('//*[@id="add-to-cart-button"]/button')
    except:
        try:
            check=driver.find_element_by_xpath('//*[@id="add-to-cart-button"]/div')
        except:
            continue
    check=check.text
    if check=='PRE-ORDER NOW':
        name=driver.find_element_by_css_selector('#root > div.product-container.py3 > section > div.outer > div > div.product.f.jcb.fw > div.product-data > h1').text
        # print(name)
        # print(i)
        # print(check)
        with open('Stock' + str(date) + '.csv', 'a', newline='',encoding='utf-8') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow((name, i, 'Pre-Order Item'))
            f_object.close()
    elif check=='Out of Stock':
        name=driver.find_element_by_css_selector('#root > div.product-container.py3 > section > div.outer > div > div.product.f.jcb.fw > div.product-data > h1')
        name=name.text
        print('out of')
        with open('Stock' + str(date) + '.csv', 'a', newline='',encoding='utf-8') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow((name, i, check))
            f_object.close()
    else:
        try:
            driver.find_element_by_css_selector('#add-to-cart-button > button').click()
        except:
            driver.find_element_by_css_selector('#justuno_form > div > div.frame-container > div:nth-child(2) > div > div > div > span > span > span').click()


driver.get('https://www.boteboard.com/cart')
counter=1
while True:
    try:
        product=driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/form/table/tbody/tr['+str(counter)+']/td[2]/a')
        names.append(product.text)
        links1.append(product.get_attribute('href'))
        counter=counter+1
    except:
        break


# print(names)
# print(links1)
# print(len(names))
# print(len(links1))

driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/form/div/div[3]/input[3]').click()
for i in range(len(names)):
    i=i+1
    Q=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr['+str(i)+']/td[2]/span')
    quantity.append(Q.text)

for i in range(len(names)):
    with open('Stock' + str(date) + '.csv', 'a', newline='', encoding='utf-8') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow((names[i],links1[i],quantity[i]))
        f_object.close()


driver.close()


