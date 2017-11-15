from django.contrib import admin
from .models import Film, Genre

class FilmAdmin(admin.ModelAdmin):
	list_display = ('title', 'cost', 'borrower', 'status', 'due_back')
	list_editable = ('due_back',)
	list_filter = ('status', 'due_back', )

	def display_genre(self):
		return ', '.join([ genre.name for genre in self.genre.all()[:3] ])


admin.site.register(Film, FilmAdmin)
admin.site.register(Genre)
