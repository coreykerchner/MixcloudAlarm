from mixcloud_alarm import auth, mixcloud_client
from pprint import pprint


def main():
    # print("Visit this URL to authorize the application:")
    # print(auth.get_authorization_url())
    # auth_code = input("Enter the authorization code: ")
    # access_token = auth.get_access_token(auth_code)


    print('Access token:', access_token)

    username = 'do_you_radio'
    mix_data = mixcloud_client.get_latest_upload(username, access_token)
    pprint(mix_data)


if __name__ == '__main__':
    main()
