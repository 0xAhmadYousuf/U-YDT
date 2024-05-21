# Help Guide for U-YDT

This guide provides detailed instructions on how to obtain necessary IDs and keys to use the U-YDT tool effectively.

## Table of Contents

1. [How to Get a YouTube Channel ID](#how-to-get-a-youtube-channel-id)
2. [How to Get a YouTube Playlist ID/Link](#how-to-get-a-youtube-playlist-idlink)
3. [How to Get a YouTube Developer API Key](#how-to-get-a-youtube-developer-api-key)

## How to Get a YouTube Channel ID

To download all videos from a YouTube channel, you need the channel's ID. Follow these steps to find it:

1. **Visit the YouTube Channel**:
   - Go to the YouTube channel in your web browser.

2. **Check the URL**:
   - The URL of the channel typically looks like this:
     ```
     https://www.youtube.com/channel/UCxxxxxxxxxxxx
     ```
   - The part after `/channel/` is the Channel ID (e.g., `UCxxxxxxxxxxxx`).

3. **Alternative Method**:
   - If the URL is not in the standard format (e.g., custom URLs), right-click on the channel's page and select "View page source."
   - Search for the term `"channelId"` in the page source. The Channel ID will be in the format:
     ```html
     "channelId":"UCxxxxxxxxxxxx"
     ```

## How to Get a YouTube Playlist ID/Link

To download all videos from a YouTube playlist, you need the playlist's ID or link. Here’s how to find it:

1. **Visit the YouTube Playlist**:
   - Go to the playlist in your web browser.

2. **Check the URL**:
   - The URL of the playlist typically looks like this:
     ```
     https://www.youtube.com/playlist?list=PLxxxxxxxxxxxx
     ```
   - The part after `list=` is the Playlist ID (e.g., `PLxxxxxxxxxxxx`).

3. **Copy the URL**:
   - You can use the entire URL directly when prompted by U-YDT, or just the Playlist ID.

## How to Get a YouTube Developer API Key

To use U-YDT, you need a YouTube Developer API key. Follow these steps to obtain one:

1. **Go to the Google Cloud Console**:
   - Visit the [Google Cloud Console](https://console.cloud.google.com/).

2. **Create a New Project**:
   - Click on the project dropdown at the top and select "New Project."
   - Give your project a name and click "Create."

3. **Enable YouTube Data API v3**:
   - In the Google Cloud Console, go to "APIs & Services" -> "Library."
   - Search for "YouTube Data API v3" and click on it.
   - Click "Enable" to enable the API for your project.

4. **Create API Credentials**:
   - Go to "APIs & Services" -> "Credentials."
   - Click on "Create Credentials" and select "API key."
   - Your API key will be created and displayed. Copy this key for use in U-YDT.

5. **Restrict Your API Key (Optional but recommended)**:
   - To prevent unauthorized use, click on "Edit API key" and set restrictions based on your needs.

By following these instructions, you will have all the necessary IDs and API keys to effectively use U-YDT for downloading YouTube content.

For more details on using the tool, refer to the [README.md](README.md) and the [FlowChart.md](FlowChart.md) documents.
