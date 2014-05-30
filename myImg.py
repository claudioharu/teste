from PySide import QtCore, QtGui
import ExtendedQLabel
import os

class Ui_Form(QtGui.QMainWindow):

	def __init__(self):
		self.path = os.getcwd() + '/c060/'
		print(self.path)
		self.manga = 'berserk'
		print(self.manga)
		self.page = 0
		self.scaleFactor = 1.0
		super(Ui_Form, self).__init__()
		self.setupUi(self)
		
		
	def setupUi(self, Form):
		
		Form.setObjectName("Form")
		Form.resize(1366, 768)
		
		self.imageLabel = ExtendedQLabel.ExtendedQLabel(Form)
		self.imageLabel.setBackgroundRole(QtGui.QPalette.Base)
		self.imageLabel.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
		self.imageLabel.setScaledContents(True)
		self.imageLabel.setText("")
		self.imageLabel.setObjectName("imageLabel")


		self.scrollArea = QtGui.QScrollArea()
		self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
		self.scrollArea.setGeometry(QtCore.QRect(560, 70, 201, 571))
		self.scrollArea.setWidget(self.imageLabel)
		self.scrollArea.setAlignment(QtCore.Qt.AlignRight)

		self.setCentralWidget(self.scrollArea)
		
		self.connect(self.imageLabel, QtCore.SIGNAL('clicked()'), self.nextPage)
		
		#self.pushButton = QtGui.QPushButton(Form)
		#self.pushButton.setGeometry(QtCore.QRect(0, 0, 31, 31))
		#self.pushButton.setObjectName("pushButton")            


		self.createActions()
		self.createMenus()
		
		self.updateActions()

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QtGui.QApplication.translate("Form", "Image Viewer", None, QtGui.QApplication.UnicodeUTF8))
		page = self.path + '000.jpg'
		print(page)
		self.imageLabel.setPixmap(QtGui.QPixmap(page))
		self.imageLabel.adjustSize()
		#self.pushButton.setText( ">")
		
	def fitToWindow(self):
		fitToWindow = self.fitToWindowAct.isChecked()
		self.scrollArea.setWidgetResizable(fitToWindow)
		if not fitToWindow:
			self.normalSize()
		self.updateActions()
	
	def nextPage(self):
		self.page += 1
		# treating pages
		print self.page
		#page = str(self.page)
		if(self.page < 10):
			page = '00' + str(self.page)
		elif(10 <= self.page < 100):
			page = '0' + str(self.page)
		elif(self.page >= 100):
			page = str(self.page)
				
		page = self.path + page + '.jpg'
		print (page)
		self.imageLabel.setPixmap(QtGui.QPixmap(page))
		self.imageLabel.adjustSize()
		
	def previusPage(self):
		
		if(str(self.page) != "0"):
			self.page -= 1
			# treating pages
			print self.page
			#page = str(self.page)
			if(self.page < 10):
				page = '00' + str(self.page)
			elif(10 <= self.page < 100):
				page = '0' + str(self.page)
			elif(self.page >= 100):
				page = str(self.page)
					
			page = self.path + page + '.jpg'
			print (page)
			self.imageLabel.setPixmap(QtGui.QPixmap(page))
			self.imageLabel.adjustSize()
			
		elif(self.page == 0): 
			page = self.path + '000.jpg'
			self.imageLabel.setPixmap(QtGui.QPixmap(page))
			self.imageLabel.adjustSize()
		
	def zoomIn(self):
		self.scaleImage(1.25)
 
	def zoomOut(self):
		self.scaleImage(0.8)
	
	def createActions(self):
		self.zoomInAct = QtGui.QAction("Zoom &In (25%)", self,
                shortcut="Ctrl++", enabled=False, triggered=self.zoomIn)
        
		self.NextPage = QtGui.QAction("Next", self,shortcut="right", enabled=False, triggered=self.nextPage)
		self.PreviusPage = QtGui.QAction("Previous", self,shortcut="left", enabled=False, triggered=self.previusPage)

		self.fitToWindowAct = QtGui.QAction("&Fit to Window", self, enabled=False, checkable=True, shortcut="Ctrl+F", triggered=self.fitToWindow)
                
	def updateActions(self):
		self.zoomInAct.setEnabled(not self.fitToWindowAct.isChecked())
		self.NextPage.setEnabled(not self.fitToWindowAct.isChecked())
		self.PreviusPage.setEnabled(not self.fitToWindowAct.isChecked())
		#self.zoomOutAct.setEnabled(not self.fitToWindowAct.isChecked())
		#self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())                

	def scaleImage(self, factor):
		self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
		
	def createMenus(self):
		self.viewMenu = QtGui.QMenu("&View", self)
		self.viewMenu.addAction(self.zoomInAct)
		self.viewMenu.addAction(self.NextPage)
		self.viewMenu.addAction(self.PreviusPage)
		
		self.menuBar().addMenu(self.viewMenu)
		
	def scaleImage(self, factor):
		self.scaleFactor *= factor
		self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

		self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
		#self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

		self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
		
	def adjustScrollBar(self, scrollBar, factor):
		scrollBar.setValue(int(factor * scrollBar.value()
			+ ((factor - 1) * scrollBar.pageStep()/2)))
			
		

if __name__ == '__main__':
 
	import sys

	app = QtGui.QApplication(sys.argv)
	ex = Ui_Form()
	ex.show()
	sys.exit(app.exec_())

