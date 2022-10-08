#!/usr/bin/env python3

from os import mkdir
from os.path import exists

from core.base.storage import Storage
from core.utils.file import get_system, get_distro
from core.settings import (
    FILE,
    FOLDER_CONFIG,
    FOLDER_PROFILE,
    FOLDER_LOG
)


class BaseConfig():

    def __init__(
            self,
            module: str = None,
            category: str = None,
            value: str = None,
            file_config: str = FILE.get("config"),
            file_profile: str = FILE.get("profile"),
            folder_config: str = FOLDER_CONFIG,
            folder_profile: str = FOLDER_PROFILE,
            folder_log: str = FOLDER_LOG):
        """
        Structure that defines the main variables.
        """
        self.module = module
        self.category = category
        self.value = value

        self.file_config = file_config
        self.file_profile = file_profile
        self.folder_config = folder_config
        self.folder_profile = folder_profile
        self.folder_log = folder_log

        self.set_folder()

        self.class_profile = Storage(database=self.file_profile)
        self.class_config = Storage(database=self.file_config)

        self.setup()

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.add_config()
        self.load_config()
        self.load_profile()

    def set_folder(self) -> None:
        """
        Setup Folder

        Checks and creates the structure of configuration
        folders that are used by the package.
        """
        folders = [
            self.folder_config,
            self.folder_profile,
            self.folder_log,
        ]
        for folder in folders:
            if not exists(folder):
                mkdir(folder)

    def add_config(self):
        """
        Configuring system settings

        Function that configures the basic settings of the
        operating system that the LinuxProfle package is running.

        Saved in the linux_config.json configuration file more
        specifically Hardware and Distribution information.
        """
        self.class_config.begin(module='info', tag='distro')
        if not len(self.class_config.search_tag('distro')):
            self.class_config.run(content=get_distro())

        self.class_config.begin(module='info', tag='system')
        if not len(self.class_config.search_tag('system')):
            self.class_config.run(content=get_system())

    def load_config(self) -> None:
        """
        Load Config

        Loads basic configuration information for use
        in the application and internal operations.
        """
        self.config = self.class_config.load()

    def load_profile(self) -> None:
        """
        Load Profile

        Load basic information from profiles for use in the
        application and internal operations.
        """
        self.profile = self.class_profile.load()
