require('dotenv').config();
const axios = require('axios');

const API_KEY = process.env.GETTRANSCRIPT_API_KEY;
const BASE_URL = "https://gettranscript.app/api/transcript";

async function getTranscript(videoId) {
    if (!API_KEY) {
        console.error("Error: GETTRANSCRIPT_API_KEY is not set in .env file.");
        return;
    }

    console.log(`Fetching transcript for video: ${videoId}...`);

    try {
        const response = await axios.get(BASE_URL, {
            headers: { 'x-api-key': API_KEY },
            params: { videoId: videoId, format: 'txt' }
        });

        const data = response.data;

        if (data.success) {
            console.log("✅ Success! Transcript preview:");
            console.log(data.text.substring(0, 200) + "...");
        } else {
            console.error(`❌ API Error: ${data.error || 'Unknown error'}`);
        }
    } catch (error) {
        if (error.response) {
            console.error(`❌ HTTP Error ${error.response.status}:`, error.response.data);
        } else {
            console.error(`❌ Request failed:`, error.message);
        }
    }
}

const TEST_VIDEO_ID = "dQw4w9WgXcQ";
getTranscript(TEST_VIDEO_ID);
