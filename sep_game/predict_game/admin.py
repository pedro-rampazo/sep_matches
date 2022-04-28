from django.contrib import admin
from predict_game.models import Member, Match, Hunch

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ('score', 'victory')

admin.site.register(Member, MemberAdmin)

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass

@admin.register(Hunch)
class HunchAdmin(admin.ModelAdmin):
    readonly_fields = ('point',)
