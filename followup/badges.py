from followup.models import Story

class CreateStoryAchievement():
    name = "First Story"
    key = 'first.story'
    description = "You've added your first story to be followed!"
    bonus = 10.0

    def evaluate(self, user, *args, **kwargs):
        if Story.objects.filter(user=user).count() > 0:
            print("Got it")
            return True
        else:
            print("No")
            return False
