from config import config
from utils.logger import Logger


class TestNotepadPlusPlus:
    """
    Test for Notead++.
    """
    
    loger = Logger(__name__)

    def test_create_new_file(self, notepad_instance):
        self.loger.info("Start Test: test_create_new_file")
        notepad_instance.new_file()
        window_text = notepad_instance.main_window.window_text()
        assert " - Notepad++" in window_text
        self.loger.info("Test Passed: Windows text is created as: {}".format(window_text))

    def test_open_and_save_file(self, notepad_instance):
        self.loger.info("Start Test: test_open_and_save_file")
        notepad_instance.open_file(config.FILE_PATH, config.FILE_NAME)
        notepad_instance.type_text("Hello")
        notepad_instance.save_file(config.FILE_PATH, config.FILE_NAME)
        assert "test_file.txt" in notepad_instance.main_window.window_text()
        self.loger.info("Test Passed: File is opened and saved")

    def test_edit_text_content(self, notepad_instance):
        self.loger.info("Start Test: test_edit_text_content")
        notepad_instance.open_file(config.FILE_PATH, config.FILE_NAME)
        notepad_instance.type_text("Editing text in Notepad ")
        actual_result = notepad_instance.get_text_content()
        notepad_instance.save_file(config.FILE_PATH, config.FILE_NAME)
        assert "Editing text in Notepad " in actual_result
        self.loger.info("Test Passed: File is edited and saved")
