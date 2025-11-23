from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_API')

supabase_client = create_client(supabase_url, supabase_key)