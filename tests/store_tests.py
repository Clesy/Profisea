from pages.demoblaze.home_page import HomePage


def test_buy_on_store(firefox_driver_setup):
    firefox_driver_setup.get("https://www.demoblaze.com/")
    home_page = HomePage(firefox_driver_setup)
    phone_page = home_page.go_to_phone()
    cart_page = phone_page.go_to_cart()
    place_order_popup = cart_page.press_place_order_btn()
    success_purchase_popup = place_order_popup.purchase("aa", "aa", "12", "aa", "aa", "aa")
    assert "Thank you for your purchase!" == success_purchase_popup.get_success_purchase_text()
