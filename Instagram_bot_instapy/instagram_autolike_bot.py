from instapy import InstaPy

session = InstaPy(username="<>", password="<>", headless_browser=True, want_check_browser=False)
session.login()
session.like_by_tags(["<>", "<>"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
session.set_relationship_bounds(enabled=True, max_followers=8500)
session.end()