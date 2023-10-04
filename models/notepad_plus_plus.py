from config import config
from utils.logger import Logger
from pywinauto import application, clipboard
from models.common.dialogs.open_dialog import OpenDialog
from models.common.dialogs.save_as_dialog import SaveAsDialog
from models.common.dialogs.confirm_save_as_dialog import ConfirmSaveAsDialog


class NotepadPlusPlus:
    """
    This class manage Notepad++ actions.
    """
    
    logger = Logger(__name__)
    
    def __init__(self):
        self.app = application.Application(backend="uia")
        self.app.start(config.RUN_APP)
        self.main_window = self.app.window(title_re=config.APP_NAME)

    def close(self) -> None:
        """
        This method will close Notepadd++ app.
        """
        self.logger.info("Notepadd++ closed")
        self.main_window.close()

    def new_file(self) -> None:
        """
        This method will create a new file.
        """
        self.logger.info("Creating new file: File -> New")
        self.main_window.menu_select("File -> New")

    def open_file(self, file_path: str, file_name: str) -> None:
        """
        This method will open a file with their path and name.
        Args:
            file_path (str): path of file.
            file_name (str): file name i.e. test.txt
        """
        self.logger.info("Open file: File -> Open with path:{} and file name:{}".format(
            file_path, 
            file_name)
        )
        self.main_window.menu_select("File -> Open...")
        open_dialog = OpenDialog(self.app.dlg.Open)
        open_dialog.set_path(file_path)
        open_dialog.set_file_name(file_name)
        open_dialog.click_on_open_button()

    def type_text(self, text: str) -> None:
        """
        This method will add text in the focus tab.
        Args:
            text (str): text to add in the focus file.
        """
        self.logger.info("Set the text as: {}".format(text))
        self.main_window.set_focus()
        self.main_window.type_keys(text, with_spaces=True)

    def save_file(self, file_path: str, file_name: str) -> None:
        """
        This method will save a file with their path and name.
        Args:
            file_path (str): path of file.
            file_name (str): file name i.e. test.txt
        """
        self.logger.info("Save file: File -> Save As with path:{} and file name:{}".format(
            file_path, 
            file_name)
        )
        self.main_window.menu_select("File -> Save As...")
        save_dialog = SaveAsDialog(self.app.dlg.SaveAs)
        save_dialog.set_path(file_path)
        save_dialog.set_file_name(file_name)
        save_dialog.click_on_save_button()
        confirm_dialog = ConfirmSaveAsDialog(self.app.dlg.ConfirmSaveAs)
        confirm_dialog.click_on_yes_button()

    def get_text_content(self) -> str:
        """
        This method will get a text of focus tab or file.
        Returns:
            str: text or content of a file.
        """
        self.main_window.set_focus()
        self.logger.info("Press Keys to copy a text: ctrl a + ctrl c")
        self.main_window.type_keys('^a^c')
        text = clipboard.GetData()
        self.logger.info("Text of file: {}".format(text))

        return text
