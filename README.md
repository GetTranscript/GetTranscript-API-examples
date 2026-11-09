# ⚡️ YouTube Transcript API: GetTranscript code examples ⚡️

Code examples for the [GetTranscript API](https://gettranscript.app/documentation). Extract YouTube transcripts, subtitles and captions for single videos, playlists and channels from your own code.

## 🛠 What you can do

- Export transcripts as **TXT, Markdown, SRT, VTT, JSON or CSV**
- Get timestamped captions
- Extract transcripts for single videos, playlists and channels

## ❗️ Limits and credits

- **Rate limit:** 60 requests per minute per API key / IP
- **Credits:** 1 credit per successfully processed video

## 🗝️ Get an API key

Create a free API key in your [GetTranscript dashboard](https://gettranscript.app/api-keys). Credit packs are listed on the [pricing page](https://gettranscript.app/pricing).

The Python and Node.js examples load the key from a `.env` file (via `python-dotenv` / `dotenv`). Create a `.env` file in the example's folder and set your key there. The exact variable name is at the top of each example script.

## 🚀 Quick start

### Python

```bash
cd python
pip install requests python-dotenv
python fetch_transcript.py
```

### Node.js

```bash
cd nodejs
npm install axios dotenv
node fetch_transcript.js
```

### cURL

```bash
cd curl
bash request.sh
```

## 📚 Documentation

Endpoints, parameters and error responses are described in the official [API documentation](https://gettranscript.app/documentation).

## 🔗 Links

- [Free YouTube transcript extractor](https://gettranscript.app/): web interface for single videos, no sign-up
- [Bulk transcript extractor](https://gettranscript.app/bulk-transcript): web interface for playlists and channels, up to 100 videos per job
- [Pricing](https://gettranscript.app/pricing): pay-as-you-go credits, 1 video = 1 credit
