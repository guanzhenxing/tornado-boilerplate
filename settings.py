import json
import os

import tornado.template
from tornado.options import define, options

from environment import init_environment

init_environment()  # 初始化环境参数

define("config_file", default=None, help="filename for additional configuration")
define("env", default="SOLO", help="Deployment Configuration.Values: SOLO,DEV,QA,UAT,PROD")
tornado.options.parse_command_line()


# Deployment Configuration
class DeploymentType:
    SOLO = "SOLO"  # 也就是本地模式
    DEV = "DEV"
    QA = "QA"
    UAT = "UAT"
    PROD = "PROD"
    dict = {
        SOLO: "SOLO",
        DEV: "DEV",
        QA: "QA",
        UAT: "UAT",
        PROD: "PROD"
    }


# Make filepaths relative to settings.
here = os.path.dirname(os.path.abspath(__file__))
pardir = os.path.abspath(os.path.join(here, os.path.pardir))

path = lambda root, *a: os.path.join(root, *a)


def init_config():
    """
    init config
    :return: config
    """
    config_file = path(here, 'conf/application.json')
    if options.config_file:
        config_file = options.config_file

    default_config = {
        'port': 8000,
        'log_file': path(pardir, 'log')
    }
    with open(config_file) as f:
        custom_config = json.load(f)

    return {**default_config, **custom_config}


def init_app_settings():
    """
    init app_settings
    :return:
    """
    if options.env in [DeploymentType.PROD, DeploymentType.UAT]:
        app_debug = True
    else:
        app_debug = False

    return {
        'debug': app_debug,
        'static_path': path(here, 'static'),
        'template_path': path(here, 'templates')
    }


# 获得配置
config = init_config()

# 获得 app_settings
app_settings = init_app_settings()
