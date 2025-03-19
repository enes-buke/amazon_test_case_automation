from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ShoppingCartPage(BasePage):
    PRODUCT_IN_CART = (By.CSS_SELECTOR, ".a-truncate-full")
    DELETE_BUTTON =(By.XPATH, "//button/span[@class='a-icon a-icon-small-trash']")
    VERIFY_DELETE=(By.CSS_SELECTOR, '.a-size-base.sc-list-item-removed-msg-text-delete')
    HOME_PAGE = (By.ID, 'nav-logo-sprites')
    PAGE_TITLE = ('Amazon.com.tr: Elektronik, bilgisayar, akıllı telefon, kitap, oyuncak, yapı market, ev, '
                  'mutfak, oyun konsolları ürünleri ve daha fazlası için internet alışveriş sitesi')
    verify_card_page="nav_cart"
    delete_product_verify="Alışveriş Sepetiniz konumundan kaldırıldı."



    def product_in_cart(self):
        product_text=self.find_element(*self.PRODUCT_IN_CART).get_attribute("textContent")
        return product_text

    def click_delete_product(self):
        self.click_element(self.DELETE_BUTTON)

    def verify_delete_product(self):
        return self.get_text(self.VERIFY_DELETE)

    def click_homepage(self):
        self.click_element(self.HOME_PAGE)

    def is_correct_title(self, expected_title):
        return self.get_title() == expected_title



