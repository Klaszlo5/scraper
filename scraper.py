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

    menus = soup.find_all('h3')  # Menü címek  
    for menu in menus:  
        menu_title = menu.text.strip()  
        price = menu.find_next('span').text.strip() if menu.find_next('span') else 'N/A'  # Az ár kiolvasása  
        menu_items = menu.find_next('ul').find_all('li') if menu.find_next('ul') else []  

        if menu_items:  
            print(f"{menu_title} - {price}")  
            for item in menu_items:  
                item_name = item.text.strip()  
                print(f" {item_name}")  
            print()  # Üres sort hozzáad  

    additional_sections = soup.find_all('div', class_='additional-section-class')  # Ellenőrizd a megfelelő osztálynevet  
    if additional_sections:  
        for section in additional_sections:  
            print(section.text.strip())  
    else:  
        print("Nincsenek további információk.")  

finally:  
    driver.quit()  
