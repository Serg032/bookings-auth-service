import os
from dotenv import load_dotenv
from supabase import create_client


def before_scenario(context, scenario):
    # Load envs so we can read SUPABASE_URL/KEY and USERS_TABLENAME
    load_dotenv()

    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    users_tablename = os.getenv("TEST_USERS_TABLENAME", "users")

    if not supabase_url or not supabase_key:
        # If not configured, skip cleanup to avoid affecting wrong environment
        return

    client = create_client(supabase_url, supabase_key)

    # Clean table before each scenario (test DB only!)
    # Supabase requires a filter on delete; use a condition that matches all rows
    client.table(users_tablename).delete().neq("id", "").execute()

    if "seed_user" in scenario.tags:
        client.table(users_tablename).insert(
            {"id": "test_id", "username": "John"}
        ).execute()
