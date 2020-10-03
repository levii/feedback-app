import flask.views

from common.user.domain.user_repository import UserRepository
from framework.container import container


class UserListPage(flask.views.MethodView):
    def get(self) -> str:
        user_repository: UserRepository = container.get(UserRepository)
        users = user_repository.fetch_list()

        return flask.render_template("common/user/users.html", users=users)
