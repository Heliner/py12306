import os

from py12306.helpers.func import singleton
from py12306.inner_config import Config

@singleton
class WebStarter():
    @classmethod
    def open_manager_web(cls):
        home_page_url = 'http://localhost:{}/'.format(Config().WEB_PORT)
        cmd = 'start {}'.format(home_page_url)
        _ = os.system(cmd)

