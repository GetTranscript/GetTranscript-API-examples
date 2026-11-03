import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GETTRANSCRIPT_API_KEY")
BASE_URL = "https://gettranscript.app/api/transcript"

def get_transcript(video_id: str):
    if not API_KEY:
        print("Error: GETTRANSCRIPT_API_KEY is not set in .env file.")
        return

    params = {"videoId": video_id, "format": "json"}
    headers = {"x-api-key": API_KEY}

    print(f"Fetching transcript for video: {video_id}...")
    
    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get("success"):
            transcript_segments = data.get("transcript", [])
            print(f"✅ Success! Found {len(transcript_segments)} segments.")
            for segment in transcript_segments[:3]:
                print(f"[{segment['start']}s] {segment['text']}")
        else:
            print(f"❌ API Error: {data.get('error', 'Unknown error')}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ HTTP Request failed: {e}")

if __name__ == "__main__":
    TEST_VIDEO_ID = "dQw4w9WgXcQ" 
    get_transcript(TEST_VIDEO_ID)
