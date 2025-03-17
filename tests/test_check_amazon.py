from pages.home_page import HomePage
from pages.product_category_page import ProductCategoryPage
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage
from tests.base_test import BaseTest


class CheckAmazonShoppingTest(BaseTest):
    def test_check_amazon_shopping(self):
        home_page=HomePage(self.driver)
        self.assertEqual(self.base_url,home_page.get_current_url(),'ERROR: Unable to access the Amazon homepage.')
        home_page.close_cookies()
        home_page.send_keys_samsung()
        home_page.click_search_button()


        product_category_page = ProductCategoryPage(self.driver)
        search_product=product_category_page.get_searched_products_text()
        self.assertTrue(search_product,"ERROR: The wrong product was searched.")
        product_category_page.scroll_by_amount(0,9000)

        product_category_page.click_second_page()
        self.assertIn(product_category_page.VERIFY_SECOND_PAGE, product_category_page.get_current_url(), 'ERROR: The second page cannot be accessed.')
        product_category_page.click_third_product()


        product_page=ProductPage(self.driver)
        buy_now_element=product_category_page.find_element(*product_page.BUY_NOW_BUTTON)
        self.assertTrue(buy_now_element.is_displayed(),'ERROR: The button is not displayed as expected.')
        product_name = product_page.get_product_text() #-----------#
        self.assertIn(product_page.verify_text,product_page.get_product_text(),'ERROR: The wrong product is selected.')
        product_page.click_add_to_card_button()
        self.assertIn(product_page.add_to_card_verify,product_page.get_verify_add_to_card(),
                      "ERROR: The product was not added to the cart.")
        product_page.click_to_cart()


        shopping_cart_page=ShoppingCartPage(self.driver)
        self.assertIn(shopping_cart_page.verify_card_page,shopping_cart_page.get_current_url() , 'ERROR: Not on the shopping cart page.')
        cart_product = shopping_cart_page.product_in_cart() #-----------#
        self.assertIn(product_name, cart_product, "ERROR: The product has not been added to your cart,"
                                                  " or the wrong product has been added.")
        shopping_cart_page.click_delete_product()
        self.assertIn(shopping_cart_page.delete_product_verify,shopping_cart_page.verify_delete_product(),
                      'ERROR: The product could not be removed from your cart.')
        shopping_cart_page.click_homepage()









