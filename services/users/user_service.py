from typing import Protocol

from supabase import Client


class UserService(Protocol):
    def create_user(self, telegram_id: int, username: str):
        ...

    def get_user(self, telegram_id: int) -> list:
        ...

class SupabaseUserService(UserService):
    def __init__(self, supabase_client: Client):
        self.supabase_client = supabase_client

    def create_user(self, telegram_id: int, username: str):
        self.supabase_client.table("users").insert({"telegram_id": telegram_id, "username": username}).execute()

    def get_user(self, telegram_id: int) -> list:
        response = (
            self.supabase_client
                .table("users")
                .select("*")
                .eq("telegram_id", telegram_id)
                .execute()
        )
        return response.data


class MockUserService(UserService):
    def __init__(self):
        self.users: list[dict] = []

    def create_user(self, telegram_id: int, username: str):
        self.users.append({"telegram_id": telegram_id, "username": username})

    def get_user(self, telegram_id: int) -> list:
        filtered_users = list(filter(lambda user: user["telegram_id"] == telegram_id, self.users))
        return filtered_users
