# Render deployment overlay

Use these files with the upstream MusicPlayer source tree.

## Render
1. Put these files into the root of the MusicPlayer repository.
2. Commit and push.
3. In Render choose **New > Blueprint** and select the repository.
4. Enter the secret environment variables requested by `render.yaml`.
5. Deploy.

The service is configured as a **Background Worker** using Docker. The container installs FFmpeg and starts `python main.py` directly.

## Required variables
- API_ID
- API_HASH
- SESSION

## Optional
- BOT_TOKEN
- SUDOERS
- SPOTIFY_CLIENT_ID
- SPOTIFY_CLIENT_SECRET
- PREFIX
- LANGUAGE
- QUALITY
- STREAM_MODE
- ADMINS_ONLY

Do not commit real Telegram credentials or String Sessions.
