import os
import pytest
from utils.logger import Logger
from config import config
from models.notepad_plus_plus import NotepadPlusPlus

loger = Logger(__name__)

def create_file(file_path=config.FULL_PATH):
    if os.path.exists(file_path):
        loger.info("File '{}' already exists.".format(file_path))
    else:
        with open(file_path, 'w') as file:
            file.write("This is the content.")
        loger.info("File '{}' created.".format(file_path))


def delete_file(file_path=config.FULL_PATH):
    loger.info("File is deleted in the path: {}".format(file_path))
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
