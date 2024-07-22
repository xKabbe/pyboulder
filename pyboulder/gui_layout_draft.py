import sys

import numpy as np
import qdarkstyle
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QWidget, QTabWidget, QGridLayout, QTableWidget, QHeaderView, QTableWidgetItem, QLabel, QComboBox, QSpinBox, QSlider,
    QTextEdit, QPushButton, QProgressBar, QHBoxLayout, QFileDialog, QFrame, QGroupBox, QSplitter, QStackedWidget,
    QFontComboBox, QRadioButton, QLCDNumber, QDateEdit, QDateTimeEdit, QTimeEdit, QDial, QDoubleSpinBox, QTreeView
)
from pyqtgraph import PlotWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTabWidget Example")
        self.resize(1920, 1080)
        self.showMaximized()

        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.addTab(self.generalTabUI(), "General")
        tabs.addTab(self.processTabUI(), "Process")
        tabs.addTab(self.networkTabUI(), "Network")
        tabs.addTab(self.videoAnalysisTabUI(), "Video Analysis")
        tabs.addTab(self.poseDetectionTabUI(), "Pose Detection")
        tabs.addTab(self.movementMetricsTabUI(), "Movement Metrics")
        tabs.addTab(self.angleMetricsTabUI(), "Angle Metrics")
        tabs.addTab(self.dataLoggingTabUI(), "Data Logging")
        tabs.addTab(self.settingsTabUI(), "Settings")
        tabs.addTab(self.dateTimeTabUI(), "Date & Time")
        tabs.addTab(self.advancedControlsTabUI(), "Advanced Controls")
        tabs.addTab(self.fontSettingsTabUI(), "Font Settings")
        tabs.addTab(self.calculationTabUI(), "Calculations")
        tabs.addTab(self.layoutExperimentTabUI(), "Layout Experiment")
        tabs.addTab(self.expandableListTabUI(), "Expandable List")
        tabs.addTab(self.treeViewTabUI(), "Tree View & Metadata")
        tabs.addTab(self.poseDetectionResultsTabUI(), "Pose Detection Results")
        layout.addWidget(tabs)

    def generalTabUI(self):
        generalTab = QWidget()
        outerLayout = QVBoxLayout()

        # Create the original layout
        topLayout = QFormLayout()
        topLayout.addRow("Some Text:", QLineEdit())

        optionsLayout = QVBoxLayout()
        optionsLayout.addWidget(QCheckBox("Option one"))
        optionsLayout.addWidget(QCheckBox("Option two"))
        optionsLayout.addWidget(QCheckBox("Option three"))

        # Left
        leftLayout = QVBoxLayout()
        leftLayout.addLayout(topLayout)
        leftLayout.addLayout(optionsLayout)
        leftLayout.addStretch()

        # Table 1
        tableWidget = QTableWidget()
        tableWidget.setColumnCount(5)
        tableWidget.setHorizontalHeaderLabels(['ID', 'X', 'Y', 'Z', 'Visibility'])
        tableWidget.horizontalHeader().setStretchLastSection(True)
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        tableWidget.setRowCount(2)
        tableWidget.setItem(0, 0, QTableWidgetItem(32))
        tableWidget.setItem(0, 1, QTableWidgetItem(1))
        tableWidget.setItem(0, 2, QTableWidgetItem(1))
        tableWidget.setItem(0, 3, QTableWidgetItem(1))
        tableWidget.setItem(0, 4, QTableWidgetItem(5))
        tableWidget.setItem(1, 0, QTableWidgetItem(33))
        tableWidget.setItem(1, 1, QTableWidgetItem(8))
        tableWidget.setItem(1, 2, QTableWidgetItem(7))
        tableWidget.setItem(1, 3, QTableWidgetItem(6))
        tableWidget.setItem(1, 4, QTableWidgetItem(5))

        another_tableLayout = QVBoxLayout()
        another_tableLayout.addWidget(tableWidget)

        # Table 2
        tableWidget1 = QTableWidget()
        tableWidget1.setColumnCount(5)
        tableWidget1.setHorizontalHeaderLabels(['ID', 'X', 'Y', 'Z', 'Visibility'])
        tableWidget1.horizontalHeader().setStretchLastSection(True)
        tableWidget1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        tableWidget1.setRowCount(2)
        tableWidget1.setItem(0, 0, QTableWidgetItem(32))
        tableWidget1.setItem(0, 1, QTableWidgetItem(1))
        tableWidget1.setItem(0, 2, QTableWidgetItem(1))
        tableWidget1.setItem(0, 3, QTableWidgetItem(1))
        tableWidget1.setItem(0, 4, QTableWidgetItem(5))
        tableWidget1.setItem(1, 0, QTableWidgetItem(33))
        tableWidget1.setItem(1, 1, QTableWidgetItem(8))
        tableWidget1.setItem(1, 2, QTableWidgetItem(7))
        tableWidget1.setItem(1, 3, QTableWidgetItem(6))
        tableWidget1.setItem(1, 4, QTableWidgetItem(5))

        another_tableLayout1 = QVBoxLayout()
        another_tableLayout1.addWidget(tableWidget1)

        # Middle
        centerLayout = QVBoxLayout()
        centerLayout.addLayout(another_tableLayout)
        centerLayout.addLayout(another_tableLayout1)

        # Right
        rightLayout = QVBoxLayout()

        # Create plot widget 1
        plotWidget1 = PlotWidget()
        x = np.arange(10)
        y = np.random.normal(size=10)
        plotWidget1.plot(x, y, pen='r')
        rightLayout.addWidget(plotWidget1)

        # Create plot widget 2
        plotWidget2 = PlotWidget()
        x = np.arange(10)
        y = np.random.normal(size=10)
        plotWidget2.plot(x, y, pen='b')
        rightLayout.addWidget(plotWidget2)

        # Create a grid layout and add the original and duplicate layouts
        gridLayout = QGridLayout()
        gridLayout.addLayout(leftLayout, 0, 0)
        gridLayout.addLayout(centerLayout, 0, 1)
        gridLayout.addLayout(rightLayout, 0, 2)

        outerLayout.addLayout(gridLayout)
        generalTab.setLayout(outerLayout)
        return generalTab

    def processTabUI(self):
        processTab = QWidget()
        outerLayout = QVBoxLayout()

        # Add a label and a combo box
        label = QLabel("Select Network:")
        comboBox = QComboBox()
        comboBox.addItems(["Network 1", "Network 2", "Network 3"])

        # Add a spin box and a slider
        spinBox = QSpinBox()
        spinBox.setRange(0, 100)
        slider = QSlider()
        slider.setOrientation(Qt.Horizontal)
        slider.setRange(0, 100)

        # Add a text edit
        textEdit = QTextEdit()

        # Create layouts and add widgets
        formLayout = QFormLayout()
        formLayout.addRow(label, comboBox)
        formLayout.addRow("Set Value:", spinBox)
        formLayout.addRow("Adjust:", slider)

        verticalLayout = QVBoxLayout()
        verticalLayout.addLayout(formLayout)
        verticalLayout.addWidget(textEdit)

        outerLayout.addLayout(verticalLayout)
        processTab.setLayout(outerLayout)
        return processTab

    def networkTabUI(self):
        networkTab = QWidget()
        outerLayout = QVBoxLayout()

        # Example components for network settings
        networkGroupBox = QGroupBox("Network Settings")
        networkLayout = QFormLayout()
        networkLayout.addRow("IP Address:", QLineEdit())
        networkLayout.addRow("Port:", QLineEdit())
        networkGroupBox.setLayout(networkLayout)

        proxyGroupBox = QGroupBox("Proxy Settings")
        proxyLayout = QFormLayout()
        proxyLayout.addRow("Proxy IP:", QLineEdit())
        proxyLayout.addRow("Proxy Port:", QLineEdit())
        proxyGroupBox.setLayout(proxyLayout)

        outerLayout.addWidget(networkGroupBox)
        outerLayout.addWidget(proxyGroupBox)
        networkTab.setLayout(outerLayout)
        return networkTab

    def videoAnalysisTabUI(self):
        videoAnalysisTab = QWidget()
        outerLayout = QVBoxLayout()

        loadVideoButton = QPushButton("Load Video")
        loadVideoButton.clicked.connect(self.openFile)

        videoFrame = QLabel()
        videoFrame.setFrameStyle(QFrame.Box)
        videoFrame.setAlignment(Qt.AlignCenter)

        playButton = QPushButton("Play")
        stopButton = QPushButton("Stop")

        slider = QSlider(Qt.Horizontal)
        progressBar = QProgressBar()

        controlLayout = QHBoxLayout()
        controlLayout.addWidget(playButton)
        controlLayout.addWidget(stopButton)
        controlLayout.addWidget(slider)

        outerLayout.addWidget(loadVideoButton)
        outerLayout.addWidget(videoFrame)
        outerLayout.addLayout(controlLayout)
        outerLayout.addWidget(progressBar)

        videoAnalysisTab.setLayout(outerLayout)
        return videoAnalysisTab

    def poseDetectionTabUI(self):
        poseDetectionTab = QWidget()
        outerLayout = QVBoxLayout()

        poseImage = QLabel()
        poseImage.setFrameStyle(QFrame.Box)
        poseImage.setAlignment(Qt.AlignCenter)
        poseImage.setText("Pose Image Placeholder")

        metricsTable = QTableWidget()
        metricsTable.setColumnCount(4)
        metricsTable.setHorizontalHeaderLabels(['Metric', 'Value', 'Min', 'Max'])
        metricsTable.setRowCount(5)
        for i in range(5):
            metricsTable.setItem(i, 0, QTableWidgetItem(f"Metric {i + 1}"))
            metricsTable.setItem(i, 1, QTableWidgetItem("0"))
            metricsTable.setItem(i, 2, QTableWidgetItem("5"))
            metricsTable.setItem(i, 3, QTableWidgetItem("100"))

        outerLayout.addWidget(poseImage)
        outerLayout.addWidget(metricsTable)
        poseDetectionTab.setLayout(outerLayout)
        return poseDetectionTab

    def movementMetricsTabUI(self):
        movementMetricsTab = QWidget()
        outerLayout = QVBoxLayout()

        metricsLayout = QFormLayout()
        metricsLayout.addRow("Reach:", QLineEdit())
        metricsLayout.addRow("Body Angle:", QLineEdit())
        metricsLayout.addRow("Hip Movement:", QLineEdit())
        metricsLayout.addRow("Foot Placement:", QLineEdit())

        # chartLabel = QLabel("Metrics Chart Placeholder")
        # chartLabel.setFrameStyle(QFrame.Box)
        # chartLabel.setAlignment(Qt.AlignCenter)

        metricsChartLayout = QVBoxLayout()

        gridLayout = QGridLayout()

        # Create plot widget 1
        plotWidget1 = PlotWidget()
        x = np.arange(10)
        y = np.random.normal(size=10)
        plotWidget1.plot(x, y, pen='r')
        metricsChartLayout.addWidget(plotWidget1)

        # Create plot widget 2
        plotWidget2 = PlotWidget()
        x = np.arange(10)
        y = np.random.normal(size=10)
        plotWidget2.plot(x, y, pen='b')
        metricsChartLayout.addWidget(plotWidget2)

        # Create plot widget 3
        plotWidget3 = PlotWidget()
        x = np.arange(10)
        y = np.random.normal(size=10)
        plotWidget3.plot(x, y, pen='r')
        metricsChartLayout.addWidget(plotWidget3)

        # Create plot widget 4
        plotWidget4 = PlotWidget()
        x = np.arange(10)
        y = np.random.normal(size=10)
        plotWidget4.plot(x, y, pen='b')
        metricsChartLayout.addWidget(plotWidget4)

        outerLayout.addLayout(metricsLayout)
        outerLayout.addLayout(metricsChartLayout)
        # outerLayout.addWidget(chartLabel)
        movementMetricsTab.setLayout(outerLayout)
        return movementMetricsTab

    def angleMetricsTabUI(self):
        movementMetricsTab = QWidget()
        outerLayout = QVBoxLayout()

        metricsLayout = QFormLayout()
        metricsLayout.addRow("Reach:", QLineEdit())
        metricsLayout.addRow("Body Angle:", QLineEdit())
        metricsLayout.addRow("Hip Movement:", QLineEdit())
        metricsLayout.addRow("Foot Placement:", QLineEdit())

        metricsChartLayout = QVBoxLayout()

        gridLayout = QGridLayout()

        # Create plot widget 1
        plotWidget1 = PlotWidget()
        x = np.arange(10)
        y = np.random.normal(size=10)
        plotWidget1.plot(x, y, pen='r')
        gridLayout.addWidget(plotWidget1, 0, 0)

        # Create plot widget 2
        plotWidget2 = PlotWidget()
        x = np.arange(10)
        y = np.random.normal(size=10)
        plotWidget2.plot(x, y, pen='b')
        gridLayout.addWidget(plotWidget2, 0, 1)

        # Create plot widget 3
        plotWidget3 = PlotWidget()
        x = np.arange(10)
        y = np.random.normal(size=10)
        plotWidget3.plot(x, y, pen='r')
        gridLayout.addWidget(plotWidget3, 1, 0)

        # Create plot widget 4
        plotWidget4 = PlotWidget()
        x = np.arange(10)
        y = np.random.normal(size=10)
        plotWidget4.plot(x, y, pen='b')
        gridLayout.addWidget(plotWidget4, 1, 1)

        metricsChartLayout.addLayout(gridLayout)

        outerLayout.addLayout(metricsLayout)
        outerLayout.addLayout(metricsChartLayout)
        # outerLayout.addWidget(chartLabel)
        movementMetricsTab.setLayout(outerLayout)
        return movementMetricsTab

    def dataLoggingTabUI(self):
        dataLoggingTab = QWidget()
        outerLayout = QVBoxLayout()

        loggingOptionsLayout = QFormLayout()
        loggingOptionsLayout.addRow("Log Interval (s):", QSpinBox())
        loggingOptionsLayout.addRow("File Path:", QLineEdit())

        startLoggingButton = QPushButton("Start Logging")
        stopLoggingButton = QPushButton("Stop Logging")

        logOutput = QTextEdit()
        logOutput.setReadOnly(True)
        logOutput.setPlaceholderText("Log output will be displayed here...")

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(startLoggingButton)
        buttonLayout.addWidget(stopLoggingButton)

        outerLayout.addLayout(loggingOptionsLayout)
        outerLayout.addLayout(buttonLayout)
        outerLayout.addWidget(logOutput)
        dataLoggingTab.setLayout(outerLayout)
        return dataLoggingTab

    def settingsTabUI(self):
        settingsTab = QWidget()
        outerLayout = QVBoxLayout()

        generalSettingsGroupBox = QGroupBox("General Settings")
        generalSettingsLayout = QFormLayout()
        generalSettingsLayout.addRow("Theme:", QComboBox())
        generalSettingsLayout.addRow("Language:", QComboBox())
        generalSettingsGroupBox.setLayout(generalSettingsLayout)

        advancedSettingsGroupBox = QGroupBox("Advanced Settings")
        advancedSettingsLayout = QFormLayout()
        advancedSettingsLayout.addRow("Option 1:", QCheckBox())
        advancedSettingsLayout.addRow("Option 2:", QCheckBox())
        advancedSettingsGroupBox.setLayout(advancedSettingsLayout)

        outerLayout.addWidget(generalSettingsGroupBox)
        outerLayout.addWidget(advancedSettingsGroupBox)
        settingsTab.setLayout(outerLayout)
        return settingsTab

    def dateTimeTabUI(self):
        dateTimeTab = QWidget()
        outerLayout = QVBoxLayout()

        # Date and Time Widgets
        dateEdit = QDateEdit()
        dateTimeEdit = QDateTimeEdit()
        timeEdit = QTimeEdit()
        dial = QDial()
        doubleSpinBox = QDoubleSpinBox()

        # Layout for Date & Time
        dateTimeLayout = QFormLayout()
        dateTimeLayout.addRow("Date:", dateEdit)
        dateTimeLayout.addRow("Date & Time:", dateTimeEdit)
        dateTimeLayout.addRow("Time:", timeEdit)
        dateTimeLayout.addRow("Dial:", dial)
        dateTimeLayout.addRow("Double Spin Box:", doubleSpinBox)

        # Main Layout
        outerLayout.addLayout(dateTimeLayout)
        dateTimeTab.setLayout(outerLayout)
        return dateTimeTab

    def advancedControlsTabUI(self):
        advancedControlsTab = QWidget()
        outerLayout = QVBoxLayout()

        # LCD Number
        lcdNumber = QLCDNumber()
        lcdNumber.display(12345)

        # Slider and SpinBox
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 100)
        spinBox = QSpinBox()
        spinBox.setRange(0, 100)

        # Radio Buttons
        radioButton1 = QRadioButton("Option 1")
        radioButton2 = QRadioButton("Option 2")

        # Layout for Controls
        controlsLayout = QFormLayout()
        controlsLayout.addRow("LCD Number:", lcdNumber)
        controlsLayout.addRow("Slider:", slider)
        controlsLayout.addRow("Spin Box:", spinBox)
        controlsLayout.addRow("Radio Buttons:", radioButton1)
        controlsLayout.addRow("", radioButton2)

        # Main Layout
        outerLayout.addLayout(controlsLayout)
        advancedControlsTab.setLayout(outerLayout)
        return advancedControlsTab

    def fontSettingsTabUI(self):
        fontSettingsTab = QWidget()
        outerLayout = QVBoxLayout()

        # Font ComboBox
        fontComboBox = QFontComboBox()

        # Font Size SpinBox
        fontSizeSpinBox = QSpinBox()
        fontSizeSpinBox.setRange(6, 72)
        fontSizeSpinBox.setValue(12)

        # Font Color Selection
        fontColorLabel = QLabel("Font Color:")
        fontColorComboBox = QComboBox()
        fontColorComboBox.addItems(["Black", "Red", "Green", "Blue"])

        # Layout for Font Settings
        fontLayout = QFormLayout()
        fontLayout.addRow("Font:", fontComboBox)
        fontLayout.addRow("Font Size:", fontSizeSpinBox)
        fontLayout.addRow(fontColorLabel, fontColorComboBox)

        # Main Layout
        outerLayout.addLayout(fontLayout)
        fontSettingsTab.setLayout(outerLayout)
        return fontSettingsTab

    def calculationTabUI(self):
        calculationTab = QWidget()
        outerLayout = QVBoxLayout()

        # Simple Calculation Widgets
        input1 = QLineEdit()
        input2 = QLineEdit()
        resultLabel = QLabel("Result: ")
        calculateButton = QPushButton("Calculate")

        # Layout for Calculation
        calcLayout = QFormLayout()
        calcLayout.addRow("Input 1:", input1)
        calcLayout.addRow("Input 2:", input2)
        calcLayout.addRow(resultLabel)
        calcLayout.addRow("", calculateButton)

        # Main Layout
        outerLayout.addLayout(calcLayout)
        calculationTab.setLayout(outerLayout)
        return calculationTab

    def layoutExperimentTabUI(self):
        layoutExperimentTab = QWidget()
        outerLayout = QVBoxLayout()

        # Complex Layout
        stackedWidget = QStackedWidget()
        page1 = QWidget()
        page2 = QWidget()
        stackedWidget.addWidget(page1)
        stackedWidget.addWidget(page2)
        stackedWidget.setCurrentIndex(0)

        # Page 1 Content
        page1Layout = QVBoxLayout()
        page1Layout.addWidget(QLabel("This is Page 1"))
        page1Layout.addWidget(QPushButton("Go to Page 2"))
        page1.setLayout(page1Layout)

        # Page 2 Content
        page2Layout = QVBoxLayout()
        page2Layout.addWidget(QLabel("This is Page 2"))
        page2Layout.addWidget(QPushButton("Back to Page 1"))
        page2.setLayout(page2Layout)

        # Splitter Example
        splitter = QSplitter()
        leftWidget = QWidget()
        rightWidget = QWidget()
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()
        leftWidget.setLayout(leftLayout)
        rightWidget.setLayout(rightLayout)
        splitter.addWidget(leftWidget)
        splitter.addWidget(rightWidget)

        # Adding Widgets to Layout
        outerLayout.addWidget(stackedWidget)
        outerLayout.addWidget(splitter)

        layoutExperimentTab.setLayout(outerLayout)
        return layoutExperimentTab

    def expandableListTabUI(self):
        expandableListTab = QWidget()
        outerLayout = QVBoxLayout()

        # Create Expandable Sections
        self.expandableGroupBoxes = []

        # Section 1
        section1 = QGroupBox("Section 1")
        section1.setCheckable(True)
        section1.setChecked(True)
        section1Layout = QVBoxLayout()
        section1Layout.addWidget(QPushButton("Button 1.1"))
        section1Layout.addWidget(QPushButton("Button 1.2"))
        section1.setLayout(section1Layout)
        self.expandableGroupBoxes.append(section1)

        # Section 2
        section2 = QGroupBox("Section 2")
        section2.setCheckable(True)
        section2Layout = QVBoxLayout()
        section2Layout.addWidget(QPushButton("Button 2.1"))
        section2Layout.addWidget(QPushButton("Button 2.2"))
        section2.setLayout(section2Layout)
        self.expandableGroupBoxes.append(section2)

        # Section 3
        section3 = QGroupBox("Section 3")
        section3.setCheckable(True)
        section3Layout = QVBoxLayout()
        section3Layout.addWidget(QPushButton("Button 3.1"))
        section3Layout.addWidget(QPushButton("Button 3.2"))
        section3.setLayout(section3Layout)
        self.expandableGroupBoxes.append(section3)

        # Add sections to layout
        for groupBox in self.expandableGroupBoxes:
            outerLayout.addWidget(groupBox)

        # Connect signals
        for groupBox in self.expandableGroupBoxes:
            groupBox.toggled.connect(self.onGroupBoxToggled)

        expandableListTab.setLayout(outerLayout)
        return expandableListTab

    def treeViewTabUI(self):
        treeViewTab = QWidget()
        layout = QVBoxLayout()

        # Create the tree view with dummy data
        treeView = QTreeView()
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['File Structure'])

        # Dummy data for the tree view
        rootNode = model.invisibleRootItem()

        videoFolder = QStandardItem('Video Files')
        videoFile1 = QStandardItem('Climb_Video_1.mp4')
        videoFile2 = QStandardItem('Climb_Video_2.mp4')

        videoFolder.appendRow(videoFile1)
        videoFolder.appendRow(videoFile2)
        rootNode.appendRow(videoFolder)

        model.appendRow(QStandardItem('Settings'))

        treeView.setModel(model)

        # Create metadata display
        metadataGroup = QGroupBox("Video Metadata")
        metadataLayout = QFormLayout()

        # Adding dummy metadata
        metadataLayout.addRow(QLabel("Title:"), QLabel("Climb_Video_1.mp4"))
        metadataLayout.addRow(QLabel("Duration:"), QLabel("10:45"))
        metadataLayout.addRow(QLabel("Resolution:"), QLabel("1920x1080"))
        metadataLayout.addRow(QLabel("Format:"), QLabel("MP4"))
        metadataLayout.addRow(QLabel("Size:"), QLabel("500 MB"))

        metadataGroup.setLayout(metadataLayout)

        # Add tree view and metadata to the layout
        layout.addWidget(treeView)
        layout.addWidget(metadataGroup)

        treeViewTab.setLayout(layout)
        return treeViewTab

    def poseDetectionResultsTabUI(self):
        poseDetectionResultsTab = QWidget()
        layout = QVBoxLayout()

        # Create the tree view with dummy pose detection results
        treeView = QTreeView()
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Pose Detection Results'])

        # Dummy data for the tree view
        rootNode = model.invisibleRootItem()

        poseResults = QStandardItem('Pose Detection Results')
        videoSegment1 = QStandardItem('Segment 1')
        pose1 = QStandardItem('Pose A')
        pose2 = QStandardItem('Pose B')
        videoSegment1.appendRow(pose1)
        videoSegment1.appendRow(pose2)

        videoSegment2 = QStandardItem('Segment 2')
        pose3 = QStandardItem('Pose C')
        pose4 = QStandardItem('Pose D')
        videoSegment2.appendRow(pose3)
        videoSegment2.appendRow(pose4)

        poseResults.appendRow(videoSegment1)
        poseResults.appendRow(videoSegment2)
        rootNode.appendRow(poseResults)

        model.appendRow(QStandardItem('Other Data'))

        treeView.setModel(model)

        # Create metadata display for pose detection results
        metadataGroup = QGroupBox("Pose Detection Metadata")
        metadataLayout = QFormLayout()

        # Adding dummy metadata
        metadataLayout.addRow(QLabel("Video Segment:"), QLabel("Segment 1"))
        metadataLayout.addRow(QLabel("Pose Detected:"), QLabel("Pose A"))
        metadataLayout.addRow(QLabel("Confidence:"), QLabel("85%"))
        metadataLayout.addRow(QLabel("Duration:"), QLabel("2:15"))
        metadataLayout.addRow(QLabel("Additional Notes:"), QLabel("Good alignment, needs improvement in reach"))

        metadataGroup.setLayout(metadataLayout)

        # Add tree view and metadata to the layout
        layout.addWidget(treeView)
        layout.addWidget(metadataGroup)

        poseDetectionResultsTab.setLayout(layout)
        return poseDetectionResultsTab

    def onGroupBoxToggled(self, checked):
        sender = self.sender()
        if checked:
            for groupBox in self.expandableGroupBoxes:
                if groupBox != sender:
                    groupBox.setChecked(False)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi *.mkv)")
        if fileName:
            print(f"Selected file: {fileName}")


def gui_layout_draft_main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    window = Window()
    window.show()
    sys.exit(app.exec_())
