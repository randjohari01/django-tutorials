from channels.testing import ChannelsLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

class TestChat(ChannelsLiveServerTestCase):
    serve_static = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        try:
            cls.driver = webdriver.Chrome()
        except:
            super().tearDownClass()
            raise

    @classmethod        
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_same_room(self):

        try:
            self._enter_chat_room("room_1")
            self._open_new_window()
            self._enter_chat_room("room_1")

            self._switch_to_window(0)
            self._post_message("hello")

            WebDriverWait(self.driver , 2).until(
                lambda _: "hello" in self._chat_log_value , "message was not received from w1 to w1"
            )


            self._switch_to_window(1)
            WebDriverWait(self.driver , 2).until(
                lambda _: "hello" in self._chat_log_value , "message was not found from w1 to w2"
            )
        finally:
            self._close_all_news_windows()

    def test_different_room(self):

        try:
            self._enter_chat_room("room_1")
            self._open_new_window()
            self._enter_chat_room("room_2")

            self._switch_to_window(0)
            self._post_message("hello")

            WebDriverWait(self.driver , 2).until(
                lambda _: "hello" in self._chat_log_value , "message was not received from R1 to R1"
            )


            self._switch_to_window(1)
            self._post_message("world")
            WebDriverWait(self.driver , 2).until(
                lambda _: "world" in self._chat_log_value , "message was not received from R2 to R2"
            )

            self.assertTrue(
                "hello" not in self._chat_log_value, "message was received from r1 to r2!!"
            )


        finally:
            self._close_all_news_windows()



    def _enter_chat_room(self , room_name):
            self.driver.get(self.live_server_url + "/chat/")
            ActionChains(self.driver).send_keys(room_name, Keys.ENTER).perform()
            WebDriverWait(self.driver,  2).until(
                lambda _: room_name in self.driver.current_url
            )

    def _open_new_window(self):
            self.driver.execute_script('window.open("about:blank", "_blank");')
            self._switch_to_window(-1)    

    def _close_all_news_windows(self):
            while len(self.driver.window_handles) > 1:
                self._switch_to_window(-1)
                self.driver.execute_script('window.close();')
            if len(self.driver.window_handles) == 1:
                self._switch_to_window(0)    

    def _switch_to_window(self , window_index):
            self.driver.switch_to.window(self.driver.window_handles[window_index])    

    def _post_message(self , message):
            ActionChains(self.driver).send_keys(message , Keys.ENTER).perform()    

    @property
    def _chat_log_value(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value="#chat-log").get_property("value")    