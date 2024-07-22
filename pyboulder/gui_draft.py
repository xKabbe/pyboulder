import sys
import cv2
import qdarkstyle
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, \
    QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import QTimer, pyqtSignal, QThread
import mediapipe as mp


class VideoAnalyzerWorker(QThread):
    update_landmarks_signal = pyqtSignal(list)

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self._running = True

    def run(self):
        mediapipe_drawing = mp.solutions.drawing_utils
        mediapipe_pose = mp.solutions.pose

        capture = cv2.VideoCapture(self.file_path)

        if not capture.isOpened():
            print(f'Error: Could not open video file "{self.file_path}"')
            return

        with mediapipe_pose.Pose() as pose:
            while self._running and capture.isOpened():
                ret, frame = capture.read()
                if not ret:
                    break

                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                results = pose.process(image)

                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.pose_landmarks:
                    mediapipe_drawing.draw_landmarks(image, results.pose_landmarks, mediapipe_pose.POSE_CONNECTIONS)

                    landmarks = [
                        {
                            'id': idx,
                            'x': landmark.x,
                            'y': landmark.y,
                            'z': landmark.z,
                            'visibility': landmark.visibility
                        }
                        for idx, landmark in enumerate(results.pose_landmarks.landmark)
                    ]
                    self.update_landmarks_signal.emit(landmarks)

                cv2.imshow('Bouldering Pose Detection', image)

                key = cv2.waitKey(1) & 0xFF
                if key == ord('q') or key == 27:
                    break

                if cv2.getWindowProperty('Bouldering Pose Detection', cv2.WND_PROP_VISIBLE) < 1:
                    break

        capture.release()
        cv2.destroyAllWindows()

    def stop(self):
        self._running = False
        self.quit()
        self.wait()


class VideoAnalyzerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyBoulder')
        self.resize(1200, 1000)

        # "Analyze Video" Button
        self.analyze_video_button = QPushButton('Analyze Video')
        self.analyze_video_button.clicked.connect(self._click_analyze_button)

        # "Show Log" Button
        self.show_log_button = QPushButton('Show Log')
        self.show_log_button.clicked.connect(self._click_show_log_button)

        # "Landmarks" Table
        self.landmark_table = QTableWidget()
        self.landmark_table.setColumnCount(5)
        self.landmark_table.setHorizontalHeaderLabels(['ID', 'X', 'Y', 'Z', 'Visibility'])
        self.landmark_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # TODO: Add Video Metadata Display
        pass

        # TODO: Add Progress Bar (of Video Analysis)
        pass

        # TODO: Add Start/Pause Button
        pass

        # TODO: Add slider for Video Scrubbing
        pass

        # TODO: Add Save Log Button
        pass

        # TODO: Add Settings Panel
        pass

        # Create layout with components
        layout = QVBoxLayout()
        layout.addWidget(self.analyze_video_button)
        layout.addWidget(self.show_log_button)
        layout.addWidget(self.landmark_table)

        # Create container for layout
        container = QWidget()
        container.setLayout(layout)

        # Set the central widget
        self.setCentralWidget(container)

        # Initialize landmark data
        self.landmark_data = []

        # Timer for updating table
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self._update_landmark_table)

    def _click_analyze_button(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select Video File', '', 'Video Files (*.mp4 *.avi *.mkv)')
        if file_path:
            try:
                self.worker = VideoAnalyzerWorker(file_path)
                self.worker.update_landmarks_signal.connect(self._update_landmark_data)
                self.worker.start()
                self.update_timer.start(100)  # Update every 100 ms
            except Exception as e:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Critical)
                error_dialog.setText(str(e))
                error_dialog.setWindowTitle('Error')
                error_dialog.exec_()

    def _update_landmark_data(self, landmarks):
        self.landmark_data = landmarks

    def _update_landmark_table(self):
        if not self.landmark_data:
            return

        # Flatten landmark data for display
        flat_data = [
            [
                landmark['id'],
                f"{landmark['x']:.4f}",
                f"{landmark['y']:.4f}",
                f"{landmark['z']:.4f}",
                f"{landmark['visibility']:.4f}"
            ]
            for landmark in self.landmark_data
        ]

        # Update table with landmark data
        self.landmark_table.setRowCount(len(flat_data))
        for row_idx, row_data in enumerate(flat_data):
            for col_idx, item_data in enumerate(row_data):
                item = QTableWidgetItem(item_data)
                self.landmark_table.setItem(row_idx, col_idx, item)

    def _click_show_log_button(self):
        print(2)

    def closeEvent(self, event):
        # Stop the video processing worker and timer
        if hasattr(self, 'worker'):
            self.worker.stop()
        self.update_timer.stop()
        super().closeEvent(event)


def gui_draft_main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    window = VideoAnalyzerWindow()
    window.show()

    sys.exit(app.exec_())
