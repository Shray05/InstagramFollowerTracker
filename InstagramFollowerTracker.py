import instaloader
import time  # To add delay


L = instaloader.Instaloader()

#creds
USERNAME = "username"
PASSWORD = "password"

try:
    #login
    L.login(USERNAME, PASSWORD)
except instaloader.TwoFactorAuthRequiredException:
    try:
        two_factor_code = input("Enter the two-factor authentication code: ")
        L.two_factor_login(two_factor_code)
        
        time.sleep(3) 
    except KeyboardInterrupt:
        print("\nTwo-factor authentication was interrupted. Please try again.")
        exit()

#load profile
profile = instaloader.Profile.from_username(L.context, USERNAME)

#list followers
followers = set([follower.username for follower in profile.get_followers()])

#list following
followings = set([following.username for following in profile.get_followees()])

#find diff
not_following_back = followings - followers

#print result
print("People who don't follow you back:")
for user in not_following_back:
    print(user)