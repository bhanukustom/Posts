from django.db import models


class Posts(models.Model):
	post_text = models.CharField(max_length=250)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	user = models.CharField(max_length=100, default='non-user')

	def __str__(self):
		return f'{self.id}:{self.user[:11]}={self.post_text[:16]}'


class Comments(models.Model):
	comment_text = models.CharField(max_length=250)
	comment_date = models.DateTimeField('commented_on', auto_now_add=True)
	root_post = models.ForeignKey(Posts, on_delete=models.CASCADE)
	parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f'<P:{self.root_post_id}/C:{self.parent_comment_id}>={self.comment_text[:26]}'
