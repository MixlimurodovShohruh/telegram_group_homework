from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    users_id = []
    for user in data["messages"]:
        if user.get("actor_id") != None:
            # if users_id[-1] != user["actor_id"]:
                users_id.append(user["actor_id"])
        elif user.get("from_id"):
            # if users_id[-1] != user["from_id"]:
                users_id.append(user["from_id"])

        
    print(list(set(users_id)))

data = read_data("data/result.json")
find_all_users_id(data)