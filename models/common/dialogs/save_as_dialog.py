from models.common.base_dialog import BaseDialog


class SaveAsDialog(BaseDialog):

    def __int__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog = dialog

    def click_on_save_button(self) -> None:
        open_button = self.get_dialog_control("Save", auto_id="1", control_type="Button")
        open_button.click()
