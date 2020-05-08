from accounts.api.serializers import UserPublicSerializer
from status.models import Status
from rest_framework.reverse import reverse as api_reverse
from rest_framework import serializers
uri = serializers.SerializerMethodField(read_only=True)


'''
Serializers -> JSON
Serializers -> Validate Data
'''


class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    # user = serializers.SerializerMethodField(read_only=True)

    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user']  # GET

    # For single fieldstatus-list
    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError("This is way too long.")
    #     return value

    # def get_user(self, obj):
    #     request = self.context.get('request')
    #     user = obj.user
    #     return UserPublicSerializer(user, read_only=True, context={'request': request}).data

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-status:detail", kwargs={"id": obj.id}, request=request)

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None

        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data


# class StatusInlineUserSerializer(StatusSerializer):
#     # uri = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = Status
#         fields = [
#             'uri',
#             'id',
#             'content',
#             'image'
#         ]

#     # For single field
#     # def validate_content(self, value):
#     #     if len(value) > 10000:
#     #         raise serializers.ValidationError("This is way too long.")
#     #     return value

#     # def get_uri(self, obj):
#     #     return "/api/status/{id}/".format(id=obj.id)


class StatusInlineUserSerializer(serializers.ModelSerializer):
    # uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'content',
            'image'
        ]
        # read_only_fields = ['user']  # GET

    # For single field
    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError("This is way too long.")
    #     return value

    # def get_uri(self, obj):
    #     return "/api/status/{id}/".format(id=obj.id)
