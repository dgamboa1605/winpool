import os
import pytest
from config import config
from models.notepad_plus_plus import NotepadPlusPlus


def create_file(file_path=config.FULL_PATH):
    if os.path.exists(file_path):
        print("File '{}' already exists.".format(file_path))
    else:
        with open(file_path, 'w') as file:
            file.write("This is the content.")
        print("File '{}' created.".format(file_path))


def delete_file(file_path=config.FULL_PATH):
    os.remove(file_path)


@pytest.fixture(scope="class")
def notepad_instance(request):
    notepad = NotepadPlusPlus()
    create_file()

    def teardown():
        notepad.close()
        delete_file()

    request.addfinalizer(teardown)
    return notepad
