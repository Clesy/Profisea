from pages.globalsqa.home_page import HomePage


def test_a(firefox_driver_setup):
    home_page = HomePage(firefox_driver_setup).load()
    bank_manager_page = home_page.bank_manager_login()
    first_name = "Clar"
    last_name = "Clar"
    bank_manager_page.add_new_customer(first_name, last_name, 3333)
    name = bank_manager_page.get_customer(first_name)
    assert first_name == name

    user = first_name + " " + last_name
    bank_manager_page.click_process_btn(user)
    home_page.click_home_btn()

    customer_login_page = home_page.customer_login()
    customer_login_page.take_user(user)
    customer_page = customer_login_page.login()
    assert user == customer_page.get_welcome_text()
