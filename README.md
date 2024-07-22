<p align="center">
    <img alt="Static Badge" src="https://img.shields.io/badge/Ascendify-blue" style="width: 425px; height: 130px;">
</p>

<p align="center">
   <a href="https://www.python.org/">
      <img alt="ShieldsIO Badge" src="https://img.shields.io/badge/3.12-555555?logo=python&label=Python&color=44cc11" /></a>
   <a href="https://github.com/xKabbe/ascendify/blob/master/LICENSE">
      <img alt="ShieldsIO Badge" src="https://img.shields.io/github/license/xKabbe/ascendify?label=License&color=yellow" /></a>
   <a href="https://github.com/xKabbe/ascendify/pulse">
      <img alt="ShieldsIO Badge" src="https://img.shields.io/github/commit-activity/m/xKabbe/ascendify?label=Commit%20Activity&color=red" /></a>
   <a href="https://github.com/xKabbe/ascendify/issues?q=is%3Aissue+is%3Aopen+">
      <img alt="ShieldsIO Badge" src="https://img.shields.io/github/issues-search/xKabbe/ascendify?query=is%3Aissue%20is%3Aopen&label=Open%20Issues&color=yellow"></a>
   <a href="https://github.com/xKabbe/ascendify/issues?q=is%3Aissue+is%3Aclosed">
      <img alt="ShieldsIO Badge" src="https://img.shields.io/github/issues-search/xKabbe/ascendify?query=is%3Aissue%20is%3Aclosed&label=Closed%20Issues&color=red"></a>
   <a href="https://github.com/xKabbe/ascendify/actions">
      <img alt="ShieldsIO Badge" src="https://img.shields.io/github/actions/workflow/status/xKabbe/ascendify/test_ascendify.yml?logo=github&label=Tests"></a>
   <a href="https://app.codecov.io/github/xKabbe/ascendify">
      <img alt="ShieldsIO Badge" src="https://img.shields.io/codecov/c/github/xKabbe/ascendify?logo=codecov&label=Codecov%20Coverage"></a>
</p>

<p align="center">
   <a href="https://github.com/xKabbe/ascendify/milestone/1">
      <img alt="ShieldsIO Badge" src="https://img.shields.io/github/milestones/progress-percent/xKabbe/ascendify/1"></a>
   <a href="https://github.com/xKabbe/ascendify/milestone/2">
      <img alt="ShieldsIO Badge" src="https://img.shields.io/github/milestones/progress-percent/xKabbe/ascendify/2"></a>
   <a href="https://github.com/xKabbe/ascendify/milestone/3">
      <img alt="ShieldsIO Badge" src="https://img.shields.io/github/milestones/progress-percent/xKabbe/ascendify/3"></a>
   <a href="https://github.com/xKabbe/ascendify/milestone/4">
      <img alt="ShieldsIO Badge" src="https://img.shields.io/github/milestones/progress-percent/xKabbe/ascendify/4"></a>
   <a href="https://github.com/xKabbe/ascendify/milestone/5">
      <img alt="ShieldsIO Badge" src="https://img.shields.io/github/milestones/progress-percent/xKabbe/ascendify/5"></a>
</p>

`Ascendify` is an open-source tool designed for analyzing and improving bouldering techniques through video analysis.
The project leverages computer vision and pose detection technologies to provide valuable insights into climbing movements.
Whether you're a climber looking to refine your technique or a coach seeking to assess performance, `Ascendify` offers an easy-to-use interface and detailed metrics to help you achieve your goals.

## Features

- **Video Analysis:** Load and process climbing videos to analyze movements.
- **Pose Detection:** Integrates with MediaPipe for accurate pose detection.
- **Movement Metrics:** Extract and visualize key metrics such as reach and body angles.
- **User Interface:** A simple GUI for loading videos and displaying results.
- **Data Logging:** Save pose data and metrics for further analysis.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- [Python 3.12](https://www.python.org/downloads/release/python-3120/) (if running locally without Docker) - Programming language
- [pip](https://pip.pypa.io/en/stable/) - Python package manager

### Installation

1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/xKabbe/ascendify.git
   ```
2. Set up and activate a virtual environment:

   ```shell
   # On linux
   python -m venv path/to/venv
   source path/to/venv/bin/activate

   # On windows
   python -m venv path/to/venv
   source path/to/venv/Scripts/activate
   ```

3. Install project in `editable` mode:
   ```shell
   pip install -e .
   ```
4. Install the production required dependencies:
   ```shell
   pip install -r requirements.txt
   ```
5. Install the testing required dependencies:
   ```shell
   pip install -r requirements-dev.txt
   ```

### Usage

#### Running Application

To run `Ascendify`, use the following command:

```shell
ascendify
```

This will start the application and allow you to load and analyze climbing videos.

#### Running Tests

`Ascendify` uses [pytest](https://docs.pytest.org/en/8.2.x/) for testing. Here are some common commands:

| Command                          | Description                                                              |
|----------------------------------|--------------------------------------------------------------------------|
| `pytest`                         | Run all tests in the current directory and its subdirectories.           |
| `pytest test_module.py`          | Run tests in a specific module.                                          |
| `pytest test_module.py::test_fn` | Run a specific test function in a module.                                |
| `pytest -k expression`           | Run tests that match the given keyword expression.                       |
| `pytest -m marker`               | Run tests that have a specific marker.                                   |
| `pytest --headless`              | Run tests in headless mode (doesn't show browser window).                |
| `pytest --fixtures`              | Show available fixtures.                                                 |
| `pytest --cov=your_module`       | Measure code coverage for your module. Requires the `pytest-cov` plugin. |
| `pytest --junitxml=result.xml`   | Generate JUnit-style XML reports.                                        |
| `pytest --html=report.html`      | Generate an interactive HTML report. Requires the `pytest-html` plugin.  |
| `pytest --durations=n`           | Show n slowest test durations.                                           |
| `pytest --markers`               | Show available markers.                                                  |
| `pytest -h`                      | Display help message and exit.                                           |

#### MkDocs Documentation

`Ascendify` uses [MkDocs](https://www.mkdocs.org) for documentation. Here are some common commands:

| Command        | Description                                                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `mkdocs serve` | This command will start a local development server, and you can access the documentation at http://127.0.0.1:8000/. <br>As you make changes to the documentation files, MkDocs will automatically update the rendered content in your browser |
| `mkdocs build` | This command will build the documentation site                                                                                                                                                                                                |
| `mkdocs -h`    | This command will print the help message and exit                                                                                                                                                                                             |

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

For any questions or support, please reach out to [Steven "Kabbe" Karbjinsky](mailto:steven.karbjinsky@web.de) via Email.
