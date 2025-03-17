from pages.home_page import HomePage
from pages.product_category_page import ProductCategoryPage
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage
from tests.base_test import BaseTest


class CheckAmazonShoppingTest(BaseTest):
    def test_check_amazon_shopping(self):
        home_page=HomePage(self.driver)
        self.assertEqual(self.base_url,home_page.get_current_url(),'Not on the Amazon homepage.')
        home_page.close_cookies()
        home_page.send_keys_samsung()
        home_page.click_search_button()


        product_category_page = ProductCategoryPage(self.driver)
        search_product=product_category_page.get_searched_products_text()
        self.assertTrue(search_product,"You searched for the wrong product.")
        product_category_page.scroll_by_amount(0,9000)
        product_category_page.wait_for_visual_delay(0.5)
        product_category_page.click_second_page()
        self.assertIn(product_category_page.VERIFY_SECOND_PAGE, product_category_page.get_current_url(), 'You are not on the second page!')
        product_category_page.scroll_third_product()
        product_category_page.click_third_product()


        product_page=ProductPage(self.driver)
        product_page.scroll_by_amount(0,800)
        self.assertIn(product_page.verify_about_part,product_page.get_product_about(),'You are inside the wrong product!')
        product_category_page.wait_for_visual_delay(0.5)
        product_page.scroll_page_top()
        product_name = product_page.get_product_text() #-----------#
        self.assertIn(product_page.verify_text,product_page.get_product_text(),'You are inside the wrong product!')
        product_page.click_add_to_card_button()
        self.assertIn(product_page.add_to_card_verify,product_page.get_verify_add_to_card(),
                      "The product couldn't be added to your cart.")
        product_page.click_to_cart()


        shopping_cart_page=ShoppingCartPage(self.driver)
        self.assertIn(shopping_cart_page.verify_card_page,shopping_cart_page.get_current_url() , 'You are not on the cart page!')
        product_category_page.wait_for_visual_delay(1)
        cart_product = shopping_cart_page.product_in_cart() #-----------#
        self.assertIn(product_name, cart_product, "The product has not been added to your cart,"
                                                  " or the wrong product has been added.")
        shopping_cart_page.click_delete_product()
        self.assertIn(shopping_cart_page.delete_product_verify,shopping_cart_page.verify_delete_product(),
                      'The product could not be removed from your cart.')
        shopping_cart_page.click_homepage()









