import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))

from app.helper import remove_query_param

@pytest.mark.parametrize("input_url, parameter, expected_output", [

    # above two are the important test cases
    ("https://drive.google.com/drive/folders/1my5S5mOPaIk7jkQOv-P62_dpLwAmFpnm?usp=drive_link", "?usp=drive_link", "https://drive.google.com/drive/folders/1my5S5mOPaIk7jkQOv-P62_dpLwAmFpnm"),  
    ("https://drive.google.com/drive/folders/1my5S5mOPaIk7jkQOv-P62_dpLwAmFpnm", "?usp=drive_link", "https://drive.google.com/drive/folders/1my5S5mOPaIk7jkQOv-P62_dpLwAmFpnm"),
    
    ("http://example.com/page?param1=value1&param2=value2", "param1", "http://example.com/page?param2=value2"),  
])

def test_remove_query_param(input_url, parameter,  expected_output):
    new_url_link = remove_query_param(input_url, parameter)
    assert new_url_link == expected_output
    

if __name__ == "__main__":
    test_remove_query_param()