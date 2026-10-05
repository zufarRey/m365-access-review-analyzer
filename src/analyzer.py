import pandas as pd

from src.data_loader import load_csv


def main():
    users = load_csv('users.csv')
    reference_date = pd.Timestamp("2026-10-05")
    pending_guests = find_stale_pending_guest_invitations(
        users, reference_date)
    print(pending_guests)

    resources = load_csv('resources.csv')
    undocumented_broken_inheritance = find_undocumented_broken_inheritance(
        resources)
    print(undocumented_broken_inheritance)

    permissions = load_csv('permissions.csv')
    disabled_users_with_permissions = find_disabled_users_with_permissions(
        users, permissions, resources)
    print(disabled_users_with_permissions)


def find_stale_pending_guest_invitations(user_dataframe, reference_date, maximum_age_days=30):
    pending_guests = user_dataframe[(user_dataframe["user_type"] == "Guest") & (
        user_dataframe["external_user_state"] == "PendingAcceptance")].copy()
    pending_guests['invited_at'] = pd.to_datetime(pending_guests['invited_at'])
    invited_dates = pending_guests['invited_at']

    invitation_age_days = (reference_date - invited_dates).dt.days
    invitation_limit_exceeded = invitation_age_days > maximum_age_days
    pending_guests.insert(6, "invitation_age_days", invitation_age_days)

    return pending_guests[invitation_limit_exceeded]


def find_undocumented_broken_inheritance(resources_dataframe):
    has_missing_reason = resources_dataframe['inheritance_reason'].isna()
    has_broken_inheritance = resources_dataframe['inheritance_broken']
    undocumented_broken_inheritance = resources_dataframe[
        has_broken_inheritance & has_missing_reason].copy()
    return undocumented_broken_inheritance


def find_disabled_users_with_permissions(user_dataframe, permission_dataframe, resources_dataframe):
    is_inactive_account = user_dataframe['account_enabled'] == False
    inactive_accounts = user_dataframe[is_inactive_account].copy()

    permissions = permission_dataframe[(permission_dataframe['principal_type'] == "User")
                                       & (permission_dataframe["assignment_type"] == "Direct")].copy()

    permissions_of_inactive_accounts = inactive_accounts.merge(
        permissions, left_on="user_id", right_on="principal_id", how="inner")

    permissions_of_inactive_accounts = permissions_of_inactive_accounts.merge(
        resources_dataframe, on="resource_id", how="left")
    relevant_columns = [
        "user_id",
        "display_name",
        "account_enabled",
        "permission_id",
        "resource_id",
        "resource_name",
        "resource_type",
        "sensitivity",
        "role",
        "assignment_type",
        "granted_at",
        "owner_user_id",
    ]
    return permissions_of_inactive_accounts[relevant_columns]


if __name__ == "__main__":
    main()
