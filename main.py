from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTextEdit, QPlainTextEdit, QPushButton, QFileDialog
from ASCCS import Ui_MainWindow
import sys

class ApplicationWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(ApplicationWindow, self).__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Browse button and Directory Dialoge.
		self.button = self.findChild(QPushButton, 'pushButton')  # Find the button by object name
		self.button.clicked.connect(self.open_directory_dialog)  # Connect the button to the slot
		self.textEdit = self.findChild(QPlainTextEdit, "plainTextEdit")

		# Start button and command output.
		self.output_window = self.findChild(QTextEdit, 'textEdit')  # Find the QTextEdit by object name
		self.button = self.findChild(QPushButton, 'pushButton_2')  # Find the button by object name
		self.button.clicked.connect(self.start)  # Connect the button to the slot




	def open_directory_dialog(self):
		self.directory = QFileDialog.getExistingDirectory(self, "Select Directory")
		if self.directory:
			print(f"Selected Directory: {self.directory}")  # You can use the selected directory here
			self.textEdit.setPlainText(self.directory)  # Replaces the existing text

	def start(self):
		self.output_window.append(f"Processing files in {self.textEdit.toPlainText()}")
		self.output_window.append("Processing /document1...")
		self.output_window.append("Found Bill of Lading.")

		self.output_window.append("Processing /document2...")
		self.output_window.append("Found Commercial Invoice.")

		self.output_window.append("Processing /document3...")
		self.output_window.append("Found Delivery Order")

		self.output_window.append("Processing /document4...")
		self.output_window.append("Unrecognized document.")

		self.output_window.append("\nDocuments found: 3.\n[\nBill of Lading,\nCommercial Invoice,\nDelivery Order\n]")

		self.output_window.append("Unrecognized Documents: 1.")




def main():
	app = QtWidgets.QApplication(sys.argv)
	application = ApplicationWindow()
	application.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()