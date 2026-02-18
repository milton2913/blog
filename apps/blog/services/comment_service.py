from apps.blog.forms import CommentForm
from apps.blog.models.comment import Comment

class CommentService:
    @staticmethod
    def handle_comment_submission(post, request_data, user=None):
        form = CommentForm(request_data)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            if user and user.is_authenticated:
                comment.author = user
            
            parent_id = request_data.get('parent_id')
            if parent_id:
                try:
                    parent_comment = Comment.objects.get(id=parent_id)
                    comment.parent = parent_comment
                except Comment.DoesNotExist:
                    pass
            
            comment.save()
            return comment, form
        return None, form

    @staticmethod
    def get_active_root_comments(post):
        return post.comments.filter(active=True, parent__isnull=True)
