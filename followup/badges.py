from followup.models import Story

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
        if Story.objects.filter(user=user).count >= 10:
            return True
        else:
            return False

class FiftyStoryAchievement():
    name = 'Fiftieth Story'
    key = 'fiftieth.story'
    description = "You've created your fiftieth story to be followed up on."
    bonus = 500

    def evaluate(self, user, *args, **kwargs):
        if Story.objects.filter(user=user).count >= 50:
            return True
        else:
            return False
class HundredStoryAchievement():
    name = 'Hundredth Story'
    key = 'hundredth.story'
    description = "You've created your hundredth story to be followed up on."
    bonus = 1000

    def evaluate(self, user, *args, **kwargs):
        if Story.objects.filter(user=user).count >= 100:
            return True
        else:
            return False

class FiveHundredStoryAchievement():
    name = 'Five Hundredth Story'
    key = 'five.hundredth.story'
    description = "You've created your five hundredth story to be followed up on."
    bonus = 5000

    def evaluate(self, user, *args, **kwargs):
        if Story.objects.filter(user=user).count >= 500:
            return True
        else:
            return False

class FollowUpAchievement():
    name = 'Follow Up'
    key = 'follow.up'
    description = "You've created your first Follow Up!"

    def evaluate(self, user, *args, **kwargs):
        if FollowUp.objects.filter(user=user) > 0:
            return True
        else:
            return False

class TenFollowUpAchievement():
    name = 'Ten Follow Ups'
    key = 'ten.follow.up'
    description = "You've created your tenth Follow Up!"

    def evaluate(self, user, *args, **kwargs):
        if FollowUp.objects.filter(user=user) > 9:
            return True
        else:
            return False

class FiftyFollowUpAchievement():
    name = 'Fifteith Follow Up'
    key = 'fifteith.follow.up'
    description = "You've created your fifteith Follow Up!"

    def evaluate(self, user, *args, **kwargs):
        if FollowUp.objects.filter(user=user) > 49:
            return True
        else:
            return False

class HundrethFollowUpAchievement():
    name = 'Hundredeth Follow Up'
    key = 'hundredeth.follow.up'
    description = "You've created your hundredth Follow Up!"

    def evaluate(self, user, *args, **kwargs):
        if FollowUp.objects.filter(user=user) > 99:
            return True
        else:
            return False

class FiveHundredthFollowUpAchievement():
    name = 'Five Hundredth Follow Up'
    key = 'five.hundredth.follow.up'
    description = "You've created your Five Hundredth Follow Up!"

    def evaluate(self, user, *args, **kwargs):
        if FollowUp.objects.filter(user=user) > 499:
            return True
        else:
            return False

class PsyopAchievement():
    name = 'Psycog'
    key = 'psycog'
    description = "You're helping people find items in the future."

    def evaluate(self, user, *args, **kwargs):
        if found:
            return True
        else:
            return False

class Psyconaut():
    name = 'Psyconaut'
    key = 'psyconaut'
    description = "You knew a story needed a follow up, before they did."

    def evaluate(self, user, *args, **kwargs):
        if found:
            return True
        else:
            return False
