"""
File: test_main.py
Author: Steven "Kabbe" Karbjinsky
Description: Contains a test for the main function in the PyBoulder project, verifying that it prints "Hello World!".

For more information, see: https://github.com/xKabbe/pyboulder
"""
from pyboulder.main import main


def test_main_output(capsys):
    main()

    captured = capsys.readouterr()
    assert captured.out.strip() == 'Hello World!'
