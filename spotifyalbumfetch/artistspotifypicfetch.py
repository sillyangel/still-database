import requests
import json
import re

token = 'BQAcX7bZr8qfz8vPZmzfd1E49Vl40YEt5IwxyxG5vMtJlsWPTdatq1aaMhIF-sGKn7fGKLaAAui9zHj_lxGZgsXp9B9HDvYLqu3M5h049EWgqfyBoIsOgQvzr6G7SGc1oz3norKCAwY6kvnzVrkK1EymEJ3E9358FzZA2ItFJs95rED1dUoo0jMEd6Yn9vxPSme0Ba37qsTiqGsWGoRhQFOTaFWFREacl3-4yoSdjKQbjzcD_GqiFCtZqFRxWBK-_GpSIe0a84Gn';

# Set headers with authorization token
headers = {
    "Authorization": f"Bearer {token}"
}

# Function to fetch and save artist picture
def fetch_and_save_artist_picture(artist_id):
    # Base URL for artist details
    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"

    # Get artist details
    artist_response = requests.get(artist_url, headers=headers)
    if artist_response.status_code == 200:
        artist_data = json.loads(artist_response.text)
        artist_name = artist_data["name"]
        artist_picture_url = artist_data["images"][0]["url"] if artist_data["images"] else None

        if artist_picture_url:
            # Remove special characters and spaces from artist name for filename
            filename = re.sub(r'\W+', '', artist_name).lower() + ".jpg"

            # Fetch the artist picture
            picture_response = requests.get(artist_picture_url)
            if picture_response.status_code == 200:
                # Save the picture to a file
                with open(filename, "wb") as outfile:
                    outfile.write(picture_response.content)
                print(f"Artist picture saved to {filename}")
            else:
                print(f"Error fetching artist picture: {picture_response.status_code}")
        else:
            print(f"No picture found for artist: {artist_name}")
    else:
        print(f"Error fetching artist details: {artist_response.status_code}")

# Prompt user for artist IDs
artist_ids = input("Enter artist IDs separated by commas: ").split(',')

# Fetch and save picture for each artist
for artist_id in artist_ids:
    fetch_and_save_artist_picture(artist_id.strip())