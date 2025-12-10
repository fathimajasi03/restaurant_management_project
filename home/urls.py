# home/urls.py
urlpatterns = [
    path('api/menu/categories/', views.MenuCategoriesView.as_view(), name='menu-categories'),
    ]