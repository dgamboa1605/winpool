class ConfirmSaveAsDialog:
    def __init__(self, dialog) -> None:
        self.dialog = dialog

    def get_dialog_control(self, identifier: str, auto_id: str = None, control_type: str = None):
        return self.dialog.child_window(title=identifier, auto_id=auto_id, control_type=control_type)

    def click_on_yes_button(self):
        yes_button = self.get_dialog_control("Yes", auto_id="CommandButton_6", control_type="Button")
        yes_button.click()
