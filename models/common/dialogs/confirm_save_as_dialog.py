from utils.logger import Logger

class ConfirmSaveAsDialog:
    """
    Components of Confirm Save As Dialog.
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

    def click_on_yes_button(self) -> None:
        """
        Clicks on Yes button.
        """
        self.loger.info("Clicks on Yes Button")
        yes_button = self.get_dialog_control("Yes", auto_id="CommandButton_6", control_type="Button")
        yes_button.click()
