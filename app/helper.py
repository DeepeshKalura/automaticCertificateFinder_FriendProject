def remove_query_param(url: str, param: str) -> str:
    """
    Removes the specified query parameter from the given URL.

    Args:
        url (str): The URL from which the query parameter needs to be removed.
        param (str): The query parameter to be removed.

    Returns:
        str: The updated URL with the query parameter removed.
    """
    param_start = url.find(param)
    
    if param_start != -1:
        param_end = url.find('&', param_start)
        if param_end == -1:
            param_end = len(url)
        else:
            param_end += 1 
        url = url[:param_start] + url[param_end:]
    
    return url