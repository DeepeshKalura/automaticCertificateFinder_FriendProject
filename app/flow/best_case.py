# convert limk into the id --> then check it exit in a databse or not 
# --> if yes then check the user exit in the databse or not 
# --> if yes then we will going to get the url of the pdf file and we will download it


from app.cache import folder_id_exists, file_exists

def  hit_in_database(folder_id: str):
    """
    Checks whether the provided folder ID exists in the database.

    Args:
        folder_id (str): The folder ID to check.

    Returns:
        bool: True if the folder ID exists in the database, False otherwise.
    """
    return folder_id_exists(folder_id) != None

def find_user_in_the_database(folder_id: str, user_name: str):
    """
    Find the user in the database based on the given folder ID and user name.

    Args:
        folder_id (str): The ID of the folder to search in.
        user_name (str): The name of the user to find.

    Returns:
        str: The file ID of the user if found, otherwise "-1".
    """
    file = file_exists(user_name, folder_id)

    if file is not None:
        return file.get('file_id')
    else:
        return "-1"



    



