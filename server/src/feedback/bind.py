from feedback.domain.repository import FeedbackRepository
from feedback.infrastructure.repository import InMemoryFeedbackRepository
from framework.container import container

container.binder.bind(interface=FeedbackRepository, to=InMemoryFeedbackRepository)
