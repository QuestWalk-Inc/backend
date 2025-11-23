from services import supabase_client
from services.users.user_service import SupabaseUserService

service = SupabaseUserService(supabase_client)