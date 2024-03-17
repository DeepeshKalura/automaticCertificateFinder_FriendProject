from app.drive_services import convert_folder_link_to_id,  get_pdf_from_file_id
from app.flow import best_case


def flow(folder_link : str, user_name: str ):
    try:
        folder_id = convert_folder_link_to_id(folder_link)
        if(best_case.hit_in_database(folder_id)):
            if(best_case.find_user_in_the_database(user_name, folder_id)):
                return get_pdf_from_file_id(folder_id, user_name)
            else:
                return "We does not find your certificate."
        else:
            return "Not the best case senario. Need to do work case sernerio."
    except Exception as e:
        raise(e)


