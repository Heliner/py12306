import json

from env import USER_ACCOUNTS
from py12306.inner_config import Config


class TestLoadFromFile(object):

    def test_from_file(self, ):
        cnf = Config()
        res = cnf.init_envs_from_json()
        print("test load_data_from_file res :\n{}".format(res))
        print("test disallow_update_configs :\n{}".format(repr(cnf.disallow_update_configs)))

        print("test to dict :\ndict:\n{}\n{}".format(cnf.__dict__, json.dumps(cnf.__dict__)))
        cnf.save_config_2_file(cnf.NEW_JSON_CONFIG_FILE)

    def test_2_json(self, ):
        print(json.dumps(USER_ACCOUNTS))
        print(json.loads(json.dumps(USER_ACCOUNTS)))

    # def test_config_lists(self):
    # print("test config list :{}".format(jsonify(Config.envs)))


if __name__ == '__main__':
    test = TestLoadFromFile()
    test.test_from_file()
    # test.test_dump()
    # test.test_2_json()
    # test.test_config_lists()
