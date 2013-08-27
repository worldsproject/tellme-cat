from django.contrib.syndication.views import Feed

class FollowUps(Feed):
    title = "Latest Follow Ups"
    link = "/followups"
    description = "An up-to-date list of Follow Ups to the stories you're interested in."
    
    def items(self):
        return self.request.story_set.all().followup_set.all()[0:10]

    def item_title(self, item):
        return "Follow up to the story: " + item.story.title

    def item_description(self, item):
        return "<a href='" + item.link + "'>" + item.title + "</a>"

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return 'http://www.tellme.cat/list'