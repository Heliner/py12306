from flask import Blueprint, request
from flask.json import jsonify
from flask_jwt_extended import (jwt_required)

from py12306.inner_config import Config, WebLoader

config = Blueprint('config', __name__)


@config.route('/config', methods=['GET'])
@jwt_required
def config_lists():
    """
    查询任务列表
    :return:
    """
    envs = Config.envs
    return jsonify(envs)


@config.route('/set-config', methods=['POST'])
@jwt_required
def config_lists():
    """
    查询任务列表
    :return:
    """
    req_config = request.json.get('data', None)

    web_loader = WebLoader()
    web_loader.set_2_envs(Config(), req_config)
    Config.save_config_2_file(Config.NEW_JSON_CONFIG_FILE)
