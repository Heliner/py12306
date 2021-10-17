from flask import Blueprint
from flask.json import jsonify
from flask_jwt_extended import (jwt_required)

from py12306.inner_config import Config

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
