import pytest
from app.drive_services import convert_folder_link_to_id

@pytest.mark.parametrize("folder_link, expected", [
    ("https://drive.google.com/drive/folders/1my5S5mOPaIk7jkQOv-P62_dpLwAmFpnm?usp=drive_link", "1my5S5mOPaIk7jkQOv-P62_dpLwAmFpnm"),
    ("https://drive.google.com/drive/folders/1my5S5mOPaIk7jkQOv-P62_dpLwAmFpnm", "1my5S5mOPaIk7jkQOv-P62_dpLwAmFpnm"),
    # ("https://drive.google.com/drive/folders/", pytest.raises(ValueError, match="he provided link is not a valid Google Drive folder link.")),
    # ("http://example.com/page?param1=value1&param2=value2", ValueError("The provided link is not a valid Google Drive folder link.")),
])

def test_convert_folder_link_to_id(folder_link, expected):
    folder_id = convert_folder_link_to_id(folder_link)
    assert folder_id == expected

if __name__ == "__main__":
    test_convert_folder_link_to_id()