import flask.views

from common.user.domain.key import UserKey
from common.user.domain.user_repository import UserRepository
from framework.container import container


class UserFeedbackListView(flask.views.MethodView):
    def get(self, user_id: str) -> str:
        user_key = UserKey.build(user_id)
        user_repository = container.get(UserRepository)
        current_user = user_repository.fetch_by_key(user_key)

        return flask.render_template("feedback/user/feedbacks.html", current_user=current_user)
