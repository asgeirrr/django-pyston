from __future__ import unicode_literals

from pyston.resource import BaseModelResource, BaseResource

from .models import Issue, User


class IssueResource(BaseModelResource):
    model = Issue
    default_detailed_fields = ('id', 'created_at', '_obj_name', 'name', ('created_by', ('contract',)), 'solver',
                               'leader', 'watched_by')
    default_general_fields = ('id', '_obj_name', 'name', 'created_by', 'watched_by')


class UserResource(BaseModelResource):
    model = User


class ExtraResource(BaseResource):

    def get(self):
        return {'extra': 1}
