from framework.container import container
from common.user.domain.user_repository import UserRepository
from common.user.infrastructure.user_repository import InMemoryUserRepository

container.binder.bind(interface=UserRepository, to=InMemoryUserRepository)
