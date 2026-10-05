import pandas as pd

from src.data_loader import load_csv


def main():
    users = load_csv('users.csv')
    current_day = pd.Timestamp("2026-10-05")
    pending_guests = find_stale_pending_guest_invitations(users, current_day)
    print(pending_guests)


def find_stale_pending_guest_invitations(user_dataframe, reference_date, maximum_age_days=30):
    pending_guests = user_dataframe[(user_dataframe["user_type"] == "Guest") & (
        user_dataframe["external_user_state"] == "PendingAcceptance")].copy()
    pending_guests['invited_at'] = pd.to_datetime(pending_guests['invited_at'])
    invited_date = pending_guests['invited_at']

    invitation_age_days = (reference_date - invited_date).dt.days
    invitation_limit_exceeded = invitation_age_days > maximum_age_days
    pending_guests.insert(6, "invitation_age_days", invitation_age_days)

    return pending_guests[invitation_limit_exceeded]


if __name__ == "__main__":
    main()
