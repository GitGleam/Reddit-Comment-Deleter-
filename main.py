import praw


# Reddit API credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'UYOUR_CLIENT_SECRET'
username = 'YOUR_REDDIT_USERNAME'
password = 'YOUR_REDDIT_PASSWORD'
user_agent = 'YOUR_USER_AGENT_NAME'

# Initialize Reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

# Function to delete all comments
def delete_all_comments():
    # Iterate over comments
    for comment in reddit.user.me().comments.new(limit=None):
        try:
            comment.delete()
            print("Comment deleted:", comment.id)
        except Exception as e:
            print("Error deleting comment", comment.id, ":", e)

# Call the function to delete all comments
delete_all_comments()