from config import config


class TestNotepadPlusPlus:

    def test_create_new_file(self, notepad_instance):
        notepad_instance.new_file()
        window_text = notepad_instance.main_window.window_text()
        assert " - Notepad++" in window_text

    def test_open_and_save_file(self, notepad_instance):
        notepad_instance.open_file(config.FILE_PATH, config.FILE_NAME)
        notepad_instance.type_text("Hello, Notepad++!")
        notepad_instance.save_file(config.FILE_PATH, config.FILE_NAME)
        assert "test_file.txt" in notepad_instance.main_window.window_text()

    def test_edit_text_content(self, notepad_instance):
        notepad_instance.open_file(config.FILE_PATH, config.FILE_NAME)
        notepad_instance.type_text("Editing text in Notepad ")
        actual_result = notepad_instance.get_text_content()
        notepad_instance.save_file(config.FILE_PATH, config.FILE_NAME)
        assert "Editing text in Notepad " in actual_result
