from flask import Blueprint, request
from flask.json import jsonify
from flask_jwt_extended import (jwt_required)

from py12306.inner_config import Config, WebLoader

config = Blueprint('config', __name__)


@config.route('/config', methods=['GET'])
@jwt_required
def get_config():
    """
    查询任务列表
    :return:
    """
    _conf = Config()
    envs = _conf.parse_envs_2_dict(_conf.envs)
    response = jsonify(envs)
    return response


@config.route('/set-config', methods=['POST'])
@jwt_required
def set_config():
    """
    查询任务列表
    :return:
    """
    req_config = request.json

    web_loader = WebLoader()
    _conf = Config()
    web_loader.set_2_config(_conf, req_config)
    web_loader.set_2_envs(_conf, req_config)
    _conf.save_config_2_file(_conf.NEW_JSON_CONFIG_FILE)
    response = jsonify(dict())
    return response

