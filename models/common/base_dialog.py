class BaseDialog:
    def __init__(self, dialog) -> None:
        self.dialog = dialog

    def get_dialog_control(self, identifier: str, auto_id: str = None, control_type: str = None):
        return self.dialog.child_window(title=identifier, auto_id=auto_id, control_type=control_type)

    def set_path(self, path: str) -> None:
        address_band = self.get_dialog_control("Address band")
        address_band.type_keys('%D' + path + "{ENTER}")

    def set_file_name(self, file_name: str) -> None:
        file = self.get_dialog_control("File name:", control_type="Edit")
        file.set_text(file_name)
