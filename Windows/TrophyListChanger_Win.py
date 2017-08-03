# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrophyList.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QApplication, QClipboard
from PyQt5.QtWidgets import QFileDialog
from bs4 import BeautifulSoup
import multiprocessing
import requests

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName('Dialog')
        Dialog.resize(858, 545)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Dialog.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logo/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(-1, 8, -1, 12)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName('verticalLayout')
        self.label_logo = QtWidgets.QLabel(Dialog)
        self.label_logo.setPixmap(QtGui.QPixmap(':/Logo/Logo.png'))
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName('label_logo')
        self.verticalLayout.addWidget(self.label_logo)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName('tabWidget')
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName('tab')
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName('gridLayout')
        self.lineEdit_URL = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_URL.setObjectName('lineEdit_URL')
        self.gridLayout.addWidget(self.lineEdit_URL, 1, 0, 1, 1)
        self.pushButton_SaveImage = QtWidgets.QPushButton(self.tab)
        self.pushButton_SaveImage.setEnabled(True)
        self.pushButton_SaveImage.setObjectName('pushButton_SaveImage')
        self.gridLayout.addWidget(self.pushButton_SaveImage, 1, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setObjectName('textBrowser')
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 2)
        self.label_URL = QtWidgets.QLabel(self.tab)
        self.label_URL.setObjectName('label_URL')
        self.gridLayout.addWidget(self.label_URL, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName('label_4')
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, '')
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName('tab_2')
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.label_URL_2 = QtWidgets.QLabel(self.tab_2)
        self.label_URL_2.setObjectName('label_URL_2')
        self.verticalLayout_2.addWidget(self.label_URL_2)
        self.lineEdit_URL_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_URL_2.setObjectName('lineEdit_URL_2')
        self.verticalLayout_2.addWidget(self.lineEdit_URL_2)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName('label_3')
        self.verticalLayout_2.addWidget(self.label_3)
        self.plainTextEdit_NaverTag = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_NaverTag.setObjectName('plainTextEdit_NaverTag')
        self.verticalLayout_2.addWidget(self.plainTextEdit_NaverTag)
        self.pushButton_html = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_html.setObjectName('pushButton_html')
        self.verticalLayout_2.addWidget(self.pushButton_html)
        self.tabWidget.addTab(self.tab_2, '')
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName('tab_3')
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName('verticalLayout_3')
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setObjectName('label_5')
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setObjectName('label_6')
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setObjectName('label_14')
        self.verticalLayout_3.addWidget(self.label_14)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setObjectName('label_7')
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setObjectName('label_8')
        self.verticalLayout_3.addWidget(self.label_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setObjectName('label_9')
        self.verticalLayout_3.addWidget(self.label_9)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName('label_10')
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName('label_11')
        self.verticalLayout_3.addWidget(self.label_11)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setObjectName('label_12')
        self.verticalLayout_3.addWidget(self.label_12)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setObjectName('label_13')
        self.verticalLayout_3.addWidget(self.label_13)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setObjectName('label_16')
        self.verticalLayout_3.addWidget(self.label_16)
        self.tabWidget.addTab(self.tab_3, '')
        self.verticalLayout.addWidget(self.tabWidget)
        self.label_15 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName('label_15')
        self.verticalLayout.addWidget(self.label_15)

        # signal
        self.pushButton_SaveImage.clicked.connect(self.pushButton_SaveImage_Clicked)
        self.pushButton_html.clicked.connect(self.pushButton_html_Clicked)
        #

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Variable
    platinum_trophy = '<img id="http://cafefiles.naver.net/20111222_198/kazenonakae_1324553334353FLhM7_png/platinum_kazenonakae.png" src="http://cafefiles.naver.net/20111222_198/kazenonakae_1324553334353FLhM7_png/platinum_kazenonakae.png" width="17" height="17">'
    gold_trophy = '<img id="http://cafefiles.naver.net/20111222_224/kazenonakae_1324553335909tYHyj_png/trophy_gold_kazenonakae.png" src="http://cafefiles.naver.net/20111222_224/kazenonakae_1324553335909tYHyj_png/trophy_gold_kazenonakae.png" width="17" height="17">'
    silver_trophy = '<img id="http://cafefiles.naver.net/20111222_139/kazenonakae_1324553373393dyJXS_png/trophy_silver_kazenonakae.png" src="http://cafefiles.naver.net/20111222_139/kazenonakae_1324553373393dyJXS_png/trophy_silver_kazenonakae.png" width="17" height="17">'
    bronze_trophy = '<img id="http://cafefiles.naver.net/20111222_112/kazenonakae_1324553335738GqDMQ_png/trophy_bronze_kazenonakae.png" src="http://cafefiles.naver.net/20111222_112/kazenonakae_1324553335738GqDMQ_png/trophy_bronze_kazenonakae.png" width="17" height="17">'
    hidden_trophy = '<img id="http://cafefiles.naver.net/20111222_286/kazenonakae_1324553373601atvu6_png/trophy_hidden7_kazenonakae.png" src="http://cafefiles.naver.net/20111222_286/kazenonakae_1324553373601atvu6_png/trophy_hidden7_kazenonakae.png" width="17" height="17">'
    space = '&nbsp;'

    hidden_name_list = []
    source_list = []

    trophy_count = ''

    trophy_info_tag = ''

    process = []

    main_url = ''

    dir = ''
    #

    # slot
    def pushButton_SaveImage_Clicked(self):
        self.textBrowser.clear()
        self.main_url = ''
        self.dir = ''
        self.dir = str(QFileDialog.getExistingDirectory())

        if self.dir != '':
            try:
                self.dir += '/'
                # self.textBrowser.append(self.dir + " 경로에 다운로드")
                self.main_url = self.lineEdit_URL.text()
                req = requests.get(self.main_url)

                p = multiprocessing.Process(target=self.SaveImage, args=(self.main_url,))
                self.process.append(p)
                p.start()

                self.textBrowser.append("이미지 태그 추출 완료")
                self.textBrowser.append(self.dir + ' 경로에 모든 이미지 백그라운드 다운로드 중 ...')
            except:
                    self.textBrowser.append("올바른 링크를 입력해주세요.")
    def pushButton_html_Clicked(self):
            self.get_trophy_info_tag(self.lineEdit_URL_2.text()+'?lang=ko&secret=hide')
            self.get_trophy_tag(self.lineEdit_URL_2.text()+'?lang=ko')
    #

    # function
    def SaveImage(self, _url):
        self.process = []
        req = requests.get(_url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        trophy_main_img_holder = soup.find("div", "game-image-holder")
        trophy_main_img = trophy_main_img_holder.a.get('href')
        trophy_img = soup.find_all("picture")

        for picture_tag in trophy_img:
            img_tag = picture_tag.find_all("img")
            for img in img_tag:
                url = img.get("src")
                filename = url.split("/")[-1]
                r = requests.get(url)
                with open(self.dir+filename, 'wb') as f:
                    f.write(r.content)

        filename = trophy_main_img.split("/")[-1]
        r = requests.get(trophy_main_img)
        with open(self.dir + filename, 'wb') as f:
            f.write(r.content)

    def get_trophy_info_tag(self, url):
        self.hidden_name_list = []
        self.source_list = []
        try:
            req = requests.get(url) # PSN Profiles 링크
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            # 게임 제목
            title_name = soup.find("span", "breadcrumb-arrow").next_sibling

            # 트로피 갯수
            platinum = soup.find("li", "icon-sprite platinum").get_text()
            gold = soup.find("li", "icon-sprite gold").get_text()
            silver = soup.find("li", "icon-sprite silver").get_text()
            bronze = soup.find("li", "icon-sprite bronze").get_text()
            hidden = 0

            # 총 트로피 갯수
            self.trophy_count = soup.find("span", "small-info floatr").b.get_text()

            # 숨겨진 트로피 조사
            hidden_trophy_table = soup.find_all("td", style="width: 100%;")

            for td_tag in hidden_trophy_table:
                a_tag = td_tag.find_all('a')
                for name in a_tag:
                    self.hidden_name_list.append(name.string)

            if len(self.hidden_name_list) > int(self.trophy_count):  # 총 트로피 수 보다 가져온 리스트 수가 더 많을 시 첫번째 인덱스 삭제
                del self.hidden_name_list[0]

            for match in self.hidden_name_list:
                if match == 'Secret Trophy':
                    hidden += 1

            html_doc = self.plainTextEdit_NaverTag.toPlainText() # 네이버에 등록한 태그
            naver_tag = BeautifulSoup(html_doc, 'html.parser')
            list_source = naver_tag.find_all("img")

            for source in list_source:
              self.source_list.append(str(source)) # 네이버에 등록한 태그 리스트에 저장

            trophy_info_img = self.source_list[-1] # 마지막에 등록된 이미지는 메인 이미지로 저장
            del self.source_list[-1] # 메인 이미지 리스트에서 삭제

            self.trophy_info_tag = (
                '<center>' + trophy_info_img + '<br><br>' +
                '<span style="font-family: Verdana; font-size: 14pt;"><b>' +
                '<font color="#000000">' + title_name + ' 트로피 리스트' + '</span><br><br>' +
                '<span style="font-family: Verdana; font-size: 14pt;">' +
                '<font color="#0075c8">' + self.platinum_trophy + self.space + platinum + self.space + '</font>' +
                '<font color="#d1b274">' + self.gold_trophy + self.space + gold + self.space + '</font>' +
                '<font color="#acacac">' + self.silver_trophy + self.space + silver + self.space + '</font>' +
                '<font color="#951015">' + self.bronze_trophy + self.space + bronze + self.space + '</font>' +
                '<font color="#000000">' + self.hidden_trophy + self.space + str(hidden) + '</font>' +
                '</b></span>' + '</center>' + '<br>'
            )
            # self.plainTextEdit_NaverTag.setPlainText(self.trophy_info_tag)
        except:
            self.plainTextEdit_NaverTag.setPlainText("올바른 링크와 태그를 입력해주세요.")
    def get_trophy_tag(self, url):
        name_list = []
        content_list = []
        grade_list = []
        trophy_tag = ''
        try:
            req = requests.get(url) # PSN Profiles 링크
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            # 트로피 제목, 내용 조사
            trophy_table = soup.find_all("td", style="width: 100%;")
            # 트로피 등급 조사
            trophy_grade = soup.find_all("span", "separator left")

            for td_tag in trophy_table:  # 트로피 제목
                a_tag = td_tag.find_all("a")
                for name in a_tag:
                    name_list.append(name.string)

            if len(name_list) > int(self.trophy_count):  # 총 트로피 수 보다 가져온 리스트 수가 더 많을 시 첫번째 인덱스 삭제
                del name_list[0]

            for br_tag in trophy_table:  # 트로피 내용
                content_list.append(br_tag.br.next_sibling)

            if len(content_list) > int(self.trophy_count):  # 총 트로피 수 보다 가져온 리스트 수가 더 많을 시 첫번째 인덱스 삭제
                del content_list[0]

            for img_tag in trophy_grade:  # 트로피 등급
                trophy = img_tag.find_all("img")
                for grade in trophy:
                    grade_list.append(grade.get("title"))

            list_count = 0

            while list_count < int(self.trophy_count):
                grade = ''
                hidden = ''

                if grade_list[list_count] == 'Platinum':
                    grade = self.platinum_trophy
                elif grade_list[list_count] == 'Gold':
                    grade = self.gold_trophy
                elif grade_list[list_count] == 'Silver':
                    grade = self.silver_trophy
                elif grade_list[list_count] == 'Bronze':
                    grade = self.bronze_trophy

                if self.hidden_name_list[list_count] == 'Secret Trophy':
                    hidden = self.hidden_trophy

                trophy_tag += (
                    '<span style="font-family: Verdana; font-size: 9pt;">' +
                    self.source_list[list_count] + self.space +
                    '<b>' + name_list[list_count] + '</b>' + self.space + grade + hidden + '<br>' +
                    content_list[list_count] + '</span><br><br>'
                )
                list_count += 1
            full_tag = self.trophy_info_tag + trophy_tag
            clipboard = QApplication.clipboard()
            clipboard.setText(full_tag)
            # pyperclip.copy(full_tag)

            self.plainTextEdit_NaverTag.setPlainText("변환이 완료되어 클립보드에 복사되었습니다. 태그를 붙여넣기 하세요.")
        except:
            self.plainTextEdit_NaverTag.setPlainText("올바른 링크와 태그를 입력해주세요.")
    #

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate('Dialog', 'PSTC - 트로피 리스트 html 변환 자동화'))
        self.pushButton_SaveImage.setText(_translate('Dialog', '이미지 저장'))
        self.label_URL.setText(_translate('Dialog', '아래 입력란에 PSN Profiles 링크를 입력해주세요. (예: https://psnprofiles.com/trophies/5992-무쌍스타즈)'))
        self.label_4.setText(_translate('Dialog', '결과'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate('Dialog', '트로피 이미지'))
        self.label_URL_2.setText(_translate('Dialog', '아래 입력란에 PSN Profiles 링크를 입력해주세요. (예: https://psnprofiles.com/trophies/5992-무쌍스타즈)'))
        self.label_3.setText(_translate('Dialog', '네이버에 등록한 이미지의 html 태그를 아래에 붙여 넣어주세요.'))
        self.pushButton_html.setText(_translate('Dialog', '트로피 리스트 html 변환'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate('Dialog', 'html 변환'))
        self.label_5.setText(_translate('Dialog', '1. PSN Profiles 링크를 복사해 "트로피 이미지" 탭에 붙여넣은 뒤 "이미지 저장" 버튼을 누르면 트로피 이미지가 컴퓨터에 저장됩니다.'))
        self.label_6.setText(_translate('Dialog', '(예: https://psnprofiles.com/trophies/5992-무쌍스타즈)'))
        self.label_14.setText(_translate('Dialog', '※ 만약 "이미지 저장" 버튼이 활성화되지 않는다면 링크를 제대로 입력했는지 확인하세요.'))
        self.label_7.setText(_translate('Dialog', '2. 카페 글쓰기를 누르고 기본으로 저장된 양식을 전부 지운뒤 트로피 이미지들을 전부 업로드 합니다.'))
        self.label_8.setText(_translate('Dialog', '(저장된 순서대로 업로드 했다면 이미지 제일 마지막에 메인 이미지가 업로드 됩니다.)'))
        self.label_9.setText(_translate('Dialog', '3. 글쓰기 영역 우측 상단에 있는 html을 체크하고 나타나는 모든 내용을 복사해 "html 변환" 탭에 붙여 넣습니다.'))
        self.label_10.setText(_translate('Dialog', '4. 다시 PSN Profiles의 링크를 붙여넣고 맨 아래의 변환 버튼을 누릅니다.'))
        self.label_11.setText(_translate('Dialog', '(변환된 태그는 자동으로 클립보드에 복사됩니다.)'))
        self.label_12.setText(_translate('Dialog', '5. 글쓰기 영역 우측 상단에 있는 html을 체크하고 모든 내용을 지운뒤 복사된 태그를 붙여 넣습니다.'))
        self.label_13.setText(_translate('Dialog', '6. html 체크를 해제하고 "확인" 버튼을 눌러 글작성을 완료합니다.'))
        self.label_16.setText(_translate('Dialog', ''))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate('Dialog', '사용 방법'))
        self.label_15.setText(_translate('Dialog', '1.0.3 | 앰아 (M-AHHH)'))

import resource_rc

if __name__ == '__main__':
    multiprocessing.freeze_support()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
