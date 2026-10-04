from pathlib import Path

import pandas as pd


def main():
    users_filename = "users.csv"
    resources_filename = "resources.csv"
    permissions_filename = "permissions.csv"

    users = load_csv(users_filename)

    resources = load_csv(resources_filename)
    permissions = load_csv(permissions_filename)

    required_user_columns = set(["user_id", "display_name", "user_type",
                                 "account_enabled", "external_user_state", "invited_at", "department"])

    required_resource_columns = set(["resource_id", "resource_name", "resource_type", "parent_resource_id",
                                     "sensitivity", "owner_user_id",  "inheritance_broken", "inheritance_reason", "external_access_allowed"])

    required_permission_columns = set(["permission_id", "resource_id", "principal_id",
                                       "principal_name", "principal_type", "role", "assignment_type", "granted_at"])

    validate_columns(users, required_user_columns, users_filename)
    validate_columns(resources, required_resource_columns, resources_filename)
    validate_columns(permissions, required_permission_columns,
                     permissions_filename)

    print(users.head())
    print(resources.head())
    print(permissions.head())


# Dynamische Pfaderstellung
def load_csv(filename):
    project_root = Path(__file__).resolve().parent.parent

    absolute_path = project_root / "data" / filename
    if absolute_path.is_file():
        df = pd.read_csv(absolute_path)
        return df
    else:
        raise FileNotFoundError(
            f"Die Datei wurde nicht gefunden: {absolute_path}")


def validate_columns(dataframe, required_columns, filename):
    existing_columns = set(dataframe.columns)
    # Wert >0 oder nicht leer sind ,sind True
    missing_columns = required_columns - existing_columns
    if missing_columns:
        raise ValueError(f"Spalten {missing_columns} fehlen in {filename}")


if __name__ == "__main__":
    main()
