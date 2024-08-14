from utils.logger import Logger

class BaseDialog:
    """
    Base components of dialogs.
    """
    
    loger = Logger(__name__)
    
    def __init__(self, dialog) -> None:
        self.dialog = dialog

    def get_dialog_control(self, identifier: str, auto_id: str = None, control_type: str = None) -> None:
        """
        Get a dialog control like Open, Save As, Confirm Save As, etc.
        Args:
            identifier (str): identifier of dialog to get control.
            auto_id (str, optional): auto identifier. Defaults to None.
            control_type (str, optional): control type. Defaults to None.
        """
        self.loger.info("Get a dialog by identifier: {}".format(identifier))
        self.loger.debug("Get a dialog by auto_id: {}, control_type: {}".format(auto_id, control_type))
        return self.dialog.child_window(title=identifier, auto_id=auto_id, control_type=control_type)

    def set_path(self, path: str) -> None:
        """
        Set path of the file that will be search.
        Args:
            path (str): file path to search.
        """
        self.loger.info("Set path to search a file: {}".format(path))
        address_band = self.get_dialog_control("Address band")
        address_band.type_keys('%D' + path + "{ENTER}")

    def set_file_name(self, file_name: str) -> None:
        """
        Set file name of the file that will be search.
        Args:
            file_name (str): file name to search.
        """
        self.loger.info("Set file name to search as: {}".format(file_name))
        file = self.get_dialog_control("File name:", control_type="Edit")
        file.set_text(file_name)
