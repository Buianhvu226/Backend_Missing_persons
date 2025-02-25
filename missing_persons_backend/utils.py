from supabase import create_client
from django.conf import settings
import os


SUPABASE_URL = 'https://clxxtikxcdjbosddoooa.supabase.co'
SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNseHh0aWt4Y2RqYm9zZGRvb29hIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAzNzAzMDIsImV4cCI6MjA1NTk0NjMwMn0.Wv3m5cAUPLNd_1BYH6uAGtdZY1sNn2f9EP-h5FuTEU8'

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_ANON_KEY
)

def upload_face_image(file_path, file_name):
    """
    Upload a face image to Supabase storage
    """
    try:
        with open(file_path, 'rb') as f:
            response = supabase.storage.from_('faces').upload(
                file_name,
                f
            )
        # Get public URL
        public_url = supabase.storage.from_('faces').get_public_url(file_name)
        return public_url
    except Exception as e:
        print(f"Error uploading to Supabase: {str(e)}")
        return None