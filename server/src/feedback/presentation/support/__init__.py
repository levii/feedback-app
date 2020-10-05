import flask.views
from werkzeug.exceptions import Forbidden

from common.user.domain.key import UserKey
from common.user.domain.user import SupportUser
from common.user.domain.user_repository import UserRepository
from feedback.application.support.feedback_comment_create_service import (
    FeedbackCommentCreateService,
)
from feedback.application.support.feedback_fetch_service import FeedbackFetchService
from feedback.application.support.feedbacks_fetch_service import FeedbacksFetchService
from feedback.domain.comment import FeedbackCommentBody
from feedback.domain.key import FeedbackKey
from framework import utcnow_with_tz
from framework.container import container


class SupportFeedbackListView(flask.views.MethodView):
    def get(self, user_id: str) -> str:
        user_repository = container.get(UserRepository)
        feedbacks_fetch_service: FeedbacksFetchService = container.get(
            FeedbacksFetchService
        )

        user_key = UserKey.build(user_id)
        current_user = user_repository.fetch_by_key(user_key)
        if not isinstance(current_user, SupportUser):
            raise Forbidden()

        feedbacks = feedbacks_fetch_service.execute(user=current_user)

        return flask.render_template(
            "feedback/support/feedbacks.html",
            current_user=current_user,
            feedbacks=feedbacks,
        )


class SupportFeedbackView(flask.views.MethodView):
    def get(self, user_id: str, feedback_id: str) -> str:
        user_repository = container.get(UserRepository)
        feedback_fetch_service: FeedbackFetchService = container.get(
            FeedbackFetchService
        )

        user_key = UserKey.build(user_id)
        feedback_key = FeedbackKey.build(feedback_id)
        current_user = user_repository.fetch_by_key(user_key)
        if not isinstance(current_user, SupportUser):
            raise Forbidden()

        feedback = feedback_fetch_service.execute(
            user=current_user, feedback_key=feedback_key
        )

        return flask.render_template(
            "feedback/support/feedback.html",
            current_user=current_user,
            feedback=feedback.feedback,
            comments=feedback.comments,
        )


class SupportFeedbackCommentView(flask.views.MethodView):
    def post(self, user_id: str, feedback_id: str) -> flask.Response:
        user_repository = container.get(UserRepository)
        feedback_comment_create_service: FeedbackCommentCreateService = container.get(
            FeedbackCommentCreateService
        )

        user_key = UserKey.build(user_id)
        feedback_key = FeedbackKey.build(feedback_id)
        current_user = user_repository.fetch_by_key(user_key)
        if not isinstance(current_user, SupportUser):
            raise Forbidden()

        feedback_comment_create_service.execute(
            user=current_user,
            feedback_key=feedback_key,
            feedback_comment_body=FeedbackCommentBody(
                f"サポートユーザからのコメントです - {utcnow_with_tz().isoformat()}"
            ),
        )

        return flask.redirect(
            location=f"/support/users/{user_id}/feedbacks/{feedback_id}",
            Response=flask.Response,
        )
