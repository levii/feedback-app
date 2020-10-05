from common.user.domain.key import UserKey
from common.user.domain.user import (
    UserName,
    CompanyName,
    CustomerUser,
    SupportUser,
)
from feedback.domain.comment import (
    FeedbackComment,
    FeedbackCommentBody,
    FeedbackCommentCollection,
)

from feedback.domain.feedback import (
    Feedback,
    FeedbackTitle,
    FeedbackDescription,
    FeedbackStatus,
    FeedbackWithComments,
    FeedbackCollection,
)

# 要望一覧
feedbacks = FeedbackCollection.build([])

# 顧客「山田 太郎」としてログイン
login_user = CustomerUser.build(
    key=UserKey.build("c10001"),
    name=UserName("山田 太郎"),
    company_name=CompanyName("株式会社ラビィ"),
)

# 要望を登録する
requested_feedback = Feedback.build_new(
    user=login_user,
    title=FeedbackTitle("IE11でも動くようにして欲しい"),
    description=FeedbackDescription("会社でふだん使っているブラウザ(IE11)でも動くようにしてほしいです。"),
)
feedbacks.append(requested_feedback)

# カスタマーサポート「佐藤 次郎」としてログイン
support_user = SupportUser.build(key=UserKey.build("s10099"), name=UserName("佐藤 次郎"),)
# カスタマーサポートの担当者が、新着の要望を確認する
new_feedbacks = feedbacks.filter_by_status(status=FeedbackStatus.New)

# 新着の要望を順に確認する (最初の要望を取り出す)
new_feedback = next(iter(new_feedbacks))
# 確認した要望のステータスを [確認済み] に変更する
accepted_feedback = new_feedback.with_status(status=FeedbackStatus.Accepted)

# カスタマーサポートから顧客に対して要望内容について問い合わせる（コメントを送る）
support_comment = FeedbackComment.build_new(
    feedback_key=accepted_feedback.key,
    comment_user=support_user,
    body=FeedbackCommentBody("...."),
)

# 要望と、その要望に対するコメントはひと塊として取り扱いたい
feedback_with_comments = FeedbackWithComments.build(
    feedback=accepted_feedback,
    comments=FeedbackCommentCollection.build([support_comment]),
)

# 顧客が、サポートからのコメントに対して返信コメントを返す
reply_comment = FeedbackComment.build_new(
    feedback_key=accepted_feedback.key,
    comment_user=login_user,
    body=FeedbackCommentBody("...."),
)
feedback_with_comments.comments.append(reply_comment)

# サポートがコメントを確認して、要望を「対応中」ステータスに変更する
implementing_feedback = feedback_with_comments.feedback.with_status(
    status=FeedbackStatus.Implementing
)

# サポートが要望を「リリース済み」ステータスに変更して、顧客にコメントで連絡する
released_feedback = implementing_feedback.with_status(status=FeedbackStatus.Released)
feedback_with_comments = FeedbackWithComments.build(
    feedback=released_feedback,
    comments=FeedbackCommentCollection.build(feedback_with_comments.comments),
)
release_comment = FeedbackComment.build_new(
    feedback_key=accepted_feedback.key,
    comment_user=support_user,
    body=FeedbackCommentBody("...."),
)
feedback_with_comments.comments.append(release_comment)
