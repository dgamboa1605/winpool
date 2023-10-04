from utils.logger import Logger
from models.common.base_dialog import BaseDialog


class OpenDialog(BaseDialog):
    """
    Components of Open dialog.
    """
    
    loger = Logger(__name__)

    def __int__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog = dialog

    def click_on_open_button(self) -> None:
        """
        Clicks on Open button.
        """
        self.loger.info("Clisk on Open button")
        open_button = self.get_dialog_control("Open", auto_id="1", control_type="Button")
        open_button.click()
