from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SnipeIT Users w/ no assets")
        self.resize(400, 300)

        self.list_widget = QtWidgets.QListWidget()
        self.setCentralWidget(self.list_widget)

        self.refresh_button = QtWidgets.QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh)

        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addWidget(self.refresh_button)

        self.refresh()

    def refresh(self):
        self.list_widget.clear()

        url = "https://terrafirma.snipe-it.io/api/v1/users"
        headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZDNmYzRiNjZhYTJiYmJmN2FhODBjMzAxMTUzOGNlNjUyMGFkYTkzYzhhZjM4MzU4ODhlODBmNDU4OTRjOTk4YWRmMzc1ZWY1Y2VkNGVjZjUiLCJpYXQiOjE2NjY2MzE0OTguMjE5MjIxLCJuYmYiOjE2NjY2MzE0OTguMjE5MjI4LCJleHAiOjIyOTc3ODcwOTguMjA2NzkyLCJzdWIiOiIyMTQiLCJzY29wZXMiOltdfQ.d7Sxo0PtTxsgeoPyyS8lHEm_RQtLLyh0XSxeeOgirCUpU-2dT5h0cgM-2kkskVUELoDANRpFcy2pOBCSDGN-x5P1WV2z1MVoIXTXTXBBUT9GKtpIhl9K9-5fbT4X12sviUhgJHcCpxpl45gU7XjZvOFzH4KMr89-tiVCRP-RjpaLwvGPMrGKk2JLV5M3472Icw_JPaL25ZPhnHHPxOeSgva9ZBYkzyspr8IMqzqdp04kUcxTt3xWitdXkRSRuO4jh5ydWfPEPDMYXFPZx_eZS7TVFof1pz6fDi9GPGRxxkxvq4uVYquQYufvZcOd9BqTRYOkcJCYZI_gnpQo1jDP5VlY6po1yNDoFsKt4mHq0r_A3ord5_cO7O_h3rWYZEN-QHYshMvua3laSK1IFyAO_z4by1C_7xNybeaRSktX7HVAntTjTS62yFkcVQoKc6gxD5KSVpWcNFxtXaqKarz_zIuvB3Rtu75GyC-P_-wN4szQRogf3_RE_mtpKpycarCuNsZkd0hSBawuoSNLPMyeGQOjtQ8b74I22Mb9dSwctALwF8UyB5JMfFJU1FaRnfwPfr5PwCXoIS3I2_-eThAjjemfJWIPqESP3J8GiG4GfWB56vph5Q7xrfDlgduvHExppl5W5WiBWc4WyVeuddByLRHDCudhtEbYgVMkEKljjO8"
        }

        response = requests.get(url, headers=headers)
        users = response.json()["rows"]

        for user in users:
            if user["assets_count"] == 0:
                    self.list_widget.addItem(user["first_name"] + " " + user["last_name"])
           

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()