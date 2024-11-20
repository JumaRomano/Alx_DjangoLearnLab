# Permissions and Groups Setup

## Overview
This application demonstrates access control using Django's groups and permissions.

### Custom Permissions
- **can_view**: Allows viewing articles.
- **can_create**: Allows creating new articles.
- **can_edit**: Allows editing articles.
- **can_delete**: Allows deleting articles.

### Groups
- **Viewers**: Assigned `can_view`.
- **Editors**: Assigned `can_view`, `can_create`, `can_edit`.
- **Admins**: Assigned all permissions.

### Usage
1. Assign users to groups via the Django admin site or programmatically.
2. Permissions are enforced in views using `@permission_required`.

### Testing
- Log in as different users and verify access to views based on their group membership.
