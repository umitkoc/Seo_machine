from datetime import datetime
from sys import argv, exit
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

from bs4 import BeautifulSoup as bs
from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QTableWidget, QTableWidgetItem)
from requests.api import get


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SEO Machine")
        self.Urls()
        self.table()
        self.table_col()
        self.table_row()
        self.buttons()
        self.input()

        self.index = 1
        self.tag = ["h1", "h2", "h3", "h4", "h5",
                    "h6", "img", "p", "a", "bold", "italic"]
        self.tag3 = ["h1", "h2", "h3", "h4", "h5", "h6",
                     "p", "a", "bold", "italic", "img", "meta"]
        self.showMaximized()

    def Urls(self):
        self.loading = QLabel(self)
        self.loading.setText("")
        self.loading.move(1100, 80)
        self.loading.setFont(QFont('Arial', 18))
        #########
        self.url1_lbl = QLabel(self)
        self.url1_lbl.setText("Url1:")
        self.url1_lbl.move(10, 10)
        ##########
        self.url1 = QLineEdit(self)
        self.url1.resize(350, 30)
        self.url1.move(35, 10)
        self.url1.setPlaceholderText("Url1")
        ##########
        self.url2_lbl = QLabel(self)
        self.url2_lbl.setText("Url2:")
        self.url2_lbl.move(10, 50)
        #########
        self.url2 = QLineEdit(self)
        self.url2.resize(350, 30)
        self.url2.move(35, 50)
        self.url2.setPlaceholderText("Url2")
        ########
        self.url3_lbl = QLabel(self)
        self.url3_lbl.setText("Url3:")
        self.url3_lbl.move(10, 90)
        #########
        self.url3 = QLineEdit(self)
        self.url3.resize(350, 30)
        self.url3.setPlaceholderText("Url3")
        self.url3.move(35, 90)
        ########
        self.url4_lbl = QLabel(self)
        self.url4_lbl.setText("Url4:")
        self.url4_lbl.move(400, 10)
        #########
        self.url4 = QLineEdit(self)
        self.url4.setPlaceholderText("Url4")
        self.url4.resize(350, 30)
        self.url4.move(425, 10)
        ########
        self.url5_lbl = QLabel(self)
        self.url5_lbl.setText("Url5:")
        self.url5_lbl.move(400, 50)
        #########
        self.url5 = QLineEdit(self)
        self.url5.move(425, 50)
        self.url5.setPlaceholderText("Url5")
        self.url5.resize(350, 30)
        ########
        self.url6_lbl = QLabel(self)
        self.url6_lbl.setText("Url6:")
        self.url6_lbl.move(400, 90)
        #########
        self.url6 = QLineEdit(self)
        self.url6.move(425, 90)
        self.url6.setPlaceholderText("Url6")
        self.url6.resize(350, 30)

    def buttons(self):
        self.start_button = QPushButton(self)
        self.start_button.setText("Başla")
        self.start_button.resize(100, 100)
        self.start_button.move(1650, 10)
        self.start_button.setStyleSheet("background-color:green;color:white;")
        try:
            self.start_button.clicked.connect(self.start)
        except:
            print("hatalı")
        #######
        self.reset_button = QPushButton(self)
        self.reset_button.setText("Reset")
        self.reset_button.resize(100, 100)
        self.reset_button.move(1780, 10)
        self.reset_button.setStyleSheet("background-color:red;color:white;")
        self.reset_button.clicked.connect(self.reset)

    def input(self):
        self.input_lbl = QLabel(self)
        self.input_lbl.move(1100, 15)
        self.input_lbl.setText("Kelimeler")

        #########
        self.input_text = QLineEdit(self)
        self.input_text.move(950, 50)
        self.input_text.resize(350, 30)
        self.input_text.setPlaceholderText("Kelimeleri ekleyiniz...")

    def start(self):
        self.loading.setText("")
        try:
            self.table1.clear()
            self.table_col()
            self.table_row()
            self.cut()
            self.tags()
            self.table_3()
            for n in self.array_text:
                self.table2.setItem(self.index, 0, QTableWidgetItem(n))
                self.search_word(n)
            j = 1
            for i in self.array_url:
                if i != "":
                    self.search_tag(i, j)
                j += 1
            for j in range(1, len(self.tag)+1):
                ortalama = 0
                step = 1
                sayac = 0
                for i in self.array_url:
                    if i != "" and step < 6:
                        ortalama += float(self.table1.item(j, step).text())
                        sayac += 1
                    step += 1
                self.table1.setItem(
                    j, 6, QTableWidgetItem(f"{ortalama/sayac}"))
                if float(self.table1.item(j, 6).text()) < float(self.table1.item(j, 7).text()):
                    self.table1.setItem(j, 8, QTableWidgetItem("yüksek"))
                elif float(self.table1.item(j, 6).text()) > float(self.table1.item(j, 7).text()):
                    self.table1.setItem(j, 8, QTableWidgetItem("düşük"))
                else:
                    self.table1.setItem(j, 8, QTableWidgetItem("eşittir"))
        except:
            self.loading.setText("hata var")

    def search_word(self, value):
        j = 1
        ortalama = 0
        sayac = 0
        for i in self.array_url:
            if i != "":
                r = get(i)
                if j == 6:
                    j += 1
                html = bs(r.content.lower(), 'html.parser')
                texts = len(str(html.find('body')).split(value))-1
                if texts < 0:
                    texts = 0
                self.table2.setItem(
                    self.index, j, QTableWidgetItem(f"{texts}"))
                if j < 6:
                    ortalama += texts
                    sayac += 1

            j += 1
        self.table2.setItem(
            self.index, 6, QTableWidgetItem(f"{ortalama/sayac}"))
        if float(self.table2.item(self.index, 6).text()) < float(self.table2.item(self.index, 7).text()):
            self.table2.setItem(self.index, 8, QTableWidgetItem("yüksek"))
        elif float(self.table2.item(self.index, 6).text()) > float(self.table2.item(self.index, 7).text()):
            self.table2.setItem(self.index, 8, QTableWidgetItem("düşük"))
        else:
            self.table2.setItem(self.index, 8, QTableWidgetItem("eşittir"))
        self.index += 1

    def tags(self):
        self.array_url = []
        self.array_url.append(self.url1.text())
        self.array_url.append(self.url2.text())
        self.array_url.append(self.url3.text())
        self.array_url.append(self.url4.text())
        self.array_url.append(self.url5.text())
        self.array_url.append(self.url6.text())

    def reset(self):
        self.table1.clear()
        self.table2.clear()
        self.table3.clear()
        self.url1.clear()
        self.url2.clear()
        self.url3.clear()
        self.url4.clear()
        self.url5.clear()
        self.url6.clear()
        self.table_col()
        self.table_row()
        self.input_text.clear()
        self.index = 1

    def cut(self):
        self.array_text = self.input_text.text().split(",")
        self.array_text.sort()

    def table(self):
        self.table1 = QTableWidget(self)
        self.table1.setColumnCount(9)
        self.table1.setRowCount(12)
        self.table1.move(10, 130)
        self.table1.resize(500, 400)
        ##########
        self.table2 = QTableWidget(self)
        self.table2.setColumnCount(9)
        self.table2.setRowCount(100)
        self.table2.move(10, 550)
        self.table2.resize(500, 450)
        ##########
        self.table3 = QTableWidget(self)
        self.table3.setColumnCount(7)
        self.table3.setRowCount(13)
        self.table3.move(520, 130)
        self.table3.resize(1400, 870)

    def table_row(self):
        self.table1.setItem(1, 0, QTableWidgetItem("h1"))
        self.table1.setItem(2, 0, QTableWidgetItem("h2"))
        self.table1.setItem(3, 0, QTableWidgetItem("h3"))
        self.table1.setItem(4, 0, QTableWidgetItem("h4"))
        self.table1.setItem(5, 0, QTableWidgetItem("h5"))
        self.table1.setItem(6, 0, QTableWidgetItem("h6"))
        self.table1.setItem(7, 0, QTableWidgetItem("img"))
        self.table1.setItem(8, 0, QTableWidgetItem("p"))
        self.table1.setItem(9, 0, QTableWidgetItem("anchor"))
        self.table1.setItem(10, 0, QTableWidgetItem("bold"))
        self.table1.setItem(11, 0, QTableWidgetItem("italic"))

        self.table1.setItem(0, 0, QTableWidgetItem("etiketler"))
        self.table1.setItem(0, 1, QTableWidgetItem("url1"))
        self.table1.setItem(0, 2, QTableWidgetItem("url2"))
        self.table1.setItem(0, 3, QTableWidgetItem("url3"))
        self.table1.setItem(0, 4, QTableWidgetItem("url4"))
        self.table1.setItem(0, 5, QTableWidgetItem("url5"))
        self.table1.setItem(0, 6, QTableWidgetItem("ortalama"))
        self.table1.setItem(0, 7, QTableWidgetItem("url6"))
        self.table1.setItem(0, 8, QTableWidgetItem("durum"))

        width1 = self.table1.verticalHeader()
        width1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        width1.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        width1.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        width1.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        width1.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        width1.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        width1.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        width1.setSectionResizeMode(8, QtWidgets.QHeaderView.Stretch)
        width1.setSectionResizeMode(9, QtWidgets.QHeaderView.Stretch)
        width1.setSectionResizeMode(10, QtWidgets.QHeaderView.Stretch)
        width1.setSectionResizeMode(11, QtWidgets.QHeaderView.Stretch)

        header1 = self.table1.horizontalHeader()
        header1.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header1.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header1.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header1.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header1.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header1.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header1.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header1.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        header1.setSectionResizeMode(8, QtWidgets.QHeaderView.Interactive)
        self.table1.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table1.setWordWrap(True)
        self.table1.horizontalHeader().setVisible(False)
        self.table1.verticalHeader().setVisible(False)
        #######

        self.table3.setItem(0, 0, QTableWidgetItem("etiketler"))
        self.table3.setItem(0, 1, QTableWidgetItem("url1"))
        self.table3.setItem(0, 2, QTableWidgetItem("url2"))
        self.table3.setItem(0, 3, QTableWidgetItem("url3"))
        self.table3.setItem(0, 4, QTableWidgetItem("url4"))
        self.table3.setItem(0, 5, QTableWidgetItem("url5"))
        self.table3.setItem(0, 6, QTableWidgetItem("url6"))
        width3 = self.table3.verticalHeader()
        width3.setSectionResizeMode(1, QtWidgets.QHeaderView.Interactive)
        width3.setSectionResizeMode(2, QtWidgets.QHeaderView.Interactive)
        width3.setSectionResizeMode(3, QtWidgets.QHeaderView.Interactive)
        width3.setSectionResizeMode(4, QtWidgets.QHeaderView.Interactive)
        width3.setSectionResizeMode(5, QtWidgets.QHeaderView.Interactive)
        width3.setSectionResizeMode(6, QtWidgets.QHeaderView.Interactive)
        width3.setSectionResizeMode(7, QtWidgets.QHeaderView.Interactive)
        width3.setSectionResizeMode(8, QtWidgets.QHeaderView.Interactive)
        width3.setSectionResizeMode(9, QtWidgets.QHeaderView.Interactive)
        width3.setSectionResizeMode(10, QtWidgets.QHeaderView.Interactive)
        width3.setSectionResizeMode(11, QtWidgets.QHeaderView.Interactive)
        width3.setSectionResizeMode(12, QtWidgets.QHeaderView.Interactive)

        header3 = self.table3.horizontalHeader()
        header3.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header3.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header3.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header3.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header3.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header3.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header3.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        self.table3.setWordWrap(True)
        #######
        self.table3.setItem(1, 0, QTableWidgetItem("h1"))
        self.table3.setItem(2, 0, QTableWidgetItem("h2"))
        self.table3.setItem(3, 0, QTableWidgetItem("h3"))
        self.table3.setItem(4, 0, QTableWidgetItem("h4"))
        self.table3.setItem(5, 0, QTableWidgetItem("h5"))
        self.table3.setItem(6, 0, QTableWidgetItem("h6"))
        self.table3.setItem(7, 0, QTableWidgetItem("p"))
        self.table3.setItem(8, 0, QTableWidgetItem("anchor"))
        self.table3.setItem(9, 0, QTableWidgetItem("bold"))
        self.table3.setItem(10, 0, QTableWidgetItem("italic"))
        self.table3.setItem(11, 0, QTableWidgetItem("img"))
        self.table3.setItem(12, 0, QTableWidgetItem("meta"))
        # self.table3.horizontalHeader().setVisible(False)
        # self.table3.verticalHeader().setVisible(False)
        self.table3.setSelectionBehavior(QAbstractItemView.SelectRows)

    def table_col(self):

        self.table2.setItem(0, 0, QTableWidgetItem("kelimeler"))
        self.table2.setItem(0, 1, QTableWidgetItem("url1"))
        self.table2.setItem(0, 2, QTableWidgetItem("url2"))
        self.table2.setItem(0, 3, QTableWidgetItem("url3"))
        self.table2.setItem(0, 4, QTableWidgetItem("url4"))
        self.table2.setItem(0, 5, QTableWidgetItem("url5"))
        self.table2.setItem(0, 6, QTableWidgetItem("ortalama"))
        self.table2.setItem(0, 7, QTableWidgetItem("url6"))
        self.table2.setItem(0, 8, QTableWidgetItem("durum"))
        self.table2.setWordWrap(True)
        header = self.table2.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.Interactive)
        self.table2.horizontalHeader().setVisible(False)
        self.table2.verticalHeader().setVisible(False)
        self.table2.setSelectionBehavior(QAbstractItemView.SelectRows)

    def search_tag(self, url, value):
        if value == 6:
            value += 1
        j = 1
        r = get(url)
        html = bs(r.content.lower(), 'html.parser')
        for i in self.tag:
            texts = 0
            if i == 'img':
                texts = len(str(html.find('body')).split('<img'))-len(
                    str(html.find('footer')).split('<img'))-len(
                    str(html.find('header')).split('<img'))+1
                if texts < 0:
                    texts = 0
            elif i == 'a':
                p = html.find_all('a')
                for i in p:
                    if str(i.text).strip() != "":
                        dizi = str(i.text).split(" ")
                        texts += len(dizi)
            elif i == 'p':
                p = html.find_all('p')
                for i in p:
                    if str(i.text).strip() != "":
                        dizi = str(i.text).split(" ")
                        texts += len(dizi)
            elif i == 'bold':
                p = html.find_all('bold')
                for i in p:
                    if str(i.text).strip() != "":
                        dizi = str(i.text).split(" ")
                        texts += len(dizi)
            elif i == 'italic':
                p = html.find_all('italic')
                for i in p:
                    if str(i.text).strip() != "":
                        dizi = str(i.text).split(" ")
                        texts += len(dizi)

            else:
                texts = len(html.find_all(i))
            self.table1.setItem(j, value, QTableWidgetItem(f"{texts}"))
            j += 1

    def table_3(self):
        x = 1
        y = 1
        for i in self.array_url:
            if i != "":
                r = get(i)
                html = bs(r.content.lower(), 'html.parser')
                y = 1
                for tags in self.tag3:
                    sonuc = ""
                    kelime = ""
                    if tags == "meta":
                        try:
                            kelime = html.find("meta", property="og:title")[
                                "content"]
                        except:
                            kelime = html.find("title").text
                    else:
                        liste = html.find_all(tags)
                        for l in liste:
                            if str(l.text).strip() != "":
                                kelime += str(l.text)
                    for texts in self.array_text:
                        k = 0
                        k += len(kelime.split(texts))
                        if k > 1:
                            sonuc += f"{texts}:{k-1}\n"
                    self.end(y, x, sonuc)
                    # self.table3.setItem(y, x, QTableWidgetItem(f"{sonuc}"))
                    y = y+1
            x = x+1

    def end(self, y, x, sonuc):
        sonuc = str(sonuc).replace("\n", ":").split(":")
        i = 0
        while i < len(sonuc):
            j = i+2
            l = sonuc[i]
            while j < len(sonuc)-1:
                m = sonuc[j]
                if m.find(l) > -1:
                    sonuc[i+1] = str(int(sonuc[i+1])-int(sonuc[j+1]))
                j += 2
            i += 2
        kelime = ""
        i = 0
        while i < len(sonuc)-1:
            kelime += sonuc[i]
            if int(sonuc[i+1]) > 0:
                kelime += f":{sonuc[i+1]}\n"
            i += 2
        self.table3.setItem(y, x, QTableWidgetItem(f"{kelime}"))
if __name__ == "__main__":
    app = QApplication(argv)
    main = Main()
    main.show()
    exit(app.exec_())
