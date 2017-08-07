# coding=utf-8
import six
from nekbot.utils.modules import import_string
from . import global_settings

__author__ = 'nekmo'


class Settings(object):
    def __init__(self, defaults=global_settings):
        self.write_conf(defaults)  # Primero guardo la configuración global

    def configure(self, mod):
        """Módulo (archivo de configuración) donde se encuentran los parámetros con
        la configuración del usuario. Esta sobrescribirá la global
        """
        if isinstance(mod, six.string_types):
            mod = import_string(mod)
        self.write_conf(mod)

    def write_conf(self, settings_mod, prevent_override=False):
        for setting in dir(settings_mod):
            if prevent_override and hasattr(self, setting):
                continue
            if setting.isupper():
                self.set(setting, getattr(settings_mod, setting))

    def set(self, key, value):
        setattr(self, key, value)

settings = Settings()
