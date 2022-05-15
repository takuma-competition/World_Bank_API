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
import japanize_matplotlib
import numpy as np

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


def plot_pop_creat():
    #ここを関数化したい
    x_list = Population.objects.all().values('year')
    y_list = Population.objects.all().values('population')

    x = []
    for item in x_list:
        x.append(item['year'])

    y = []
    for item in y_list:
        y.append(item['population'])

    plt.bar(x, y, color='#00d5ff')
    plt.title(r"人口推移", color='#000000')
    #plt.xticks(np.arange(0, 50, 5))
    plt.xlabel("年")
    plt.ylabel("人口")
    return plt

#SVG化
def plot_con_svg(plt):
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

# 実行するビュー関数
def get_svg(request):
    plt = plot_pop_creat()  
    svg = plot_con_svg(plt)  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response