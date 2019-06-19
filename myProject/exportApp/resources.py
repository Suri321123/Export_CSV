from import_export import resources
from .models import User,Member

class UserResource(resources.ModelResource):
    class Meta:
        model = User


class MemberResource(resources.ModelResource):
    class Meta:
        model = Member