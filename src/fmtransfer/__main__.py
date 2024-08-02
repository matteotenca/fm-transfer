import sys
from PyQt6.QtWidgets import QApplication
import fmtransfer

def _main() -> None:
    app = QApplication(sys.argv)
    fm_transfer = fmtransfer.FmTransfer()
    fm_transfer.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    _main()