from mixcloud_alarm.auth import run_flask, access_token
from mixcloud_alarm.client import get_latest_upload


def main():
    # Start the Flask server and OAuth process
    run_flask()

    # Access token should be set after the server shuts down
    if access_token:
        username = 'do_you_radio'
        mix_data = get_latest_upload(username, access_token)
        # play_audio(mix_url)
        print(mix_data)
    else:
        print("Failed to retrieve access token.")


if __name__ == '__main__':
    main()
