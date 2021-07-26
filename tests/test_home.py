import pytest
from pytest import assume
import allure
import random as RD
# import pytest_check as check
from testlib.pages.homepage import HomePage
from testlib.pages.login_form_page import LoginFormPage
from testlib.pages.user_type_page import UserTypePage
from testlib.pages.register_form_page import RegisterFormPage
from testlib.pages.otp_form_page import OtpFormPage
from testlib.pages.password_form_page import PasswordFormPage
from testlib.pages.success_page import SuccessPage

from testlib.get_otp import GetOtp
import calendar, time
from datetime import datetime, timezone, timedelta


HP = HomePage()
LFP = LoginFormPage()
UTP = UserTypePage()
RFP = RegisterFormPage()
OTP = OtpFormPage()
GOTP = GetOtp()
PFP = PasswordFormPage()
SP = SuccessPage()

E_MAIL = "jondoekatsia"+ str(RD.randint(0, 100)) 
EMAIL = "22vzm."+E_MAIL+"@inbox.testmail.app"
@allure.feature("Extra.ge Registration test")
@allure.story("Happy path testing")
@allure.link("./test_data/test_cases.md", "User registration")
class TestHome:
    @allure.title("Go to https://extra.ge")
    @allure.description("Check if home page is loaded. Check header elements.")
    def test_home_logo_displayed(self):
        """Test Home Page is loaded"""
        logo = HP.check_page_loaded().is_displayed()
        user_button = HP.check_user_button().is_displayed()
        categories = HP.categories().is_displayed()
        search_bar = HP.search_bar().is_displayed()
        cart = HP.cart().is_displayed()
        print(user_button)
        print(categories)
        print(search_bar)
        print(cart)
        with assume: assert logo == True
        with assume: assert user_button == True
        with assume: assert categories == True
        with assume: assert search_bar == True
        with assume: assert cart == True

    @allure.title("Click \"შესვლა\" button")
    @allure.description("After clicking login button authorization form must be displayed")
    def test_login_form(self):
        """Check login form elements and click register link"""
        user_button = HP.check_user_button()
        user_button.click()
        close_button = LFP.close_button()
        form_header = LFP.form_header()
        with assume: assert close_button.is_displayed() == True
        with assume: assert form_header.text == 'ავტორიზაცია'



    @allure.title("Click register link")
    @allure.description("???")
    def test_user_type(self):
        """Check back button visibility"""
        register_link = LFP.register_link()
        register_link.click()
        close = LFP.close_button()
        back = UTP.back_button()
        header = UTP.header()
        user_type = UTP.user_type()
        with assume: assert close.is_displayed() == True
        with assume: assert back.is_displayed() == True
        with assume: assert header.text == "მომხმარებლის ტიპი"
        with assume: assert user_type.text == "ფიზიკური პირი"

        user_type.click()


    @allure.title("Enter name")
    @allure.description("Enter user first name")
    def test_first_name(self):
        name_input = RFP.name_input()
        name_label = RFP.name_label()
        next_button = RFP.register_button()

        with assume: assert name_input.is_displayed() == True
        with assume: assert name_label.is_displayed() == True
        with assume: assert name_label.text == "სახელი"
        with assume: assert name_input == RFP.get_active_element()

        with assume: assert next_button.is_displayed() == True
        with assume: assert next_button.text == "გაგრძელება"

        name_input.send_keys("Jondo")

        with assume: assert name_input.get_attribute("value") == "Jondo"

    @allure.title("Enter Last name")
    @allure.description("check last name inputs and enter")
    def test_last_name(self):
        last_name_input = RFP.last_name_input()
        last_name_label = RFP.last_name_label()
        with assume: assert last_name_input.is_displayed() == True
        with assume: assert last_name_label.is_displayed() == True
        with assume: assert last_name_label.text == "გვარი"

        last_name_input.send_keys("Katsia")

        with assume: assert last_name_input.get_attribute("value") == "Katsia"

    @allure.title("Enter e-mail")
    @allure.description("test email field and enter email")
    def test_email(self):
        email_input = RFP.email_input()
        email_label = RFP.email_label()
        next_button = RFP.register_button()

        with assume: assert email_input.is_displayed() == True
        with assume: assert email_label.is_displayed() == True
        with assume: assert email_label.text == "ტელეფონი ან ელ.ფოსტა"

        email_input.send_keys(EMAIL)

        with assume: assert email_input.get_attribute("value") == EMAIL
        with assume: assert next_button.is_enabled() == True


    @allure.title("test day input")
    @allure.description("testing day input")
    def test_day_input(self):
        day_input = RFP.day_input()
        day_label = RFP.day_label()
        with assume: assert day_input.is_displayed() == True
        with assume: assert day_label.is_displayed() == True
        with assume: assert day_label.text == "დღე"

        day_input.click()
        RFP.day_ch()[3].click()
        with assume: assert RFP.day_val().text == '4'

    @allure.title("test month input")
    @allure.description("testing month input")
    def test_month_input(self):
        month_input = RFP.month_input()
        month_label = RFP.month_label()
        with assume: assert month_input.is_displayed() == True
        with assume: assert month_label.is_displayed() == True
        with assume: assert month_label.text == "თვე"

        month_input.click()
        RFP.month_ch()[3].click()
        with assume: assert RFP.month_val().text == "აპრილი"

    @allure.title("test year input")
    @allure.description("testing year input")
    def test_registration_form(self):
        year_input = RFP.year_input()
        year_label = RFP.year_label()
        
        with assume: assert year_input.is_displayed() == True
        with assume: assert year_label.is_displayed() == True
        with assume: assert year_label.text == "წელი"

        year_input.click()
        RFP.year_ch()[12].click()
        with assume: assert RFP.year_val().text == '2009'

    @allure.title("click next button")
    @allure.description("check what happens after next button click")
    def test_click_next(self):
        next_button = RFP.register_button()
        next_button.click()

        close_button = OTP.close_button()
        back_button = OTP.back_button()
        otp_title = OTP.form_header()
        otp_message = OTP.message()
        otp_input = OTP.otp_input()
        otp_label = OTP.otp_label()
        otp_resend = OTP.otp_resend()
        otp_submit = OTP.otp_submit()

        with assume: assert close_button.is_displayed() == True
        with assume: assert back_button.is_displayed() == True
        with assume: assert otp_title.is_displayed() == True
        with assume: assert otp_title.text == "ელ.ფოსტის დადასტურება"
        with assume: assert otp_message.is_displayed() == True
        with assume: assert otp_message.text == "შენს მიერ მითითებულ ელ.ფოსტაზე "+ EMAIL +" გამოგზავნილია ვერიფიკაციის კოდი"
        with assume: assert otp_input.is_displayed() == True
        with assume: assert otp_label.is_displayed() == True
        with assume: assert otp_label.text == "შეიყვანე კოდი"
        with assume: assert otp_resend.is_displayed() == True
        with assume: assert otp_resend.text == "კოდის მოთხოვნა"
        with assume: assert otp_submit.is_displayed() == True
        with assume: assert "_s_btn-disabled-dark-100" in otp_submit.get_attribute("class")
        with assume: assert otp_submit.text == "დადასტურება"


    @allure.title("enter OTP")
    @allure.description("check otp functionality for "+E_MAIL)
    def test_enter_otp(self):
        current_datetime = datetime.utcnow()
        substracted = current_datetime - timedelta(minutes=1)
        back_time = substracted.utctimetuple()
        ts = calendar.timegm(back_time)
        otp_code = GOTP.check_mail(email=E_MAIL, ts=ts)
        
        otp_submit = OTP.otp_submit()
        otp_input = OTP.otp_input()
        time.sleep(15)
        otp_input.send_keys(otp_code)

        with assume: assert otp_input.get_attribute("value") == otp_code
        with assume: assert "_s_btn-disabled-dark-100" not in otp_submit.get_attribute("class")


    @allure.title("Submit OTP")
    @allure.description("Please, edit and give detailed description for test step")
    def test_step_name(self):
        otp_submit = OTP.otp_submit()
        otp_submit.click()

        form_close = PFP.close_button()
        form_header = PFP.form_header()
        

        password_submit = PFP.password_submit()

        with assume: assert "_s_btn-disabled-purple" in password_submit.get_attribute("class")
        with assume: assert form_close.is_displayed() == True
        with assume: assert form_header.text == "შექმენი პაროლი"

    @allure.title("Enter password")
    @allure.description("enter password")
    def test_enter_password(self):
        password = PFP.gen_password()
        password_input = PFP.password_input()
        password_label = PFP.password_label()


        password_input_rep = PFP.repeat_password()
        password_label_rep = PFP.repeat_password_label()

        with assume: assert password_input.is_displayed() == True
        with assume: assert password_label.text == "პაროლი"
        with assume: assert password_input_rep.is_displayed() == True
        with assume: assert password_label_rep.text == "გაიმეორე პაროლი"

        password_input.send_keys(password)
        password_input_rep.send_keys(password)

    @allure.title("Agree TOC")
    @allure.description("Agree to TOC")
    def test_agree_toc(self):
        toc = PFP.toc()
        toc_text = PFP.toc_label()
        toc_link = PFP.toc_link()

        with assume: assert toc_text.text == "გავეცანი და ვეთანხმები"
        with assume: assert toc_link.text == "წესებსა და პირობებს"
        with assume: assert toc_link.get_attribute("href") == "https://extra.ge/customer-agreement"

        toc_text.click()

    @allure.title("Submit registration")
    @allure.description("Submit registration")
    def test_submit_registration(self):
        password_submit = PFP.password_submit()

        with assume: assert "_s_btn-disabled-purple" not in password_submit.get_attribute("class")
        
        password_submit.click()

    @allure.title("Confirmation")
    @allure.description("Registration confirmation")
    def test_confirmation(self):
        image = SP.image()
        close = SP.close_button()
        header = SP.header_text()
        text = SP.message()
        button = SP.button()

        with assume: assert image.is_displayed == True
        with assume: assert close.is_displayed == True
        with assume: assert header.text == "გილოცავ!"
        with assume: assert text.text == "შენ წარმატებით გაიარე რეგისტრაცია"
        with assume: assert button.is_displayed() == True
        with assume: assert button.text == "შესვლა"