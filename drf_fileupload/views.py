"""
    views
    ~~~~~

    Inspired by rest_framework.generics
"""

from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.renderers import JSONRenderer

from .mixins import FileUploadModelMixin


class FileUploadAPIView(FileUploadModelMixin, GenericAPIView):
    """ Concrete view for uploading to a model instance """

    parser_classes = (MultiPartParser,)
    renderer_classes = (JSONRenderer,)

    def post(self, request, *args, **kwargs):
        """ Entry point """

        return self.upload(request, *args, **kwargs)
