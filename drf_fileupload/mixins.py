"""
    mixins
    ~~~~~~

    Inspired by rest_framework.mixins for composable file uploads
"""

from rest_framework.response import Response


class FileUploadModelMixin:
    """ Upload a file to an existing model instance field

    In most cases a serializer & model with an ImageField
    field is returned from `get_object` & `get_serializer`
    where the serializer has one field named 'file'.
    """

    def upload(self, request, *args, **kwargs):
        """ Custom action handler """

        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_upload(serializer)

        headers = self.get_upload_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

    def perform_upload(self, serializer):
        """ Perform the actual upload """

        serializer.save()

    def get_upload_success_headers(self, data):
        """ Include the Location header of the uploaded files URL """

        try:
            return {'Location': data['file']}
        except (TypeError, KeyError):
            return {}
