from django.shortcuts import render
from product.models import Drink,Category
import pandas as pd

# Create your views here.
def home(request):
    drinks = pd.read_csv('/content/drive/MyDrive/recommendation/starbucks/drinks_category.csv', encoding='euc-kr')
    print(drinks.to_string())
    # product = drinks.object.all().values()
    # df = pd.DataFrame(product)
    # mydict = {
    #     "df":df.to_html()
    # }
    # return render(request,'base.html',context=mydict)

# ratings = pd.read_csv('/content/drive/MyDrive/recommendation/starbucks/new_drink_ratings.csv')




