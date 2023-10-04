from config import config
from pywinauto import application, clipboard
from models.common.dialogs.open_dialog import OpenDialog
from models.common.dialogs.save_as_dialog import SaveAsDialog
from models.common.dialogs.confirm_save_as_dialog import ConfirmSaveAsDialog


class NotepadPlusPlus:
    def __init__(self):
        self.app = application.Application(backend="uia")
        self.app.start(config.RUN_APP)
        self.main_window = self.app.window(title_re=config.APP_NAME)

    def close(self):
        self.main_window.close()

    def new_file(self):
        self.main_window.menu_select("File -> New")

    def open_file(self, file_path, file_name):
        self.main_window.menu_select("File -> Open...")
        open_dialog = OpenDialog(self.app.dlg.Open)
        open_dialog.set_path(file_path)
        open_dialog.set_file_name(file_name)
        open_dialog.click_on_open_button()

    def type_text(self, text):
        self.main_window.set_focus()
        self.main_window.type_keys(text, with_spaces=True)

    def save_file(self, file_path, file_name):
        self.main_window.menu_select("File -> Save As...")
        save_dialog = SaveAsDialog(self.app.dlg.SaveAs)
        save_dialog.set_path(file_path)
        save_dialog.set_file_name(file_name)
        save_dialog.click_on_save_button()
        confirm_dialog = ConfirmSaveAsDialog(self.app.dlg.ConfirmSaveAs)
        confirm_dialog.click_on_yes_button()

    def get_text_content(self):
        self.main_window.set_focus()
        self.main_window.type_keys('^a^c')
        text = clipboard.GetData()

        return text
