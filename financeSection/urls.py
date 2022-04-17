
from django.urls import path
from financeSection.views import paymetSection,deleteYourDetails,updateYourDetails


urlpatterns = [
    path('payment/',paymetSection),
    path('delete/<int:id>',deleteYourDetails),
    path('update/<int:id>',updateYourDetails),
]
