from django.urls import path
from .views import api_data_view

urlpatterns = [
    path('data/', api_data_view, name='api_data'),
]





# array = ["a", "b", "c"]

# array.each_with_index do |value, index|
#     puts value
#     puts index
# end
# puts "adeus!"


# "a"
# 0

# "b"
# 1

# "c"
# 2

# "adeus!"
