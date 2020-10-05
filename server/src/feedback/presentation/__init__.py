import flask

from feedback.presentation.support import SupportFeedbackListView, SupportFeedbackView
from feedback.presentation.user import (
    UserFeedbackListView,
    UserFeedbackView,
    UserFeedbackCommentView,
)


def register_feedback_blueprints(blueprint: flask.Blueprint) -> None:
    # for customer user
    blueprint.add_url_rule(
        "/user/users/<user_id>/feedbacks",
        view_func=UserFeedbackListView.as_view("paths/user/feedbacks"),
        methods=["GET", "POST"],
    )

    blueprint.add_url_rule(
        "/user/users/<user_id>/feedbacks/<feedback_id>",
        view_func=UserFeedbackView.as_view("paths/user/feedback"),
        methods=["GET"],
    )

    blueprint.add_url_rule(
        "/user/users/<user_id>/feedbacks/<feedback_id>/comments",
        view_func=UserFeedbackCommentView.as_view("paths/user/feedback/comments"),
        methods=["POST"],
    )

    # for support
    blueprint.add_url_rule(
        "/support/users/<user_id>/feedbacks",
        view_func=SupportFeedbackListView.as_view("paths/support/feedbacks"),
        methods=["GET"],
    )
    blueprint.add_url_rule(
        "/support/users/<user_id>/feedbacks/<feedback_id>",
        view_func=SupportFeedbackView.as_view("paths/support/feedback"),
        methods=["GET"],
    )
