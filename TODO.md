# PyBoulder TODOs

## Project Roadmap

### Phase 1: Initial Setup and Basic Functionaliy

- Project Initialization
  - [ ] Set up project structure
  - [ ] Initialize version control (git -> GitHub)
  - [ ] Create a basic README file
- Basic Video Processing and Pose Detection
  - [ ] Implement video loading and display
  - [ ] Integrate MediaPipe for pose detection
  - [ ] Display detected poses on the video feed
- Testing Framework
  - [ ] Set up `pytest` for testing
  - [ ] Write basic tests for video processing functions

### Phase 2: Core Features

- Pose Data Extraction
  - [ ] Extract and log pose landmark data
  - [ ] Save pose data to a file (e.g. CSV or JSON)
- Movement Metrics Calculation
  - [ ] Calculate basic metrics (e.g. reach, body angles)
  - [ ] Display metrics on the video feed
- User Interface
  - [ ] Create a simple GUI for loading videos and displaying results
  - [ ] Use libraries like `tkinter` or `PyQt`

### Phase 3: Advanced Features

- Data Visualization
  - [ ] Implement advanced data visualization for metrics and trends
  - [ ] Use libraries like `Matplotlib` or `Plotly`
- Movement Analysis and Feedback
  - [ ] Implement algorithms to analyze movement patterns
  - [ ] Provide real-time feedback on movement efficiency and technique
- Performance Optimization
  - [ ] Optimize video processing for real-time performance
  - [ ] Handle high-resolution videos and reduce latency


### Phase 4: Extended Functionality

- Machine Learning Integration
  - [ ] Integrate machine learning models to classify movements
  - [ ] Train models on collected pose data to predict performance
- Multiple Camera Support
  - [ ] Implement support for multiple video inputs
  - [ ] Synchronize and analyze data from mutliple cameras
- User Profiles and Progress Tracking
  - [ ] Implement user profile management
  - [ ] Track and visualize user progress over time

### Phase 5: Final Polishing and Deployment

- Comprehensive Testing and Bug Fixing
  - [ ] Conduct extensive testing and fix any bugs
  - [ ] Ensure all features work seamlessly (test campaign)
- Documentation
  - [ ] Write detailed documentation for users and developers (if not already happened)
  - [ ] Include usage guides, API documentation and setup instructions (if not already happened)
- Deployment
  - [ ] Prepare the project for deployment
  - [ ] Consider packaging the project as a standalone application

### Project Structure

```txt
PyBoulder/
│
├── pyboulder/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── video_processor.py   # Basic Video Processing and Pose Detection
│   │   ├── pose_detection.py     # MediaPipe integration
│   │   └── metrics.py            # Movement Metrics Calculation
│   │
│   ├── data_processing/
│   │   ├── __init__.py
│   │   ├── data_extraction.py    # Pose Data Extraction
│   │   ├── data_saving.py        # Save data to file (CSV/JSON)
│   │
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── gui.py                # User Interface with `tkinter` or `PyQt`
│   │
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── movement_analysis.py  # Movement Analysis and Feedback
│   │   └── feedback.py           # Real-time feedback
│   │
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── visualizer.py         # Advanced Data Visualization
│   │
│   ├── ml/
│   │   ├── __init__.py
│   │   ├── model.py              # Machine Learning Models
│   │   └── training.py           # Model Training
│   │
│   ├── multi_camera/
│   │   ├── __init__.py
│   │   ├── camera_handler.py     # Multiple Camera Support
│   │   └── synchronization.py    # Synchronize camera feeds
│   │
│   ├── user_management/
│   │   ├── __init__.py
│   │   ├── profiles.py           # User Profile Management
│   │   └── progress_tracking.py  # Track and visualize user progress
│   │
│   └── main.py                   # Entry point of the application
│
├── data/                        # Folder to store extracted pose data
│   └── .gitkeep                 # Ensures the data directory is tracked
│
├── docs/                        # Documentation files
│   └── .gitkeep                 # Ensures the docs directory is tracked
│
├── tests/
│   └── ...
│
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── requirements-dev.txt
├── setup.py                    # For package distribution
└── TODO.md
```
