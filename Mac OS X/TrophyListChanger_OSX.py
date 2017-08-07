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
import requests
import multiprocessing

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
        self.pushButton_SaveImage.clicked.connect(self.pushButton_SaveImage_Clicked) # 이미지 저장 버튼 슬롯 연결
        self.pushButton_html.clicked.connect(self.pushButton_html_Clicked) # html 변환 버튼 슬롯 연결
        #

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # slot
    def pushButton_SaveImage_Clicked(self):
        self.textBrowser.clear()
        self.dir_path = '' # 저장 경로
        self.dir_path = str(QFileDialog.getExistingDirectory()) # 다이얼로그에서 선택한 경로 저장

        if self.dir_path != '': # 다이얼로그 취소시 '' 저장 # 다이얼로그 취소가 아니면
            try:
                self.dir_path = self.dir_path + '/' # 파일 이름을 붙이기전 '/' 추가
                main_url = self.lineEdit_URL.text() # 링크 입력창에 붙여넣은 URL 가져옴

                req = requests.get(main_url) # 링크를 입력하지 않았거나 잘못된 링크 입력시 여기서 에러 발생
                html = req.text
                soup = BeautifulSoup(html, 'html.parser')

                # DLC가 없는 상황을 대비한 메인이미지 추출
                trophy_main_img_holder = soup.find("div", "game-image-holder")
                trophy_main_img = trophy_main_img_holder.a.get('href')

                trophy_main_img_list = []
                trophy_main_img_list.append(trophy_main_img)

                # DLC가 있는 상황의 메인 + 모든 이미지
                trophy_img = soup.find_all("picture")

                # 멀티 프로세싱 OSX
                q = multiprocessing.Queue() # 큐 생성

                for picture_tag in trophy_img:  # 트로피 이미지
                    img_tag = picture_tag.find_all("img")
                    for img in img_tag:
                        src = img.get("src")
                        IsTrophy = True # 트로피 이미지
                        proc = multiprocessing.Process(target=self.Download_Image, args=(src, q, IsTrophy)) # 태그 수 만큼 프로세서 생성
                        proc.start() # 시작

                IsTrophy = False # 트로피 메인 이미지
                proc = multiprocessing.Process(target=self.Download_Image, args=(trophy_main_img, q, IsTrophy))
                proc.start()  # 시작

                qcount = len(trophy_img) + len(trophy_main_img_list) # 다운로드 받게 되는 링크 개수 총 합

                for filename in range(qcount): # 큐에 저장된 정보를 링크 개수 만큼 가져옴
                    filename = q.get()
                    self.textBrowser.append(filename + " 다운로드 완료")

            except:
                self.textBrowser.setText("올바른 링크를 입력해주세요.")

    def pushButton_html_Clicked(self):
        # 트로피 메인 정보를 위한 태그 size 17px 17px
        platinum_trophy = '<img id="http://cafefiles.naver.net/20111222_198/kazenonakae_1324553334353FLhM7_png/platinum_kazenonakae.png" src="http://cafefiles.naver.net/20111222_198/kazenonakae_1324553334353FLhM7_png/platinum_kazenonakae.png" width="17" height="17">'
        gold_trophy = '<img id="http://cafefiles.naver.net/20111222_224/kazenonakae_1324553335909tYHyj_png/trophy_gold_kazenonakae.png" src="http://cafefiles.naver.net/20111222_224/kazenonakae_1324553335909tYHyj_png/trophy_gold_kazenonakae.png" width="17" height="17">'
        silver_trophy = '<img id="http://cafefiles.naver.net/20111222_139/kazenonakae_1324553373393dyJXS_png/trophy_silver_kazenonakae.png" src="http://cafefiles.naver.net/20111222_139/kazenonakae_1324553373393dyJXS_png/trophy_silver_kazenonakae.png" width="17" height="17">'
        bronze_trophy = '<img id="http://cafefiles.naver.net/20111222_112/kazenonakae_1324553335738GqDMQ_png/trophy_bronze_kazenonakae.png" src="http://cafefiles.naver.net/20111222_112/kazenonakae_1324553335738GqDMQ_png/trophy_bronze_kazenonakae.png" width="17" height="17">'
        hidden_trophy = '<img id="http://cafefiles.naver.net/20111222_286/kazenonakae_1324553373601atvu6_png/trophy_hidden7_kazenonakae.png" src="http://cafefiles.naver.net/20111222_286/kazenonakae_1324553373601atvu6_png/trophy_hidden7_kazenonakae.png" width="17" height="17">'

        # DLC 메인 정보를 위한 태그 size 15px 15px
        division_platinum_trophy = '<img id="http://cafefiles.naver.net/20111222_198/kazenonakae_1324553334353FLhM7_png/platinum_kazenonakae.png" src="http://cafefiles.naver.net/20111222_198/kazenonakae_1324553334353FLhM7_png/platinum_kazenonakae.png" width="15" height="15">'
        division_gold_trophy = '<img id="http://cafefiles.naver.net/20111222_224/kazenonakae_1324553335909tYHyj_png/trophy_gold_kazenonakae.png" src="http://cafefiles.naver.net/20111222_224/kazenonakae_1324553335909tYHyj_png/trophy_gold_kazenonakae.png" width="15" height="15">'
        division_silver_trophy = '<img id="http://cafefiles.naver.net/20111222_139/kazenonakae_1324553373393dyJXS_png/trophy_silver_kazenonakae.png" src="http://cafefiles.naver.net/20111222_139/kazenonakae_1324553373393dyJXS_png/trophy_silver_kazenonakae.png" width="15" height="15">'
        division_bronze_trophy = '<img id="http://cafefiles.naver.net/20111222_112/kazenonakae_1324553335738GqDMQ_png/trophy_bronze_kazenonakae.png" src="http://cafefiles.naver.net/20111222_112/kazenonakae_1324553335738GqDMQ_png/trophy_bronze_kazenonakae.png" width="15" height="15">'
        division_hidden_trophy = '<img id="http://cafefiles.naver.net/20111222_286/kazenonakae_1324553373601atvu6_png/trophy_hidden7_kazenonakae.png" src="http://cafefiles.naver.net/20111222_286/kazenonakae_1324553373601atvu6_png/trophy_hidden7_kazenonakae.png" width="15" height="15">'

        space = '&nbsp;'

        try:

            main_url = self.lineEdit_URL_2.text() + '?lang=ko' # 한국어 검색을 위해 입력 링크에 자동으로 붙임
            hidden_url = main_url + '&secret=hide' # 숨겨진 트로피 식별을 위해 입력 링크에 자동으로 붙임

            req = requests.get(main_url) # 잘못된 링크를 입력하거나 빈칸일 시 여기서 에러 발생
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            # 게임 제목 # 성공
            title_name = soup.find("span", "breadcrumb-arrow").next_sibling

            # 총 트로피 갯수 # 성공
            all_trophy_count = 0  # 총 트로피 갯수 0 으로 초기화
            division_trophy_count_list = []  # base, DLC 1, DLC 2, DLC 3 ...

            trophy_count = soup.find_all("span", "small-info floatr")
            for trophies in trophy_count:
                aaa = int(trophies.b.get_text())  # 태그 별 트로피 갯수 비교 후 가장 큰 값을 총 트로피 갯수로 저장
                division_trophy_count_list.append(aaa)  # base, DLC 1, DLC 2, DLC3 ... 순서대로 저장
                if all_trophy_count < aaa:
                    all_trophy_count = aaa # 가져온 모든 수 중 가장 큰 값을 총 트로피 개수로 저장

            del division_trophy_count_list[-1]  # 총 트로피 개수 삭제

            # 개별 트로피 갯수 # 성공
            platinum_trophy_count = soup.find("li", "icon-sprite platinum").get_text()  # 플래티넘은 어차피 1개이기 때문에 상관없음 # 플래티넘 트로피 성공

            gold_trophy_count = 0  # 골드 트로피 갯수 0으로 초기화 # 골드 트로피 성공
            division_gold_trophy_count_list = []  # base, DLC 1, DLC 2, DLC 3 ...

            gold = soup.find_all("li", "icon-sprite gold")
            for gold_trophies in gold:
                aaa = int(gold_trophies.get_text())
                division_gold_trophy_count_list.append(aaa)  # base, DLC 1, DLC 2, DLC3 ... 순서대로 저장
                if gold_trophy_count < aaa:
                    gold_trophy_count = aaa # 가져온 모든 수 중 가장 큰 값을 총 골드 트로피 개수로 저장

            del division_gold_trophy_count_list[-1]  # 총 골드 트로피 개수 삭제

            silver_trophy_count = 0  # 실버 트로피 갯수 0으로 초기화 # 실버 트로피 성공
            division_silver_trophy_count_list = []  # base, DLC 1, DLC 2, DLC 3 ...

            silver = soup.find_all("li", "icon-sprite silver")
            for silver_trophies in silver:
                aaa = int(silver_trophies.get_text())
                division_silver_trophy_count_list.append(aaa)  # base, DLC 1, DLC 2, DLC3 ... 순서대로 저장
                if silver_trophy_count < aaa:
                    silver_trophy_count = aaa # 가져온 모든 수 중 가장 큰 값을 총 실버 트로피 개수로 저장

            del division_silver_trophy_count_list[-1]  # 총 실버 트로피 개수 삭제

            bronze_trophy_count = 0  # 브론즈 트로피 갯수 0으로 초기화 # 브론즈 트로피 성공
            division_bronze_trophy_count_list = []  # base, DLC 1, DLC 2, DLC 3 ...

            bronze = soup.find_all("li", "icon-sprite bronze")
            for bronze_trophies in bronze:
                aaa = int(bronze_trophies.get_text())
                division_bronze_trophy_count_list.append(aaa)  # base, DLC 1, DLC 2, DLC3 ... 순서대로 저장
                if bronze_trophy_count < aaa:
                    bronze_trophy_count = aaa # 가져온 모든 수 중 가장 큰 값을 총 브론즈 트로피 개수로 저장

            del division_bronze_trophy_count_list[-1]  # 총 브론즈 트로피 개수 삭제

            hidden_trophy_count = 0  # 히든 트로피 갯수 0으로 초기화 # 히든 트로피 성공

            hidden_req = requests.get(hidden_url)  # 히든 트로피만 url 따로 설정
            hidden_html = hidden_req.text
            hidden_soup = BeautifulSoup(hidden_html, 'html.parser')

            hidden_trophy_table = hidden_soup.find_all("td", style="width: 100%;")

            hidden_name_list = [] # 트로피 이름 저장

            for tag in hidden_trophy_table:
                a = tag.find_all("a")
                for text in a:
                    name = text.get_text()
                    hidden_name_list.append(name) # "a" 링크에서 내용만 저장

            for match in hidden_name_list:
                if match == 'Secret Trophy':  # 저장된 이름이 Secret Trophy면
                    hidden_trophy_count += 1  # 갯수 1씩 증가

            # 디비전 별 숨겨진 트로피 검색
            division_hidden_trophy_count_list = [] # 각 디비전별 트로피 개수 리스트로 저장
            division_count = 0 # 디비전 순서
            count = 0 # 트로피 이름 저장 리스트 순서

            while division_count < len(division_trophy_count_list): # 디비전 순서가 리스트의 길이보다 작으면 # Base, DLC 3개면 리스트의 길이는 4가 된다.
                search_count = 0  # 디비전 별 검색 횟수 # 다음 디비전을 위해 초기화
                hidden_search_count = 0  # 디비전 별 숨겨진 틀피 개수 # 다음 디비전을 위해 초기화
                while search_count < division_trophy_count_list[division_count]: # 디비전 별 트로피 개수만큼 검색
                    if hidden_name_list[count] == 'Secret Trophy': # 그 중 트로피 이름이 Secret Trophy면
                        hidden_search_count += 1 # 디비전 별 숨겨진 트로피 개수 증가

                    count += 1 # 트로피 이름 저장 리스트 인덱스 증가
                    search_count += 1 # 검색할 다음 트로피 인덱스 증가

                division_count += 1 # 다음 디비전
                division_hidden_trophy_count_list.append(hidden_search_count) # 해당 디비전에서 찾은 숨겨진 트로피 개수 리스트에 저장

            # 트로피 제목 트로피 내용 # 성공
            trophy_name_list = [] # 트로피 이름 저장
            trophy_content_list = [] # 트로피 내용 저장
            platinum_content = '' # 플래티넘 트로피 내용 # None 방지

            all_trophy_table = soup.find_all("td", style="width: 100%;")

            for tag in all_trophy_table:
                a = tag.find_all("a")
                for text in a:
                    name = text.get_text()
                    trophy_name_list.append(name) # 모든 트로피 내용 중 링크 태그 a에 있는 내용을 트로피 이름으로 저장

            # all_count = 0 # 사용 중지
            find_platinum_content = 0 # 플래티넘 내용 검색 횟수

            for tag in all_trophy_table:
                text = tag.find_all("br")
                for content in text:
                    trophy_content_list.append(content.next_sibling) # 모든 트로피 내용 중 br 태그 다음에 있는 텍스트를 트로피 내용으로 저장

            for tag in all_trophy_table:  # 플래티넘 내용 가져오기
                text = tag.stripped_strings # 트로피 테이블 중 텍스트 전부 가져옴 # 트로피 이름, 내용
                for content in text:
                    if find_platinum_content == 1: # 인덱스 0은 플래티넘 트로피 제목. 인덱스 1이면
                        platinum_content = content # 해당 내용 플래티넘 내용으로 저장
                        break  # 플래티넘 내용만 얻은 뒤 탈출
                    find_platinum_content += 1 # 인덱스 증가

                    # if (all_count % 2) == 0: # 짝수는 이름, 홀수는 내용 판별
                    #     pass
                    #     # name_list.append(content) # 트로피 이름 # 사용 중지
                    # else:
                    #     content_list.append(content) # 트로피 내용 # 사용 중지
                    # all_count+=1 # 사용 중지
                break  # 탈출

            trophy_content_list[0] = platinum_content  # 리스트 인덱스 0에 있는 None 값을 플래티넘 내용으로 변경

            # 트로피 등급 # 성공
            grade_list = [] # 트로피 등급 저장
            trophy_grade = soup.find_all("span", "separator left")

            for img_tag in trophy_grade:  # 트로피 등급
                trophy = img_tag.find_all("img")
                for grade in trophy:
                    grade_list.append(grade.get("title")) # 트로피 등급 제목 리스트에 저장 Platinum, Gold, Silver, Bronze

            # 네이버 태그
            naver_tag_list = []  # 네이버 태그 리스트
            naver_tag_img_list = []  # 이미지 태그 개별 저장
            naver_tag = self.plainTextEdit_NaverTag.toPlainText() # 사용자가 붙여넣은 태그 저장

            naver_tag_list = BeautifulSoup(naver_tag, 'html.parser').find_all("img")

            for tag in naver_tag_list:
                naver_tag_img_list.append(str(tag)) # 이미지 태그 분리하여 리스트에 저장

            # DLC 유무
            no_dlc_game_count = all_trophy_count + 1 # DLC가 없는 단일 게임은 총 트로피 개수 + 메인 이미지 수
            yes_dlc_game_count = len(naver_tag_list) # DLC가 있는 게임은 분리한 이미지 태그 수 # DLC 이미지 추가 시 NO DLC 개수를 넘어서기 때문에 자동판별

            # trophy_main_img = naver_tag_img_list[-1]  # 마지막에 있는 메인이미지 태그만 저장
            # del naver_tag_img_list[-1]  # 메인이미지 태그 삭제

            trophy_main_img = naver_tag_img_list[all_trophy_count]  # 리스트는 0번 부터 시작 # 마지막 트로피 다음에 있는 이미지

            trophy_info_tag = (
                '<center>' + trophy_main_img + '<br><br>' +
                '<span style="font-family: Verdana; font-size: 14pt;"><b>' +
                '<font color="#000000">' + title_name + ' 트로피 리스트' + '<br>' +
                '(' + title_name + ')' + '</font></span><br>' +
                '<br><span style="font-family: Verdana; font-size: 14pt;">' +
                '<font color="#0075c8">' + platinum_trophy + space + str(platinum_trophy_count) + space + '</font>' +
                '<font color="#d1b274">' + gold_trophy + space + str(gold_trophy_count) + space + '</font>' +
                '<font color="#acacac">' + silver_trophy + space + str(silver_trophy_count) + space + '</font>' +
                '<font color="#951015">' + bronze_trophy + space + str(bronze_trophy_count) + space + '</font>' +
                '<font color="#000000">' + hidden_trophy + space + str(hidden_trophy_count) + '</font>' +
                '</b></span>' + '</center>' + '<br>'
            )

            # 디비전 별 트로피
            if no_dlc_game_count < yes_dlc_game_count: # Yes DLC 이미지 태그 개수가 No DLC 이미지 태그 개수 보다 크면 DLC가 있는 게임

                dlc_main_img = []  # base, DLC 1, DLC 2, DLC 3 ...
                dlc_count = all_trophy_count + 1  # 트로피 개수와 메인 이미지 개수의 합 인덱스 다음부터 DLC 메인 이미지 # ex) 총 트로피 15 + 메인 1 = 16 이므로 17부터 DLC 이미지
                while dlc_count < yes_dlc_game_count:
                    dlc_main_img.append(naver_tag_img_list[dlc_count]) # DLC 메인 이미지 저장
                    dlc_count += 1

                # print(dlc_main_img)

                division_name = [] # DLC 트로피 메인 제목

                division_name_span = soup.find_all("span", "title")
                for tag in division_name_span:
                    division_name.append(tag.get_text()) # DLC 트로피 메인 제목 저장

                # print(division_name)

                division_count = 0 # 디비전 순서 # 0 BaseGame, 1 DLC#1, 2 DLC#2 ...
                i = 0 # 트로피 등급 리스트 인덱스

                division_full_tag = [] # 디비전 별 메인 정보 저장 리스트
                division_trophy_full_tag = [] # 디비전 별 트로피 저장 리스트

                while division_count < len(division_trophy_count_list): # 디비전 순서 < 디비전 개수
                    division_tag = ''
                    if division_name[division_count] == 'Base Game': # 인덱스 0은 BaseGame으로 번역문이 필요 없음
                        division_tag += (
                            '<center>' + dlc_main_img[division_count] + '<br>' +
                            '<span style="font-family: Verdana; font-size: 11pt;"><b>' +
                            division_name[division_count] + '<br><br>' +
                            '<font color="#0075c8">' + division_platinum_trophy + space + str(
                                platinum_trophy_count) + space + '</font>' +
                            '<font color="#d1b274">' + division_gold_trophy + space + str(
                                division_gold_trophy_count_list[division_count]) + space + '</font>' +
                            '<font color="#acacac">' + division_silver_trophy + space + str(
                                division_silver_trophy_count_list[division_count]) + space + '</font>' +
                            '<font color="#951015">' + division_bronze_trophy + space + str(
                                division_bronze_trophy_count_list[division_count]) + space + '</font>' +
                            '<font color="#000000">' + division_hidden_trophy + space + str(
                                division_hidden_trophy_count_list[division_count]) + '</font>' +
                            '</span>' + '</b></center>' + '<br>'
                        )
                    else: # BaseGame을 제외한 DLC# 메인 정보
                        division_tag += (
                            '<center>' + dlc_main_img[division_count] + '<br>' +
                            '<span style="font-family: Verdana; font-size: 11pt;"><b>' +
                            'DLC Pack #' + str(division_count) + ': ' + division_name[division_count] + '<br>' + # DLC 제목 번역문 자리
                            '(DLC Pack #' + str(division_count) + ': ' + division_name[ # DLC 제목 원문 자리
                                division_count] + ')' + '<br><br>' +
                            '<font color="#d1b274">' + division_gold_trophy + space + str(
                                division_gold_trophy_count_list[division_count]) + space + '</font>' +
                            '<font color="#acacac">' + division_silver_trophy + space + str(
                                division_silver_trophy_count_list[division_count]) + space + '</font>' +
                            '<font color="#951015">' + division_bronze_trophy + space + str(
                                division_bronze_trophy_count_list[division_count]) + space + '</font>' +
                            '<font color="#000000">' + division_hidden_trophy + space + str(
                                division_hidden_trophy_count_list[division_count]) + '</font>' +
                            '</span>' + '</b></center>' + '<br>'
                        )
                    division_full_tag.append(division_tag) # 변환된 디비전 태그 리스트에 순서대로 저장

                    # 트로피
                    trophy_tag = ''
                    search = 0 # 트로피 검색 개수 # 다음 디비전 때는 0으로 초기화 필요

                    while search < division_trophy_count_list[division_count]: # 트로피 검색 개수 < 리스트에 저장된 디비전 별 트로피 개수
                        grade = ''
                        hidden = ''

                        if grade_list[i] == 'Platinum': # 리스트에 저장된 내용이 Platinum이면 등급에 Platinum 트로피 이미지 태그 저장
                            grade = platinum_trophy
                        elif grade_list[i] == 'Gold': #
                            grade = gold_trophy
                        elif grade_list[i] == 'Silver': #
                            grade = silver_trophy
                        elif grade_list[i] == 'Bronze': #
                            grade = bronze_trophy

                        if hidden_name_list[i] == 'Secret Trophy': #리스트에 저장된 내용이 Secret Trophy이면 숨겨진 트로피 이미지 태그 저장
                            hidden = hidden_trophy

                        trophy_tag += (
                            '<span style="font-family: Verdana; font-size: 9pt;">' +
                            naver_tag_img_list[i] + space + # 트로피 순서에 맞는 이미지
                            '<b>' + trophy_name_list[i] + '</b>' + space + grade + hidden + '<br>' + # 트로피 순서에 맞는 제목과 등급, 숨겨진 트로피
                            trophy_content_list[i] + '</span><br><br>' # 트로피 순서에 맞는 내용
                        )

                        i += 1 # 트로피 등급 리스트 인덱스 증가
                        search += 1 # 다음 트로피 인덱스 증가

                    division_trophy_full_tag.append(trophy_tag) # 해당 디비전의 모든 트로피 태그 저장

                    division_count += 1 # 다음 디비전 인덱스 증가

                # 테스트
                # print(len(division_trophy_full_tag))

                text = ''

                for i in range(0, len(division_trophy_count_list)): # 모든 디비전 별 메인 정보와 트로피 정보 합침
                    text += division_full_tag[i] + division_trophy_full_tag[i]

                # pyperclip.copy(trophy_info_tag + text)

                full_tag = trophy_info_tag + text # 전체 트로피 메인 정보와 위에서 합친 정보를 합침
                clipboard = QApplication.clipboard()
                clipboard.setText(full_tag) # 클립보드에 복사

            else:
                trophy_main_img = naver_tag_img_list[-1]  # 마지막에 있는 메인이미지 태그만 저장
                del naver_tag_img_list[-1]  # 메인이미지 태그 삭제

                trophy_info_tag = (
                    '<center>' + trophy_main_img + '<br><br>' +
                    '<span style="font-family: Verdana; font-size: 14pt;"><b>' +
                    '<font color="#000000">' + title_name + ' 트로피 리스트' + '<br>' +
                    '(' + title_name + ')' + '</font></span><br>' +
                    '<br><span style="font-family: Verdana; font-size: 14pt;">' +
                    '<font color="#0075c8">' + platinum_trophy + space + str(
                        platinum_trophy_count) + space + '</font>' +
                    '<font color="#d1b274">' + gold_trophy + space + str(gold_trophy_count) + space + '</font>' +
                    '<font color="#acacac">' + silver_trophy + space + str(silver_trophy_count) + space + '</font>' +
                    '<font color="#951015">' + bronze_trophy + space + str(bronze_trophy_count) + space + '</font>' +
                    '<font color="#000000">' + hidden_trophy + space + str(hidden_trophy_count) + '</font>' +
                    '</b></span>' + '</center>' + '<br>'
                )
                # 트로피 등급 확인 후 태그 선정
                list_count = 0
                trophy_tag = ''
                while list_count < int(all_trophy_count):
                    grade = ''
                    hidden = ''

                    if grade_list[list_count] == 'Platinum':
                        grade = platinum_trophy
                    elif grade_list[list_count] == 'Gold':
                        grade = gold_trophy
                    elif grade_list[list_count] == 'Silver':
                        grade = silver_trophy
                    elif grade_list[list_count] == 'Bronze':
                        grade = bronze_trophy

                    if hidden_name_list[list_count] == 'Secret Trophy':
                        hidden = hidden_trophy

                    trophy_tag += (
                        '<span style="font-family: Verdana; font-size: 9pt;">' +
                        naver_tag_img_list[list_count] + space +
                        '<b>' + trophy_name_list[list_count] + '</b>' + space + grade + hidden + '<br>' +
                        trophy_content_list[list_count] + '</span><br><br>'
                    )
                    list_count += 1

                full_tag = trophy_info_tag + trophy_tag
                clipboard = QApplication.clipboard()
                clipboard.setText(full_tag)
                # pyperclip.copy(full_tag)

            self.plainTextEdit_NaverTag.setPlainText("변환이 완료되어 클립보드에 복사되었습니다.")
        except:
            self.plainTextEdit_NaverTag.setPlainText("올바른 링크와 태그를 입력하세요.")
    #

    # function
    def set_Queue(self, q, filename):
            q.put(filename) # 전달 받은 내용 큐에 저장

    def Download_Image(self, src, q, IsTrophy):
        if IsTrophy: # 트로피 이미지 태그면
            filename = src.split("/")[-1]
            r = requests.get(src)
            with open(self.dir_path+filename, 'wb') as f: # 파일 저장
                f.write(r.content)
                self.set_Queue(q, filename) # 저장한 파일이름 큐에 저장하기 위해 전달
        else: # 트로피 메인 이미지 태그면
            filename = src.split("/")[-1]
            r = requests.get(src)
            with open(self.dir_path + filename, 'wb') as f: # 파일 저장
                f.write(r.content)
                self.set_Queue(q, filename) # 저장한 파일이름 큐에 저장하기 위해 전달
    #

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate('Dialog', 'PSTC - 트로피 리스트 html 변환 자동화'))
        self.pushButton_SaveImage.setText(_translate('Dialog', '이미지 저장'))
        self.label_URL.setText(_translate('Dialog', '아래 입력란에 PSN Profiles 링크를 입력해주세요. (예: https://psnprofiles.com/trophies/5992-무쌍스타즈)'))
        self.label_4.setText(_translate('Dialog', '결과 (잠시 기다려주세요.)'))
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
        self.label_15.setText(_translate('Dialog', '1.0.6 | 앰아 (M-AHHH)'))

import resource_rc

if __name__ == '__main__':
    # multiprocessing.freeze_support() # 윈도우즈용 exe 배포시 주석 해제
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
