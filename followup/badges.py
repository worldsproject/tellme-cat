from followup.models import Story
from followup.models import FollowUp

class CreateStoryAchievement():
    name = "First Story"
    key = 'first.story'
    description = "You've added your first story to be followed!"
    bonus = 10.0

    def evaluate(self, user, *args, **kwargs):
        if Story.objects.filter(user=user).count() > 0:
            return True
        else:
            return False

class TenStoryAchievement():
    name = 'Tenth Story'
    key = 'tenth.story'
    description = "You've created your tenth story to be followed up on."
    bonus = 100

    def evaluate(self, user, *args, **kwargs):
        if Story.objects.filter(user=user).count() >= 10:
            return True
        else:
            return False

class FiftyStoryAchievement():
    name = 'Fiftieth Story'
    key = 'fiftieth.story'
    description = "You've created your fiftieth story to be followed up on."
    bonus = 500

    def evaluate(self, user, *args, **kwargs):
        if Story.objects.filter(user=user).count() >= 50:
            return True
        else:
            return False

class HundredStoryAchievement():
    name = 'Hundredth Story'
    key = 'hundredth.story'
    description = "You've created your hundredth story to be followed up on."
    bonus = 1000

    def evaluate(self, user, *args, **kwargs):
        if Story.objects.filter(user=user).count() >= 100:
            return True
        else:
            return False

class FiveHundredStoryAchievement():
    name = 'Five Hundredth Story'
    key = 'five.hundredth.story'
    description = "You've created your five hundredth story to be followed up on."
    bonus = 5000

    def evaluate(self, user, *args, **kwargs):
        if Story.objects.filter(user=user).count() >= 500:
            return True
        else:
            return False

class FollowUpAchievement():
    name = 'Follow Up'
    key = 'follow.up'
    description = "You've created your first Follow Up!"
    bonus = 10

    def evaluate(self, user, *args, **kwargs):
        if FollowUp.objects.filter(user=user).count() > 0:
            return True
        else:
            return False

class TenFollowUpAchievement():
    name = 'Tenth Follow Up'
    key = 'tenth.follow.up'
    description = "You've created your tenth Follow Up!"
    bonus = 100

    def evaluate(self, user, *args, **kwargs):
        if FollowUp.objects.filter(user=user).count() > 9:
            return True
        else:
            return False

class FiftyFollowUpAchievement():
    name = 'Fiftieth Follow Up'
    key = 'fiftieth.follow.up'
    description = "You've created your fiftieth Follow Up!"
    bonus = 500

    def evaluate(self, user, *args, **kwargs):
        if FollowUp.objects.filter(user=user).count() > 49:
            return True
        else:
            return False

class HundredFollowUpAchievement():
    name = 'Hundredth Follow Up'
    key = 'hundredth.follow.up'
    description = "You've created your hundredth Follow Up!"
    bonus = 1000

    def evaluate(self, user, *args, **kwargs):
        if FollowUp.objects.filter(user=user).count() > 99:
            return True
        else:
            return False

class FiveHundredFollowUpAchievement():
    name = 'Five Hundredth Follow Up'
    key = 'five.hundredth.follow.up'
    description = "You've created your five hundredth Follow Up!"
    bonus = 5000

    def evaluate(self, user, *args, **kwargs):
        if FollowUp.objects.filter(user=user).count() > 499:
            return True
        else:
            return False
