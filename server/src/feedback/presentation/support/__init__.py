import flask.views
from werkzeug.exceptions import Forbidden

from common.user.domain.key import UserKey
from common.user.domain.user import SupportUser
from common.user.domain.user_repository import UserRepository
from feedback.application.support.feedbacks_fetch_service import FeedbacksFetchService
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
