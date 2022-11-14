from selenium.webdriver.common.by import By


class BaseLocators:
    # Texts
    HEADER_TEXT = (By.XPATH, "//strong[@class='mainHeading']")

    # Buttons
    HOME_BTN = (By.XPATH, "//button[normalize-space()='Home']")
    LOGOUT_BTN = (By.XPATH, "//button[normalize-space()='Logout']")


class HomePageLocators:
    # Buttons
    CUSTOMER_LOGIN_BTN = (By.XPATH, "//button[normalize-space()='Customer Login']")
    BANK_MANAGER_BTN = (By.XPATH, "//button[normalize-space()='Bank Manager Login']")


# Customer
class CustomerLoginPageLocators:
    # Lists
    USERS_LIST = (By.XPATH, "//select[@id='userSelect']")
    USERS_LIST_OPTIONS = (By.TAG_NAME, "option")

    # Buttons
    LOGIN_BTM = (By.XPATH, "//button[normalize-space()='Login']")


class CustomerPageLocators:
    # Buttons
    TRANSACTION_BTN = (By.XPATH, "//button[normalize-space()='Transactions']")
    DEPOSIT_BTN = (By.XPATH, "//button[normalize-space()='Deposit']")
    WITHDRAW_BTN = (By.XPATH, "//button[normalize-space()='Withdrawl']")
    DEPOSIT_INPUT_BTN = (By.XPATH, "//button[@type='submit']")
    WITHDRAW_INPUT_BTN = (By.XPATH, "//button[normalize-space()='Withdraw']")

    # Input field
    DEPOSIT_INPUT = (By.CSS_SELECTOR, "input[placeholder='amount']")

    # Notification
    TRANSACTIONS_NOTIFICATION = (By.XPATH, "//span[@class='error ng-binding']")

    # Transactions
    # TRANSACTION_QUERY = (By.XPATH, "//table[contains(@class,'table table-bordered')]")
    TRANSACTION_QUERY = (By.XPATH, "//tr[contains(@id, 'anchor')]")
    TRANSACTION_DATE = (By.XPATH, "//tr[contains(@id, 'anchor')]//td[position()=1]")
    TRANSACTION_AMOUNT = (By.XPATH, "//tr[contains(@id, 'anchor')]//td[position()=2]")
    TRANSACTION_TYPE = (By.XPATH, "//tr[contains(@id, 'anchor')]//td[position()=3]")

    # Input field
    WITHDRAW_INPUT = (By.XPATH, "//input[@placeholder='amount']")

    # Text
    WELCOME_USER_TEXT = (By.XPATH, "//span[@class='fontBig ng-binding']")


class BankManagerPageLocators:
    # Buttons
    ADD_CUSTOMER_BTN = (By.XPATH, "//button[normalize-space()='Add Customer']")
    OPEN_ACCOUNT_BTN = (By.XPATH, "//button[normalize-space()='Open Account']")
    CUSTOMER_BTN = (By.XPATH, "//button[normalize-space()='Customers']")
    ADD_CUSTOMER_SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")
    PROCESS_BTN = (By.XPATH, "//button[normalize-space()='Process']")

    # Input field
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='Last Name']")
    POST_CODE_INPUT = (By.XPATH, "//input[@placeholder='Post Code']")
    SEARCH_CUSTOMER_INPUT = (By.XPATH, "//input[@placeholder='Search Customer']")

    # Customer table
    CUSTOMER_DATE = (By.XPATH, "(//td[@class='ng-binding']/following-sibling::td)[1]")

    # Lists
    CUSTOMER_LIST = (By.XPATH, "//select[@id='userSelect']")
    CURRENCY_LIST = (By.XPATH, "//option[@value='{}']")
    LIST_OPTIONS = (By.TAG_NAME, "option")


class StorePage:
    # Link
    PHONE_LINK = (By.XPATH, "(//a[normalize-space()='Phones'])[1]")
    OPEN_PHONE_LINK = (By.XPATH, "(//a[@class='hrefch'])[1]")
    CART_LINK = (By.XPATH, "//a[@id='cartur']")

    # Text
    SUCCESS_PURCHASE_TEXT = (By.XPATH, "// h2[normalize-space() = 'Thank you for your purchase!']")

    # Buttons
    ADD_TO_CART_BTN = (By.XPATH, "//a[normalize-space()='Add to cart']")
    PLACE_ORDER_BTN = (By.XPATH, "//button[normalize-space()='Place Order']")
    PURCHASE_BTN = (By.XPATH, "//button[normalize-space()='Purchase']")

    # Inputs
    NAME_INPUT = (By.XPATH, "//input[@id='name']")
    COUNTRY_INPUT = (By.XPATH, "//input[@id='country']")
    CITY_INPUT = (By.XPATH, "//input[@id='city']")
    CREDIT_CARD_INPUT = (By.XPATH, "//input[@id='card']")
    MONTH_INPUT = (By.XPATH, "//input[@id='month']")
    YEAR_INPUT = (By.XPATH, "//input[@id='year']")
