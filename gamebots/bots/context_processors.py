from .models import Bot


def bots(request):
    """Make `bots` global"""
    qs = Bot.objects.all()
    return {"bots_qs": qs}
