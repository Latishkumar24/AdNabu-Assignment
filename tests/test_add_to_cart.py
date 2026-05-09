from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_add_to_cart():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.maximize_window()
    wait = WebDriverWait(driver,10)

    driver.get("https://adnabu-store-assignment1.myshopify.com/password")

    #Input Password To Enter store
    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.send_keys("AdNabuQA")

    #Clicking Enter Button
    enter_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))
    ).click()

    #search product
    search = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "svg.icon-search"))
    ).click()

    search_input =  wait.until(
        EC.visibility_of_element_located((By.ID, "Search-In-Modal"))
    )
    search_input.send_keys("The Collection Snowboard: Liquid")
    
    searchicon = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Search']"))
    ).click()

    # open product
    wait.until(
        EC.element_to_be_clickable((By.ID, "CardLink--7801364742234"))
    ).click()


    #add to cart
    wait.until(
        EC.element_to_be_clickable((By.ID, "ProductSubmitButton-template--19850788667482__main"))
    ).click()

    #Verify product added to cart
    my_cart = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-item__name.h4.break"))
    )

    assert "The Collection Snowboard: Liquid" in my_cart.text




    

    


    
