import yaml

def load_yaml(config_dir, db_config_file):
    return yaml.load(open("{}/{}".format(config_dir, db_config_file) ))