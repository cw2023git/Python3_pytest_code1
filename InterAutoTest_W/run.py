
# print('hello world!')

import os
import pytest
from config import config

if __name__ == '__main__':
    report_path=config.get_report_path()+os.sep+"result"
    report_html_path=config.get_report_path()+os.sep+"html"

    # pytest.main(["-s","test_excel_case.py","--alluredir",report_path])
    pytest.main(["-s","--alluredir",report_path])


























































