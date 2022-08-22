from panther_config import detection
import match_filters




def aws_admin_role_assumed(*roles):
    filters = [
        match_filters.deep_equal("event_type", "RoleAssumed")
    ]

    for r in roles:
        filters = match_filters.deep_equal("iam.role.name",)

    return detection.Rule(
        filters=filters,
    )