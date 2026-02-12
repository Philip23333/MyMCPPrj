
from utils.path_tool import get_abs_path
import yaml

CONFIGS_DIR = "configs/"

def load_config_by_name(config_name:str,encoding='utf-8'):

    abs_config_path = get_abs_path(CONFIGS_DIR + config_name + '.yml')
    with open(abs_config_path, 'r', encoding=encoding) as f:
        return yaml.full_load(f)


if __name__ == '__main__':
    config_name = 'agent'
    config = load_config_by_name(config_name)
    for i in config:
        print(f"{i}:{config[i]}")
