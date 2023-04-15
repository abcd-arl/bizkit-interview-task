from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    if not args: return USERS

    group = {}
    for parameter in args.keys():
        group[parameter] = []

    for user in USERS:
        parameter = None
        if "id" in args and args["id"] == user["id"]: parameter = "id"
        elif "name" in args and args["name"].lower() in user["name"].lower(): parameter = "name"
        elif "age" in args and int(args["age"]) >= user["age"]-1 and int(args["age"]) <= user["age"]+1: parameter = "age"
        elif "occupation" in args and args["occupation"].lower() in user["occupation"].lower(): parameter = "occupation"

        if parameter is not None:
            group[parameter].append(user)


    return [user for group in group.values() for user in group]
