import flask.views

from common.user.domain.key import UserKey
from common.user.domain.user_repository import UserRepository
from feedback.application.user.feedback_create_service import FeedbackCreateService
from feedback.application.user.feedback_fetch_service import FeedbackFetchService
from feedback.application.user.feedbacks_fetch_service import FeedbacksFetchService
from feedback.domain.feedback import FeedbackTitle, FeedbackDescription
from feedback.domain.key import FeedbackKey
from framework import utcnow_with_tz
from framework.container import container


class UserFeedbackListView(flask.views.MethodView):
    def get(self, user_id: str) -> str:
        user_repository = container.get(UserRepository)
        feedbacks_fetch_service: FeedbacksFetchService = container.get(
            FeedbacksFetchService
        )

        user_key = UserKey.build(user_id)
        current_user = user_repository.fetch_by_key(user_key)
        feedbacks = feedbacks_fetch_service.execute(user=current_user)

        return flask.render_template(
            "feedback/user/feedbacks.html",
            current_user=current_user,
            feedbacks=feedbacks,
        )

    def post(self, user_id: str) -> flask.Response:
        user_repository = container.get(UserRepository)
        feedback_create_service: FeedbackCreateService = container.get(
            FeedbackCreateService
        )

        user_key = UserKey.build(user_id)
        current_user = user_repository.fetch_by_key(user_key)
        feedback_create_service.execute(
            user=current_user,
            title=FeedbackTitle(f"作成した要望 - {utcnow_with_tz().isoformat()}"),
            description=FeedbackDescription("要望本文"),
        )

        return flask.redirect(location=flask.request.path, Response=flask.Response)


class UserFeedbackView(flask.views.MethodView):
    def get(self, user_id: str, feedback_id: str) -> str:
        user_repository = container.get(UserRepository)
        feedback_fetch_service: FeedbackFetchService = container.get(
            FeedbackFetchService
        )

        user_key = UserKey.build(user_id)
        feedback_key = FeedbackKey.build(feedback_id)
        current_user = user_repository.fetch_by_key(user_key)
        feedback = feedback_fetch_service.execute(
            user=current_user, feedback_key=feedback_key
        )

        return flask.render_template(
            "feedback/user/feedback.html",
            current_user=current_user,
            feedback=feedback.feedback,
            comments=feedback.comments,
        )
