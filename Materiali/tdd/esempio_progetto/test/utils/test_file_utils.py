# tests/utils/test_file_utils.py - test per il modulo di utilità file_utils
import file_utils

def test_count_lines_empty_file():
    assert file_utils.count_lines('tests/utils/data/empty_file.txt') == 0

def test_count_lines_single_line_file():
    assert file_utils.count_lines('tests/utils/data/single_line_file.txt') == 1

def test_count_lines_multi_line_file():
    assert file_utils.count_lines('tests/utils/data/multi_line_file.txt') == 3
