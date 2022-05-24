from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
# from django.http import HttpResponse
from .models import Posts, Comments


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class Login(APIView):
    def get(self, req):
        user = req.session.get('user', False)
        if user:
            return Response({"user": user})
        else:
            return Response(status=400, data={"message": "To proceed further, please add user name via HTTP.POST"})

    def post(self, req):
        user = req.data.get('user')
        if user:
            req.session['user'] = user
            return Response({"message": "Switched to user", "user": user})
        else:
            return Response(status=400,
                            data={"message": "POST a valid json, {\"user\": \"<username>\"}"})


class TimeLineApi(APIView):
    def get(self, req):
        posts = Posts.objects.all()
        post_serializer = PostSerializer(posts, many=True)
        comments = Comments.objects.all()
        comment_serializer = CommentSerializer(comments, many=True)
        return Response({"posts": post_serializer.data, "comments": comment_serializer.data})


class CommentsApi(APIView):
    def post(self, req):
        comment_text = req.data.get('comment_text')
        root_post = req.data.get('root_post')
        parent_comment = req.data.get('parent_comment')
        if not all([comment_text, root_post, parent_comment]):
            return Response(status=400, data={"message": "Missing fields.",
                                              "fields": "[comment_text, root_post, parent_comment]"})
        comment = Comments(comment_text=comment_text, root_post_id=root_post, parent_comment_id=parent_comment)
        comment.save()
        return Response({"message": "Created", "comment": comment.comment_text})


class PostApi(APIView):
    def post(self, req):
        user = req.session['user']
        post_data = req.data.get('post_content')
        if not user:
            return Response(status=400,
                            data={"message": "To add a post, Please switch to a user at /app/user "})
        if not post_data:
            return Response(status=400,
                            data={"message": "To add a post, Please add some content as {\"post_content\": \"...\"}"})

        p = Posts(post_text=post_data, user=user)
        p.save()
        return Response({"message": "created new post", "content": p.post_text})
