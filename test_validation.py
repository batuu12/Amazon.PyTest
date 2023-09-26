
from pages.cartDetails import CartDetails
from pages.homepage import HomePage
from pages.productDetails import ProductDetails
from pages.searchDetails import SearchDetails


def test_case_1_validate_added_item(driver):
    
    homepage = HomePage(driver)
    searchdetails = SearchDetails(driver)
    productdetails = ProductDetails(driver)
    cartdetails = CartDetails(driver)

    homepage.accept_cookies()
    homepage.search_desired_item("Iphone")
    searchdetails.click_desired_item()
    actualProduct = productdetails.get_product_text()
    productdetails.add_to_cart_desired_item()
    homepage.navigate_to_cart()
    expectedProduct = cartdetails.get_cart_item_details()

    print(actualProduct)
    print(expectedProduct)

    assert actualProduct.strip() == expectedProduct.strip()


def test_case_2_validate_zero_results(driver):
     
    homepage = HomePage(driver)
    searchdetails = SearchDetails(driver)

    homepage.accept_cookies()
    homepage.search_desired_item("Iphone")
    searchdetails.set_min_value(1000000)
    searchdetails.set_max_value(3000000)
    searchdetails.filter_desired_values()
    isResultOk = searchdetails.is_Result_Ok_Or_Not()

    assert isResultOk == True

def test_case_3_validate_searched_item(driver):

    homepage = HomePage(driver)
    searchdetails = SearchDetails(driver)
    productdetails = ProductDetails(driver)

    homepage.accept_cookies()
    homepage.search_desired_item("Iphone")
    searchdetails.click_desired_item()
    name = productdetails.get_product_text()
    isNameTrue = name.__contains__("iPhone")

    print(name)
    print(isNameTrue)
    
    assert isNameTrue == True