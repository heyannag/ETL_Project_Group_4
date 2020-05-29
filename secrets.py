client_id = "a753d56129f44f3fb9f17e0061f38eba"
# Client Secret = 70e3adb4ad4e45d4a27c65a576d2d411
# scopes = playlist-read-private
# redirect_uri = https%3A%2F%2Fgoogle.com

spotify_token = "BQCvZY6eIwAQVhNqL65ROnPZal0BvmzvlavwsMi2z98ZtUk_xyCMBqRv8bmJxNAysALSrBM7dDQVe1c736Bu4t6I0NNSC3hNsD6vm81OqzM_wxoJ3_I4fCKgHvQyVMd8KpZYp0feJnFMs8O1bGu51uTPMkQZSvZppNFA8NpNSsZ5nzYvdjCK6YyBdXNv"
spotify_user_id = "m.annagivens"

youtube_api = "AIzaSyDrkTN5CVV8NUIdCilSgVShzf-jGvhjz-A"

# curl -X "POST" "https://api.spotify.com/v1/users/m.annagivens/playlists" --data "{\"name\":\"New Playlist\",\"description\":\"New playlist description\",\"public\":false}" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQCvZY6eIwAQVhNqL65ROnPZal0BvmzvlavwsMi2z98ZtUk_xyCMBqRv8bmJxNAysALSrBM7dDQVe1c736Bu4t6I0NNSC3hNsD6vm81OqzM_wxoJ3_I4fCKgHvQyVMd8KpZYp0feJnFMs8O1bGu51uTPMkQZSvZppNFA8NpNSsZ5nzYvdjCK6YyBdXNv"

# google-auth-oauthlib==0.4.1
# google-api-python-client==1.7.11
# youtube_dl==2020.1.24
# requests==2.22.0

# $.ajax({
#    url: 'https://api.spotify.com/v1/me',
#    headers: {
#        'Authorization': 'Bearer ' + accessToken
#    },
#    success: function(response) {
#        ...
#    }

# https://www.google.com/?code=AQDscVS9sv5-DBQ-Zh3fdXY7YM8zkaIDYEnxoNrg6OG_cp2FoV8B4qpG66YfNIrcqWvmD3ZvjhI38I6bDAs-smE_UWN7WSL3QRiKFDkOKgsxT5O-LbE-TQsM3hWKxMSxliJ5hxXVYgixq3VgA_Z_3_Pa0kNpq_ImIBkeRbd1f-78UflW6XnXYA

# curl -H "Authorization: Basic a753d56129f44f3fb9f17e0061f38eba:70e3adb4ad4e45d4a27c65a576d2d411" -d grant_type=authorization_code -d code=AQDscVS9sv5-DBQ-Zh3fdXY7YM8zkaIDYEnxoNrg6OG_cp2FoV8B4qpG66YfNIrcqWvmD3ZvjhI38I6bDAs-smE_UWN7WSL3QRiKFDkOKgsxT5O-LbE-TQsM3hWKxMSxliJ5hxXVYgixq3VgA_Z_3_Pa0kNpq_ImIBkeRbd1f-78UflW6XnXYA
# -d redirect_uri=https%3A%2F%2Fgoogle.com https://accounts.spotify.com/api/token

