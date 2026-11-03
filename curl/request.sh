#!/bin/bash

API_KEY=${GETTRANSCRIPT_API_KEY:-"YOUR_API_KEY_HERE"}
VIDEO_ID="dQw4w9WgXcQ"

echo "Fetching transcript for video: $VIDEO_ID..."

curl -X GET "https://gettranscript.app/api/transcript?videoId=${VIDEO_ID}&format=json" \
     -H "x-api-key: ${API_KEY}" \
     -H "Content-Type: application/json"
