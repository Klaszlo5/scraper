from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from bs4 import BeautifulSoup  
import time  

# WebDriver beállítása  
driver = webdriver.Chrome()  

try:  
    driver.get("https://cafemetropolitan.hu/#food-menu")  
    wait = WebDriverWait(driver, 20)  
    greenpoint_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "GreenPoint7 irodaház")))  
    greenpoint_button.click()  

    time.sleep(2)  

    page_source = driver.page_source  
    soup = BeautifulSoup(page_source, 'html.parser')  

    no_menu_message = soup.find(text="Erre a hétre még nincs étlap feltöltve")  
    if no_menu_message:  
        print("Erre a hétre még nincs étlap feltöltve.")  
    else:  
        menus = soup.find_all('div', class_='menu-section-class') 
        for menu in menus:  
            menu_title = menu.find('h3').text.strip()  
            price = menu.find('span', class_='price-class').text.strip() if menu.find('span', class_='price-class') else 'N/A'  
            
            menu_items = menu.find_all('li')  
            if menu_items:  
                print(f"{menu_title} - {price}")  
                for item in menu_items:  
                    print(f" {item.text.strip()}")  
                print()
            else:  
                print(f"{menu_title} - {price} (Nincs étel a menüben)")  

        additional_items = soup.find_all('div', class_='special-item-class')
        for item in additional_items:  
            item_name = item.text.strip()  
            price = item.find('span', class_='price-class').text.strip() if item.find('span', class_='price-class') else 'N/A'  
            print(f"{item_name} - {price}")  

finally:  
    driver.quit()  
