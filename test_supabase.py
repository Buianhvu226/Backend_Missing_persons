from supabase import create_client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Supabase client with environment variables
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_ANON_KEY')
supabase = create_client(supabase_url, supabase_key)

def test_upload_image():
    try:
        # Path to image file
        # C:\Finding lost member\Backend-Missing_persons\test_image.jpg
        image_path = "C:/Finding lost member/Backend-Missing_persons/OIP.jfif"
        
        # Upload file to 'faces' bucket
        with open(image_path, 'rb') as f:
            response = supabase.storage \
                .from_('images') \
                .upload(f"test/{os.path.basename(image_path)}", f)
        
        print("Upload successful!")
        
        # Get public URL of uploaded file
        public_url = supabase.storage \
            .from_('images') \
            .get_public_url(f"test/{os.path.basename(image_path)}")
        
        print(f"Public URL: {public_url}")
        
        return public_url
        
    except Exception as e:
        print(f"Upload failed: {str(e)}")
        return None

if __name__ == "__main__":
    test_upload_image()