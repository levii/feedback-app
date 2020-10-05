import flask

from feedback.presentation.user import UserFeedbackListView, UserFeedbackView


def register_feedback_blueprints(blueprint: flask.Blueprint) -> None:
    blueprint.add_url_rule(
        "/user/users/<user_id>/feedbacks",
        view_func=UserFeedbackListView.as_view("paths/user/feedbacks"),
        methods=["GET", "POST"],
    )

    blueprint.add_url_rule(
        "/user/users/<user_id>/feedbacks/<feedback_id>",
        view_func=UserFeedbackView.as_view("paths/user/feedback"),
        methods=["GET", "POST"],
    )
