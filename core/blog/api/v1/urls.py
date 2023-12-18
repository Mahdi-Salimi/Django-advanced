from django.urls import path
from .views import PostList, PostDetail, PostModelViewSet, CategoryModelViewSet
from rest_framework.routers import DefaultRouter

app_name='api-v1'

router = DefaultRouter()
router.register('post', PostModelViewSet,basename='post')
router.register('category', CategoryModelViewSet,basename='category ')
urlpatterns = router.urls



# urlpatterns = [
#     path('', PostList.as_view(), name='post-list'),
#     path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
# ]