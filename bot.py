import praw
import datetime


def hosting_post(sub, today):
    title = "Weekly What Are You Hosting Megathread - " + today
    post = sub.submit(
        title,
        selftext='''#Weekly What Are You Hosting Megathread
        
##Questions involving what to host belong here.

In the past, there have been a number of posts asking for what to host. For starters, please make sure to check out the [Awesome Self-Hosted](https://github.com/Kickball/awesome-selfhosted) list of Apps to Host on Github
        
With that said, Feel free to chime in with your preferred must-have apps, your first-installs, your ideal setups, and more!
        
 Please refrain from posting similar this type of submission outside of this weekly thread.''',
        send_replies=False,
    )
    post.mod.distinguish()
    post.mod.sticky(bottom=True)
    post.mod.flair(text="Weekly Megathread", css_class="megathread")
    return post.id


def dashboard_post(sub, today):
    title = "Weekly Dashboard Showoff Megathread - " + today
    post = sub.submit(
        title,
        selftext='''#Weekly Dashboard Showoff Megathread

##Wanna show off your sweet dashboard? Do it here. 

In the past, there have been a number of posts showing off their dashboards for their self-hosted environments. We love to see this! But they were beginning to clog up the sub. 

With that said, Feel free to show us your awesome dashboards, share your progress, etc!

 Please refrain from posting this type of submission outside of this weekly thread.''',
        send_replies=False,
    )
    post.mod.distinguish()
    post.mod.sticky(bottom=True)
    post.mod.flair(text="Weekly Megathread", css_class="megathread")
    return post.id


def main():
    date = datetime.datetime.now()
    weekday = datetime.datetime.today().weekday()
    today = date.strftime("%B %d, %Y")
    sub = praw.Reddit('shwiki').subreddit('selfhosted')
    if weekday == 0:
        hosting_post(sub, today)
    elif weekday == 4:
        dashboard_post(sub, today)


if __name__ == '__main__':
    main()
