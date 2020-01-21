from rest_framework import serializers

from .models import Comment

import logging
logger = logging.getLogger('django')


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    user_name = serializers.CharField(max_length=200)
    comment_text = serializers.CharField()
    date = serializers.DateField()

    def create(self, validated_data):
        print(validated_data)
        logger.info(f'New data added: user_name={validated_data["user_name"]}; comment_text={validated_data["comment_text"]}')
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.comment_text = validated_data.get('comment_text', instance.comment_text)
        logger.info('Information update!')
        instance.save()
        return instance
