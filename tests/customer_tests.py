from pages.globalsqa.home_page import HomePage


def test_a(firefox_driver_setup):
    firefox_driver_setup.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/")
    home_page = HomePage(firefox_driver_setup)
    customer_login_page = home_page.customer_login()
    customer_login_page.take_user("Ron Weasly")
    customer_login_page.take_user("Albus Dumbledore")
    customer_page = customer_login_page.login()
    amount = 100
    customer_page.deposit(amount)
    assert customer_page.notification() == "Deposit Successful"

    assert amount == int(customer_page.get_transaction_amount())
    customer_page.logout()

    assert customer_login_page.is_displayed()


def test_b(firefox_driver_setup):
    firefox_driver_setup.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/")
    home_page = HomePage(firefox_driver_setup)
    customer_login_page = home_page.customer_login()
    customer_login_page.take_user("Harry Potter")
    customer_page = customer_login_page.login()
    amount = 100
    customer_page.withdraw_transaction(amount)
    assert customer_page.notification() == "Transaction Failed. You can not withdraw amount more than the balance."

    customer_page.deposit(amount)
    customer_page.withdraw_transaction(amount)
    assert customer_page.notification() == "Transaction successful"
    for x in customer_page.get_transactions_amount():
        assert int(x.text) == amount

    customer_page.logout()
    assert customer_login_page.is_displayed()
