import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductCategoryPage(BasePage):
    SEARCHED_PRODUCTS = (By.CSS_SELECTOR, '[data-cy="title-recipe"]:not(:has(.a-row)) a[class="a-link-normal s-line-clamp-4 s-link-style a-text-normal"]')
    SECOND_PAGE = (By.XPATH, '//li[@class="s-list-item-margin-right-adjustment"][2]')
    THIRD_PRODUCT = (By.CSS_SELECTOR, '[data-cy="title-recipe"]:not(:has(.a-row)) a[class="a-link-normal s-line-clamp-4 s-link-style a-text-normal"]')
    VERIFY_SECOND_PAGE='sr_pg_2'


    def get_searched_products_text(self):
        product_elements = self.find_elements(*self.SEARCHED_PRODUCTS)
        samsung_found = False
        for idx, element in enumerate(product_elements, 1):
            product_name = self.get_text(element)
            if "Samsung" in product_name:
                samsung_found = True
                print(f"Product '{idx}' is -> {product_name}")
            else:
                samsung_found = False
                break
        return samsung_found


    def click_second_page(self):
        self.click_element(self.SECOND_PAGE)

    def click_third_product(self):
        self.click_element(self.THIRD_PRODUCT)
