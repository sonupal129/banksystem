from .imports import *

# CODE BELOW

class GroupRequiredMixins(object):
    group_required = None  # Group Name Only

    def get_required_group(self):
        if self.group_required == None:
            raise AttributeError ("Attribute group_required not found, Please add group_required attribute")
        elif not isinstance(self.group_required, (tuple, list)):
            raise TypeError ("Attribute group_required should be in tuple or list")
        return self.group_required


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        else:
            group_required = set(self.get_required_group())
            user_group = request.user.groups.values_list("name", flat=True)
            group_found = [group for group in group_required if group in user_group]
            if set(group_required) == set(group_found) or request.user.is_superuser:
                return super(GroupRequiredMixins, self).dispatch(request, *args, **kwargs)
        return HttpResponseForbidden("Not allowed to view page, please contact administrator")


class BasePermissionMixin(LoginRequiredMixin):
    permission_denied_message = "You are not authenticated to view this page"