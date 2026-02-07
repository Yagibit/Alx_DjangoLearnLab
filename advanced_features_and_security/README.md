# Permissions and Groups Setup

## Groups:
1. **Viewers**: Can view book instances. Assigned `can_view` permission.
2. **Editors**: Can create and edit books. Assigned `can_create` and `can_edit` permissions.
3. **Admins**: Full control. Assigned all permissions including `can_delete`.

## How to use:
Permissions are enforced in `views.py` using the `@permission_required` decorator. 
Example: `@permission_required('bookshelf.can_edit', raise_exception=True)`