import flask

from common.user.presentation.user_list import UserListPage


def register_user_blueprints(blueprint: flask.Blueprint):
    blueprint.add_url_rule(
        "/users",
        view_func=UserListPage.as_view("paths/users"),
        methods=["GET"]
    )
