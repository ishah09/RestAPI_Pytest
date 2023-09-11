import os
import yaml


class ConfigfileReader(object):

    def __init__(self, pstr_current_path):
        self.dir_path = self.get_proj_dirpath()
        self.base_config = self.read_base_config_file()
        self.path = pstr_current_path

    def get_project_path(self):
        """
        Description:
        |  This method fetches path of the root Project folder

        :return: String
        """
        try:
            return os.path.dirname(self.dir_path)
        except Exception as e:
            print("Error in get_project_path method-->" + str(e))

    def get_proj_dirpath(self):
        return os.path.abspath(os.getcwd())

    def get_config_filepath(self):
        """
        Description:
            |  This method fetches path of config.yml

        :return: String
        """
        try:
            str_filepath = self.get_proj_dirpath() + os.path.sep + "config.yml"
            return str_filepath
        except Exception as e:
            print("Error in get_config_filepath method-->" + str(e))

    def read_base_config_file(self):
        """
        Description:
            |  This method reads base config.yml file and loads the content into a dictionary object.

        :return: Dictionary
        """

        config = None
        try:
            with open(self.get_config_filepath(), 'r') as config_yml:
                config = yaml.safe_load(config_yml)
        except Exception as e:
            pass

        if config is None:
            raise Exception("Error Occurred while reading a config file")
        return config

    def get_baseurl(self):
        """

        :return:
        """
        try:
            return self.base_config.get("baseurl")
        except Exception as e:
            print("Error in fetch_execution_environment method-->" + str(e))
