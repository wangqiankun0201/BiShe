from PySide2.QtWidgets import QApplication,QComboBox,QGroupBox,QLabel,QLineEdit,QRadioButton,QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import  QIcon
import math
import os
import xlwt
from numpy import double

class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/main.ui')
        


        # 设置控件隐藏
        self.ui.label_8.setVisible(False)
        self.ui.label_10.setVisible(False)
        self.ui.label_12.setVisible(False)
        self.ui.label_17.setVisible(False)
        self.ui.label_24.setVisible(False)
        self.ui.label_28.setVisible(False)
        self.ui.label_38.setVisible(False)
        self.ui.label_43.setVisible(False)
        self.ui.label_44.setVisible(False)
        self.ui.lineEdit_5.setVisible(False)
        self.ui.lineEdit_6.setVisible(False)
        self.ui.lineEdit_7.setVisible(False)
        self.ui.lineEdit_15.setVisible(False)
        self.ui.lineEdit_20.setVisible(False)
        self.ui.lineEdit_25.setVisible(False)
        self.ui.lineEdit_31.setVisible(False)
        self.ui.lineEdit_32.setVisible(False)
        self.ui.radioButton_7.setVisible(False)
        self.ui.radioButton_8.setVisible(False)
        self.ui.label_42.setVisible(False)
        self.ui.lineEdit_39.setVisible(False)
        self.ui.label_55.setVisible(False)
        self.ui.label_56.setVisible(False)
        self.ui.label_57.setVisible(False)
        self.ui.lineEdit_49.setVisible(False)
        self.ui.lineEdit_50.setVisible(False)
        self.ui.lineEdit_51.setVisible(False)
        
        
        #设置信号
        self.ui.comboBox.currentIndexChanged.connect(self.maiDi)
        self.ui.comboBox_2.currentIndexChanged.connect(self.neiChen)
        self.ui.comboBox_3.currentIndexChanged.connect(self.queXian)
        self.ui.buttonGroup.buttonClicked.connect(self.cheLiang)
        self.ui.pushButton.clicked.connect(self.heZai)
        self.ui.pushButton_2.clicked.connect(self.houDu)
        self.ui.pushButton_3.clicked.connect(self.shengYu)
        self.ui.pushButton_4.clicked.connect(self.jiYongLiang)
        self.ui.pushButton_5.clicked.connect(self.daoChu)
        self.ui.buttonGroup_2.buttonClicked.connect(self.lieWen)
    #判断埋地方式
    def maiDi(self):
        maidi = self.ui.comboBox.currentText()
        if maidi == "沟埋式管道":
            self.ui.label_10.setVisible(False)
            self.ui.label_12.setVisible(False)
            self.ui.lineEdit_7.setVisible(False)
            self.ui.lineEdit_15.setVisible(False)
        else:
            self.ui.label_10.setVisible(True)
            self.ui.label_12.setVisible(True)
            self.ui.lineEdit_7.setVisible(True)
            self.ui.lineEdit_15.setVisible(True)
    #判断车辆情况
    def cheLiang(self):
        if self.ui.buttonGroup.checkedButton().text() == "两轮":
            self.ui.label_24.setVisible(True)
            self.ui.label_28.setVisible(True)
            self.ui.lineEdit_20.setVisible(True)
            self.ui.lineEdit_25.setVisible(True)
        else:
            self.ui.label_24.setVisible(False)
            self.ui.label_28.setVisible(False)
            self.ui.lineEdit_20.setVisible(False)
            self.ui.lineEdit_25.setVisible(False)
    #计算总荷载
    def heZai(self):
        #获取参数值
        goucaokuan = double(self.ui.lineEdit_19.text())
        rongzhong = double(self.ui.lineEdit_17.text())
        tushen = double(self.ui.lineEdit_16.text())
        tianjiao = double(self.ui.lineEdit_18.text())
        cejiao = double(self.ui.lineEdit_9.text())
        guanjing = double(self.ui.lineEdit_10.text())
        shuishen = double(self.ui.lineEdit_13.text())
        danya = double(self.ui.lineEdit_21.text())
        chechang = double(self.ui.lineEdit_23.text())
        chekuan = double(self.ui.lineEdit_22.text())
        dongli = double(self.ui.lineEdit_24.text())
        zhenkong = double(self.ui.lineEdit_3.text())
        #根据埋地方式选择土压力计算方法
        if self.ui.comboBox.currentText() == "沟埋式管道":
            tu_1 = (rongzhong*goucaokuan*goucaokuan/(2*(math.tan(cejiao/180))*((math.tan(45-tianjiao/2))**2)))* \
            (1-math.e**(-2*(math.tan(cejiao/180))*((math.tan(45-tianjiao/2))**2)*tushen/goucaokuan))
            tu_2 =(guanjing*(1+math.tan(45-cejiao/2)))*rongzhong*guanjing*(1-math.e**(-2*0.9*tushen/(guanjing*(1+math.tan(45-cejiao/2)))))/1.8
            tuyali = max(tu_1,tu_2)
        else:
            dengchen = double(self.ui.lineEdit_15.text())
            nianju = double(self.ui.lineEdit_7.text())
            if tushen <= dengchen:
                tu_1 = (rongzhong*guanjing*guanjing/(2*(math.tan(cejiao/180))*((math.tan(45-tianjiao/2))**2)))*(math.e**(2*(math.tan(cejiao/180))*((math.tan(45-tianjiao/2))**2)*tushen/guanjing)-1)
                tu_2 = rongzhong*tushen*guanjing + rongzhong*tushen*tushen*(math.tan(cejiao/180))*((math.tan(45-tianjiao/2))**2) + 2*nianju*(1-2*math.sqrt(math.tan(cejiao/180))*((math.tan(45-tianjiao/2))**2))*tushen
                tu_3 =(guanjing*(1+math.tan(45-cejiao/2)))*rongzhong*guanjing*(1-math.e**(-2*0.9*tushen/(guanjing*(1+math.tan(45-cejiao/2)))))/1.8
                tuyali = max(tu_1,tu_2,tu_3)
            else:
                tu_1 = (rongzhong*guanjing*guanjing/(2*(math.tan(cejiao/180))*((math.tan(45-tianjiao/2))**2)))(math.e**((2*(math.tan(cejiao/180))*((math.tan(45-tianjiao/2))**2))*tushen/guanjing)-1)+rongzhong*guanjing*(tushen-dengchen)*(math.e**(2*(math.tan(cejiao/180))*((math.tan(45-tianjiao/2))**2)*dengchen/guanjing))
                tu_2 = rongzhong*tushen*guanjing+rongzhong*(2*tushen-dengchen)*dengchen*(math.tan(cejiao/180))*((math.tan(45-tianjiao/2))**2)+ 2*nianju*(1-2*math.sqrt(math.tan(cejiao/180))*((math.tan(45-tianjiao/2))**2))*dengchen
                tu_3 =(guanjing*(1+math.tan(45-cejiao/2)))*rongzhong*guanjing*(1-math.e**(-2*0.9*tushen/(guanjing*(1+math.tan(45-cejiao/2)))))/1.8
                tuyali = max(tu_1,tu_2,tu_3)
        #计算静液压力
        jingye = 0.0981*shuishen
        
        # 计算活荷载
        if self.ui.buttonGroup.checkedButton().text() == "单轮":
            cheya = (danya * dongli)/((chechang+1.4*tushen)*(chekuan+1.4*tushen))/1000
        else:
            zongliang = double(self.ui.lineEdit_25.text())
            jingju = double(self.ui.lineEdit_20.text())
            cheya = (danya*dongli*zongliang)/((chechang+1.4*tushen)*(zongliang*chekuan+(zongliang-1)*jingju+1.4*tushen))/1000
        
        zongyali = tuyali + jingye +cheya + zhenkong + 10
        self.ui.lineEdit_34.setText(str(zongyali))

    #修复设计方式选择
    def neiChen(self):
        if self.ui.comboBox_2.currentText() == "结构性修复设计":
            self.ui.label_6.setVisible(False)
            self.ui.label_8.setVisible(True)
            self.ui.label_17.setVisible(True)
            self.ui.lineEdit_4.setVisible(False)
            self.ui.lineEdit_5.setVisible(True)
            self.ui.lineEdit_6.setVisible(True)
        else:
            self.ui.label_6.setVisible(True)
            self.ui.label_8.setVisible(False)
            self.ui.label_17.setVisible(False)
            self.ui.lineEdit_4.setVisible(True)
            self.ui.lineEdit_5.setVisible(False)
            self.ui.lineEdit_6.setVisible(False)
    #内衬壁厚设计
    def houDu(self):
        neijing = double(self.ui.lineEdit.text())
        changqi = double(self.ui.lineEdit_8.text())
        if self.ui.comboBox_2.currentText() == "半结构性修复设计":
            bosong = double(self.ui.lineEdit_4.text())
            zhenkong = double(self.ui.lineEdit_3.text())
            shuishen = double(self.ui.lineEdit_13.text())
            zuixiao = neijing/((14*changqi/(zhenkong+shuishen*0.0981)*2*(1-bosong**2))**(1/3)+1)
            self.ui.lineEdit_37.setText(str(zuixiao))
        else:
            duanqi = double(self.ui.lineEdit_6.text())
            zonghe = double(self.ui.lineEdit_5.text())
            zuixiao = 0.721*neijing*(((2*double(self.ui.lineEdit_34.text()))**2)/(changqi*(1-0.33*double(self.ui.lineEdit_13.text())/double(self.ui.lineEdit_16.text()))*zonghe*(1/(1+4*math.e**(-0.213*double(self.ui.lineEdit_16.text()))))))**(1/3)
            if zuixiao >= (0.1970*neijing/(duanqi)**(1/3)):
                self.ui.lineEdit_37.setText(str(zuixiao))
            else:
                self.ui.lineEdit_37.setText("最小壁厚不符合要求！")
        
    #计算涂料用量
    def jiYongLiang(self):
        neijing = double(self.ui.lineEdit.text())
        changdu = double(self.ui.lineEdit_2.text()) 
        bihou = double(self.ui.lineEdit_35.text())
        yongliang = changdu * (math.pi*neijing*neijing-math.pi*(neijing-bihou)**2)/1000000
        self.ui.lineEdit_38.setText(str(yongliang))
    #缺陷判断
    def queXian(self):
        if self.ui.comboBox_3.currentText() == "腐蚀缺陷":
            self.ui.label_38.setVisible(False)
            self.ui.label_43.setVisible(False)
            self.ui.label_44.setVisible(False)
            self.ui.radioButton_7.setVisible(False)
            self.ui.radioButton_8.setVisible(False)
            self.ui.lineEdit_31.setVisible(False)
            self.ui.lineEdit_32.setVisible(False)
            self.ui.label_37.setVisible(True)
            self.ui.label_32.setVisible(True)
            self.ui.label_33.setVisible(True)
            self.ui.label.setVisible(True)
            self.ui.label_45.setVisible(True)
            self.ui.label_31.setVisible(True)
            self.ui.lineEdit_28.setVisible(True)
            self.ui.lineEdit_29.setVisible(True)
            self.ui.lineEdit_33.setVisible(True)
            self.ui.lineEdit_27.setVisible(True)
            self.ui.lineEdit_36.setVisible(True)
            self.ui.lineEdit_11.setVisible(True)
            self.ui.lineEdit_39.setVisible(False)
            self.ui.lineEdit_26.setVisible(True)
            self.ui.lineEdit_30.setVisible(True)
            self.ui.label_42.setVisible(False)
            self.ui.label_34.setVisible(True)
            self.ui.label_46.setVisible(True)
            self.ui.label_55.setVisible(False)
            self.ui.label_56.setVisible(False)
            self.ui.label_57.setVisible(False)
            self.ui.lineEdit_49.setVisible(False)
            self.ui.lineEdit_50.setVisible(False)
            self.ui.lineEdit_51.setVisible(False)
            self.ui.label_49.setVisible(True)
            self.ui.label_50.setVisible(True)
            self.ui.label_51.setVisible(True)
            self.ui.label_52.setVisible(True)
            self.ui.label_53.setVisible(True)
            self.ui.label_54.setVisible(True)
            self.ui.lineEdit_43.setVisible(True)
            self.ui.lineEdit_44.setVisible(True)
            self.ui.lineEdit_45.setVisible(True)
            self.ui.lineEdit_46.setVisible(True)
            self.ui.lineEdit_47.setVisible(True)
            self.ui.lineEdit_48.setVisible(True)
        else:
            self.ui.label_38.setVisible(True)
            self.ui.radioButton_7.setVisible(True)
            self.ui.radioButton_8.setVisible(True)
            self.ui.label_37.setVisible(False)
            self.ui.label_32.setVisible(False)
            self.ui.label_33.setVisible(False)
            self.ui.label.setVisible(False)
            self.ui.label_45.setVisible(False)
            self.ui.label_31.setVisible(False)
            self.ui.lineEdit_28.setVisible(False)
            self.ui.lineEdit_29.setVisible(False)
            self.ui.lineEdit_33.setVisible(False)
            self.ui.lineEdit_27.setVisible(False)
            self.ui.lineEdit_36.setVisible(False)
            self.ui.lineEdit_11.setVisible(False)
            self.ui.lineEdit_39.setVisible(True)
            self.ui.lineEdit_26.setVisible(False)
            self.ui.lineEdit_30.setVisible(False)
            self.ui.label_42.setVisible(True)
            self.ui.label_34.setVisible(False)
            self.ui.label_46.setVisible(False)
            self.ui.label_55.setVisible(True)
            self.ui.label_56.setVisible(True)
            self.ui.label_57.setVisible(True)
            self.ui.lineEdit_49.setVisible(True)
            self.ui.lineEdit_50.setVisible(True)
            self.ui.lineEdit_51.setVisible(True)
            self.ui.lineEdit_43.setVisible(False)
            self.ui.lineEdit_44.setVisible(False)
            self.ui.lineEdit_45.setVisible(False)
            self.ui.lineEdit_46.setVisible(False)
            self.ui.lineEdit_47.setVisible(False)
            self.ui.lineEdit_48.setVisible(False)
            self.ui.label_49.setVisible(False)
            self.ui.label_50.setVisible(False)
            self.ui.label_51.setVisible(False)
            self.ui.label_52.setVisible(False)
            self.ui.label_53.setVisible(False)
            self.ui.label_54.setVisible(False)

            if self.ui.buttonGroup_2.checkedButton().text() == "轴向裂纹":
                self.ui.label_44.setVisible(False)
                self.ui.lineEdit_32.setVisible(False)
                self.ui.label_43.setVisible(True)
                self.ui.lineEdit_31.setVisible(True)
            else:
                self.ui.label_44.setVisible(True)
                self.ui.lineEdit_32.setVisible(True)
                self.ui.label_43.setVisible(False)
                self.ui.lineEdit_31.setVisible(False)
    #旧管道剩余承载力计算
    def shengYu(self):
        #腐蚀缺陷管道
        if self.ui.comboBox_3.currentText() == "腐蚀缺陷":
            guanhou = double(self.ui.lineEdit_12.text())
            qufu = double(self.ui.lineEdit_14.text())
            quechang = double(self.ui.lineEdit_29.text())
            zhouhe = double(self.ui.lineEdit_33.text())
            huankang = double(self.ui.lineEdit_28.text())
            huanying = double(self.ui.lineEdit_27.text())
            neimo = double(self.ui.lineEdit_36.text())
            junyun = double(self.ui.lineEdit_11.text())
            #旧管道轴向应力计算
            jiuzhouxiang = (1*double(self.ui.lineEdit.text())/(4*junyun))*(huankang*2*guanhou/(double(self.ui.lineEdit_10.text())-guanhou))+(double(self.ui.lineEdit_4.text())*zhouhe/(math.pi*double(self.ui.lineEdit.text())*junyun))*1000
            #旧管道环向应力计算
            if quechang*quechang <= 50*double(self.ui.lineEdit.text())*guanhou:
                m = (1+(0.6275*quechang*quechang/(double(self.ui.lineEdit.text())*guanhou))+(0.003375*quechang**4/(double(self.ui.lineEdit.text())*guanhou)/(double(self.ui.lineEdit.text())*guanhou)))**0.5
            else:
                m = 0.032*quechang*quechang/(double(self.ui.lineEdit.text())*guanhou)+3.3   
            jiuhuanxiang = (qufu+68.95)*((1-0.85*junyun/guanhou)/(1-0.85*junyun/guanhou*m**(-1)))/2

            self.ui.lineEdit_26.setText(str(jiuzhouxiang))
            self.ui.lineEdit_30.setText(str(jiuhuanxiang))
            self.ui.lineEdit_43.setText(str(jiuzhouxiang))
            self.ui.lineEdit_44.setText(str(jiuhuanxiang))

            #内衬轴向应力计算
            neizhouxiang = 1000*double(self.ui.lineEdit_34.text())*double(self.ui.lineEdit_2.text())*8000*double(self.ui.lineEdit.text())/(math.pi*(double(self.ui.lineEdit.text())**4-(double(self.ui.lineEdit.text())-2*double(self.ui.lineEdit_35.text()))**4))
            #内衬环向应力计算
            neihuanxiang = neimo*huanying/1.5

            self.ui.lineEdit_46.setText(str(neizhouxiang))
            self.ui.lineEdit_45.setText(str(neihuanxiang))


            #复合管道轴向应力计算
            zhouxiang = jiuzhouxiang + neizhouxiang
            #复合管道环向应力计算
            huanxiang = jiuhuanxiang + neihuanxiang

            self.ui.lineEdit_48.setText(str(zhouxiang))
            self.ui.lineEdit_47.setText(str(huanxiang))

        #裂纹缺陷管道
        else:
            #轴向裂纹计算
            if self.ui.buttonGroup_2.checkedButton().text() == "轴向裂纹":
                banchang = double(self.ui.lineEdit_31.text())
                yinzi = banchang/(math.sqrt(1000*double(self.ui.lineEdit_10.text())*double(self.ui.lineEdit_12.text())))
                #Folias模型
                frou_1 = 1/(math.sqrt(1+1.05*yinzi*yinzi))
                #Erdogan模型
                frou_2 = 1/(0.614+0.87542*yinzi+0.386*math.e**(-2.275*yinzi))
                #Kim模型
                frou_3 = (2/math.sqrt(3))*(1/(math.sqrt(1+0.34*yinzi+1.24*yinzi*yinzi)))

                frou = min(frou_1,frou_2,frou_3)
                jiujixian = frou*double(self.ui.lineEdit_14.text())*double(self.ui.lineEdit_12.text())/(double(self.ui.lineEdit_10.text())*1000)
            #环向裂纹计算
            else:
                jiaodu = double(self.ui.lineEdit_32.text())
                #kanninen模型
                jiujixian = 2*double(self.ui.lineEdit_14.text())*(math.pi - jiaodu/180 +2*(math.sin(math.sin(jiaodu/180)/2)))/(double(self.ui.lineEdit_10.text())*1000)
            
            self.ui.lineEdit_49.setText(str(jiujixian))
            self.ui.lineEdit_38.setText(str(jiujixian))

            #内衬管极限承载力计算
            neijixian = double(self.ui.lineEdit_14.text())*double(self.ui.lineEdit_35.text())/(double(self.ui.lineEdit_4.text())*(double(self.ui.lineEdit.text())-2*double(self.ui.lineEdit_35.text())))

            self.ui.lineEdit_50.setText(str(neijixian))
            
            #复合管道承载力计算
            jixian = neijixian + jiujixian
            self.ui.lineEdit_51.setText(str(jixian))
        self.ui.lineEdit_40.setText(self.ui.lineEdit_34.text())
        self.ui.lineEdit_41.setText(self.ui.lineEdit_35.text())
        self.ui.lineEdit_42.setText(self.ui.lineEdit_38.text())

    #裂纹控件隐藏
    def lieWen(self):
        if self.ui.buttonGroup_2.checkedButton().text() == "轴向裂纹":
            self.ui.label_44.setVisible(False)
            self.ui.lineEdit_32.setVisible(False)
            self.ui.label_43.setVisible(True)
            self.ui.lineEdit_31.setVisible(True)
        else:
            self.ui.label_44.setVisible(True)
            self.ui.lineEdit_32.setVisible(True)
            self.ui.label_43.setVisible(False)
            self.ui.lineEdit_31.setVisible(False)
    def daoChu(self):
        #文件导出
        ws = xlwt.Workbook(encoding='utf8')
        worksheet = ws.add_sheet('排水管道喷涂修复承载性研究')
        worksheet.write(0,0,"竖向总荷载(MPa)")
        worksheet.write(0,1,"内衬壁厚取值(mm)")
        worksheet.write(0,2,"涂料用量(m³)")
        worksheet.write(1,0,self.ui.lineEdit_40.text())
        worksheet.write(1,1,self.ui.lineEdit_41.text())
        worksheet.write(1,2,self.ui.lineEdit_42.text())
        if self.ui.comboBox_3.currentText() == "腐蚀缺陷":
            worksheet.write(0,3,"旧管道轴向应力(MPa)")
            worksheet.write(0,4,"旧管道环向应力(MPa)")
            worksheet.write(0,5,"内衬管轴向应力(MPa)")
            worksheet.write(0,6,"内衬管环向应力(MPa)")
            worksheet.write(0,7,"复合管轴向应力(MPa)")
            worksheet.write(0,8,"复合管环向应力(MPa)")
            worksheet.write(1,3,self.ui.lineEdit_43.text())
            worksheet.write(1,4,self.ui.lineEdit_44.text())
            worksheet.write(1,5,self.ui.lineEdit_46.text())
            worksheet.write(1,6,self.ui.lineEdit_45.text())
            worksheet.write(1,7,self.ui.lineEdit_48.text())
            worksheet.write(1,8,self.ui.lineEdit_47.text())
        else:
            worksheet.write(0,3,"旧管道极限承载力(MPa)")
            worksheet.write(0,4,"内衬管极限承载力(MPa)")
            worksheet.write(0,5,"复合管极限承载力(MPa)")
            worksheet.write(1,3,self.ui.lineEdit_49.text())
            worksheet.write(1,4,self.ui.lineEdit_50.text())
            worksheet.write(1,5,self.ui.lineEdit_51.text())
        #检测文件是否存在
        e_file = os.path.exists('承载力.xls')
        if e_file:
            os.remove(r'承载力.xls')
        #保存文件
        ws.save('承载力.xls')



app = QApplication([])
app.setWindowIcon(QIcon('ui/logo.png'))
stats = Stats()
stats.ui.show()
app.exec_()