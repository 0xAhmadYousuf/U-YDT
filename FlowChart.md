## Simple WorkFlow
```
Main Function
├── Load Log
│   ├── Check if log file exists
│   └── If exists, load log from file
│       └── If not, return empty log
├── Save Log
│   ├── Check if directory exists for log file
│   │   └── If not, create directory
│   └── Save log to file
└── User Options
    ├── Display options: Channel, Playlist, Single Content, Check Previous
    └── Handle User Choice
        ├── Channel Download
        │   ├── Check if API keys exist in log
        │   │   ├── If yes, display API keys and prompt user to choose or enter new API key
        │   │   └── If no, prompt user to enter new API key
        │   ├── Update log with chosen or new API key
        │   ├── Prompt user for Channel ID
        │   │   ├── If channel exists in log, display and confirm or update channel name
        │   │   └── If not, prompt for channel name and update log
        │   └── Call `download_channel(api_key, channel_id, channel_name)`
        ├── Playlist Download
        │   ├── Prompt user for Playlist URL or ID
        │   ├── Normalize URL/ID
        │   ├── Check if normalized URL exists in log
        │   │   ├── If yes, display and confirm or update playlist name
        │   │   └── If not, fetch playlist title and update log
        │   └── Call `download_playlist_videos(normalized_url)`
        ├── Single Content Download
        │   ├── Prompt user for Content URL or ID
        │   ├── Normalize URL/ID
        │   ├── Check if normalized URL exists in log
        │   │   ├── If yes, display and confirm or update video name
        │   │   └── If not, fetch video title and update log
        │   └── Call `download_single_video(normalized_url)`
        ├── Check Previous Downloads
        │   ├── Prompt user for type of previous downloads (Videos, Playlists, Channels, All)
        │   ├── Display list of previous downloads based on choice
        │   ├── Prompt user to choose a download
        │   ├── Handle Download Choice
        │   │   ├── If Playlist, call `download_playlist_videos(previously_stored_url)`
        │   │   ├── If Channel
        │   │   │   ├── Prompt for API key (existing or new)
        │   │   │   └── Call `download_channel(api_key, previously_stored_channel_id, previously_stored_channel_name)`
        │   │   └── If Single Content, call `download_single_video(previously_stored_url)`
        └── Return to main menu or exit based on user input
```

## Detailed Steps for Each Function

### Overview
The tool allows users to download content from YouTube, including channels, playlists, and single videos. It also maintains a log of previous downloads and supports re-downloading these items. The log stores API keys, channel IDs, playlist URLs, and video URLs, along with their associated names or titles.

### Detailed Workflow

1. **Initialization and Log Handling**
   - **Load Log**:
     - The tool first checks if a log file exists. If it does, the log data is loaded from the file. If not, an empty log is initialized.
   - **Save Log**:
     - Before saving the log data, the tool checks if the directory for the log file exists. If it does not, the directory is created. The log data is then saved to the file.

2. **Main Function Execution**
   - **User Interface**:
     - The tool presents the user with four main options: download a channel, download a playlist, download a single video, or check previous downloads.

3. **Channel Download Workflow**
   - **API Key Handling**:
     - The tool checks if API keys are stored in the log. If they are, it displays the available API keys and prompts the user to choose one or enter a new API key. If no API keys are stored, the user is prompted to enter a new API key, which is then added to the log.
   - **Channel ID and Name Handling**:
     - The user is prompted to enter a Channel ID. If the channel is already in the log, the stored channel name is displayed, and the user can confirm or enter a new name. If the channel is not in the log, the user is prompted to enter a channel name, which is then added to the log.
   - **Download Channel**:
     - The function `download_channel(api_key, channel_id, channel_name)` is called to start the download process for the specified channel.

4. **Playlist Download Workflow**
   - **Playlist URL/ID Handling**:
     - The user is prompted to enter a Playlist URL or ID, which is then normalized using the function `normalize_playlist_url()`.
   - **Playlist Name Handling**:
     - If the normalized URL is already in the log, the stored playlist name is displayed, and the user can confirm or enter a new name. If the normalized URL is not in the log, the tool fetches the playlist title using `fetch_playlist_title(normalized_url)` and updates the log.
   - **Download Playlist**:
     - The function `download_playlist_videos(normalized_url)` is called to start the download process for the specified playlist.

5. **Single Content Download Workflow**
   - **Content URL/ID Handling**:
     - The user is prompted to enter a Single Content URL or ID, which is then normalized using the function `normalize_video_url()`.
   - **Content Name Handling**:
     - If the normalized URL is already in the log, the stored video name is displayed, and the user can confirm or enter a new name. If the normalized URL is not in the log, the tool fetches the video title using `fetch_video_title(normalized_url)` and updates the log.
   - **Download Single Content**:
     - The function `download_single_video(normalized_url)` is called to start the download process for the specified video.

6. **Check Previous Downloads**
   - **Type Selection**:
     - The user is prompted to choose the type of previous downloads to check: Videos, Playlists, Channels, or All.
   - **Display Previous Downloads**:
     - Based on the user's choice, the tool displays the list of previous downloads for the selected type.
   - **Download Selection**:
     - The user is prompted to choose an item from the list to re-download.
     - For playlists, the function `download_playlist_videos(previously_stored_url)` is called.
     - For channels, the user is prompted to select an API key (existing or new) and then the function `download_channel(api_key, previously_stored_channel_id, previously_stored_channel_name)` is called.
     - For single content, the function `download_single_video(previously_stored_url)` is called.

7. **Loop or Exit**
   - After completing a task, the tool prompts the user if they want to perform another task. If the user chooses to continue, the tool loops back to the main menu. If the user chooses to exit, the program terminates.

### Error Handling
- The tool includes error handling to catch and display any exceptions that occur during execution. It also handles keyboard interruptions gracefully, allowing the user to exit the program by pressing Enter.

By following these steps, the tool provides a comprehensive solution for downloading YouTube content and managing download history, ensuring that users have a smooth and efficient experience.
