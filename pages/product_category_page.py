from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductCategoryPage(BasePage):
    SEARCHED_PRODUCTS = (By.CSS_SELECTOR, '.a-link-normal.s-line-clamp-4.s-link-style.a-text-normal')
    SECOND_PAGE = (By.XPATH, '//li[@class="s-list-item-margin-right-adjustment"][2]')
    THIRD_PRODUCT = (By.XPATH, '(//div[@class="a-section aok-relative s-image-square-aspect"])[3]')
    VERIFY_SECOND_PAGE='sr_pg_2'
    searched_product='samsung'


    def get_searched_products_text(self):
        product_elements = self.find_elements(*self.SEARCHED_PRODUCTS)
        samsung_found = False
        for element in product_elements:
            product_name = element.text
            if "Samsung" in product_name:
                samsung_found = True
                print(f"Found in-> {product_name}")
        return samsung_found


    def scroll_by_amount(self, x_offset, y_offset):
        self.driver.execute_script("window.scrollBy(arguments[0], arguments[1]);", x_offset, y_offset)

    def wait_for_visual_delay(self, delay_in_seconds):
        self.driver.execute_script(f"return new Promise(resolve => setTimeout(resolve, {delay_in_seconds * 1000}))")

    def click_second_page(self):
        self.click_element(self.SECOND_PAGE)

    def click_third_product(self):
        self.click_element(self.THIRD_PRODUCT)

    def scroll_third_product(self):
        self.scroll_element(self.THIRD_PRODUCT)
