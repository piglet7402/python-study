import sys
from PyQt5.QtWidgets import QFileDialog, QRadioButton
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import cv2
import numpy as np
from PyQt5 import uic

form_class = uic.loadUiType("form3.ui")[0]

class MyApp(QWidget, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.show()  # 창 보여주기

    def initUI(self):
        self.start = 0
        self.qimg = 0

        # 프로그램 시작시 None 선택된 상태로 시작하기 위해서
        self.Radio()
        self.start = 1

        self.file.clicked.connect(self.openfile)    # '파일선택' 푸시 버튼이 눌리면 openfile 함수 호출

        # 라디오버튼이 눌렸을 경우
        self.none.clicked.connect(self.Radio)  # 'none' 라디오 버튼을 클릭 시
        self.blur.clicked.connect(self.Radio)   # 'blur' 라디오 버튼을 클릭 시
        self.sharpen.clicked.connect(self.Radio)  # 'sharpen' 라디오 버튼을 클릭 시

        # 체크박스 선택할 경우
        self.gray.stateChanged.connect(self.Check)
        self.invert.stateChanged.connect(self.Check)

        # # 저장 버튼 클릭할 경우
        # self.save.clicked.connect(self.fileSave)

        self.setWindowTitle('Image File')
        self.move(300, 300)

    def openfile(self):
        self.fname, _ = QFileDialog.getOpenFileName(self, 'Open file', './')

        pixmap = QPixmap(self.fname)   # Qt 에서 이미지 가져오기

        # 이미지 크기를 label 사이즈 맞춰주기
        # QLabel 1, 2 크기는 같음
        self.lbl_W = self.lbl1.width()    # 라벨의 가로길이
        self.lbl_H = self.lbl1.height()   # 라벨의 세로길이

        # 이미지를 라벨의 크기로 변경, 비율무시
        self.src_pixmap = pixmap.scaled(self.lbl_W, self.lbl_H, aspectRatioMode=Qt.IgnoreAspectRatio)

        self.lbl1.setPixmap(self.src_pixmap)    # Qt 에서 원본 이미지 보여주기
        self.lbl2.setPixmap(self.src_pixmap)  # Qt 에서 원본 이미지 보여주기

        # opencv 로 이미지 효과를 넣기 위해 이미지 읽어오기
        self.src = cv2.imread(self.fname)  # opencv 이미지 읽어오기
        self.src1 = cv2.cvtColor(self.src, cv2.COLOR_BGR2RGB)

        # 결과 이미지를 Qt 에서 보여주기
        # self.result_imgShow(self.src_pixmap)
        # self.result_imgShow(self.src)

    def result_imgShow(self, rec_img):
        self.fix_pixmap = rec_img
        Qimging = QImage(self.fix_pixmap.data, self.fix_pixmap.shape[1], self.fix_pixmap.shape[0], QImage.Format_RGB888)
        qimg = QPixmap.fromImage(Qimging)

        # 결과 이미지를 Qt 에서 보여주기
        self.lbl2.setPixmap(qimg)  # Qt 에서 결과 이미지 보여주기

    def Radio(self):
        RButton = self.sender()
        if self.blur == RButton:
            print("blur")

            self.result1 = cv2.blur(self.src1, (4, 4))   # blur 효과 주기

            # blurRGB = cv2.cvtColor(self.result1, cv2.COLOR_BGR2RGB)
            # blurQ= QImage(self.result1.data, self.result1.shape[1], self.result1.shape[0], QImage.Format_RGB888)
            # qimg = QPixmap.fromImage(blurQ)

            # 결과 이미지를 Qt 에서 보여주기
            self.result_imgShow(self.result1)

        if self.sharpen == RButton:
            print("sharpen")
            sharpening_2 = np.array([[-1, -1, -1, -1, -1],
                                     [-1, 2, 2, 2, -1],
                                     [-1, 2, 9, 2, -1],
                                     [-1, 2, 2, 2, -1],
                                     [-1, -1, -1, -1, -1]]) / 9.0
            self.result1 = cv2.filter2D(self.src1, -1, sharpening_2)

            # sharpenRGB = cv2.cvtColor(self.result1, cv2.COLOR_BGR2RGB)
            # sharpenQ = QImage(self.result1.data, self.result1.shape[1], self.result1.shape[0], QImage.Format_RGB888)
            # qimg = QPixmap.fromImage(sharpenQ)

            # 결과 이미지를 Qt 에서 보여주기
            self.result_imgShow(self.result1)

        if self.none == RButton:
            print("none")
            self.result1 = self.src1
            # self.result_imgShow(self.src_pixmap)

            # noneQ = QImage(self.result1.data, self.result1.shape[1], self.result1.shape[0], QImage.Format_RGB888)
            # qimg = QPixmap.fromImage(noneQ)

            # 결과 이미지를 Qt 에서 보여주기
            self.result_imgShow(self.result1)

        if self.start == 0:  # 프로그램이 처음 시작된 상태라면
            self.none.setChecked(True)  # none 버튼이 선택되어진 상태로 시작함

        self.Check()

    def Check(self):

        CBox = self.sender()
        # print( type( CBox ) )
        if type(CBox) == QRadioButton:  # radio button 들어왔을 경우
            CBox = self.invert
        if self.invert == CBox:
            print("invert")
            self.invertB = self.invert.isChecked()  # invert 박스에 선택됬는지 여부 확인
            if self.invertB == True:
                print("invert : {}".format(self.invertB))
                self.result2 = cv2.bitwise_not(self.result1)
                # invertQ = QImage(self.result2.data, self.result2.shape[1], self.result2.shape[0], QImage.Format_RGB888)
                # qimg = QPixmap.fromImage(invertQ)

                # 결과 이미지를 Qt 에서 보여주기
                self.result_imgShow(self.result2)

            if self.invertB == False:
                print("invert : {}".format(self.invertB))
                # 결과 이미지를 Qt 에서 보여주기
                self.result2 = self.result1
                # self.result_imgShow(self.src_pixmap)

                # invertQ = QImage(self.result2.data, self.result2.shape[1], self.result2.shape[0], QImage.Format_RGB888)
                # qimg = QPixmap.fromImage(invertQ)

                # 결과 이미지를 Qt 에서 보여주기
                self.result_imgShow(self.result2)

        if self.gray == CBox:
            print("gray")
            self.grayB = self.gray.isChecked()  # gray 박스에 선택됬는지 여부 확인
            if self.grayB == True:
                print("gray : {}".format(self.grayB))
                self.result = cv2.cvtColor(self.result2, cv2.COLOR_RGB2GRAY)   # 이미지 색깔 변경하기
                grqyQ = QImage(self.result.data, self.result.shape[1], self.result.shape[0], QImage.Format_RGB888)
                qimg = QPixmap.fromImage(grqyQ)

                # 결과 이미지를 Qt 에서 보여주기
                self.result_imgShow(qimg)

            if self.grayB == False:
                print("gray : {}".format(self.grayB))
                self.result_imgShow(self.src_pixmap)

        if CBox == None:
            print("Not Choice")

        print("test!!!!!!")

    def fileSave(self):
        print("save")
        # 저장 버튼 클릭할 경우

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
