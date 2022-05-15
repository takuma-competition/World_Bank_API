from django.shortcuts import render
from django.http import HttpResponse
import matplotlib

from Country_population.models import Population
#バックエンド指定
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
from django.http import HttpResponse

from .models import Population
import warnings
warnings.simplefilter('ignore')

#世界銀行データAPI
import wbgapi as wb 

#インデックスにアクセスした瞬間に日本の人口データをDBに登録する
def index(request):
    df_pop = wb.data.DataFrame(['SP.POP.TOTL'], 'JPN', mrv=50).T
    #year_list = []
    #pop_list = []
    for item in df_pop.index:
        Population.objects.create(year = int(item[2:]), population = float(df_pop.at[item,'JPN']))
        
        #year_list.append(Population(year = int(item[2:])), Population(population = float(df_pop.at[item,'JPN'])) )
        #pop_list.append(Population(population = float(df_pop.at[item,'JPN'])))

    #Population.objects.bulk_create(year_list)
    #Population.objects.bulk_create(pop_list)

    return render(request, 'Country_population/index.html')

#グラフ作成
def setPlt():
    x = ["07/01", "07/02", "07/03", "07/04", "07/05", "07/06", "07/07"]
    y = [3, 5, 0, 5, 6, 10, 2]
    plt.bar(x, y, color='#00d5ff')
    plt.title(r"$\bf{Running Trend  -2020/07/07}$", color='#3407ba')
    plt.xlabel("Date")
    plt.ylabel("km")

# SVG化
def plt2svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

# 実行するビュー関数
def get_svg(request):
    setPlt()  
    svg = plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response
# Create your views here.
