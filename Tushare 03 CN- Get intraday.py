import tushare
import pandas
import datetime
import os
import time


# 因为每只股票所要得到的数据结果都是一样的，所以我们只需要
# 定义一个函数完成这种功能即可
def stockPriceIntraday(ticker,folder):
    #step 1: 获取五分钟k线的所有数据
    intraday = tushare.get_hist_data(ticker, ktype='5')
    #step 2: 新建一个文件file
    file = folder+'/'+ticker+'.csv'
    #step 5 :系统需要先找到文件才能逐行写入数据，再用pandas类名调用rend_csv方法
    # 读取文件头，当值为0时，用append在下方继续添加数据。这样的结果
    # 就是可以将数据翻转过来，便于读取。
    if os.path.exists(file):

        history = pandas.read_csv(file,index_col=0)

        intraday.append(history)
    # print(intraday)
    # step 3 :获取头部信息，并把名字改成'timestemps'
    intraday.sort_index(inplace=True)
    intraday.index.name='timestemps'
    # step 4:将提取并整理之后的数据丢到文件里
    intraday.to_csv(file)
    print('intraday got and save')

# ----------------这里穿插一段代码用于测试--------------------
# step1:通过'get_stock_basics()'方法可以直接获取所有股票面板信息
TickersRawData = tushare.get_stock_basics()
# step2:通过第一步的对象调用index.tolist()方法，获取所有股票面板信息的头部（即股票代码）
tickers = TickersRawData.index.tolist()
# step3:新建一个后缀为'.csv'的文件，并用today().strftime()修改一下文件名的格式
dateToday = datetime.datetime.today().strftime('%Y%m%d')
# 重点提醒：新建TickerList_文件时，只能引用到它上层的两层目录/Data/TickerListCN/多或者少都会报错！！！
file = '../Data/TickerListCN/TickerList_'+dateToday+'.csv'
# 通过to_csv()方法，把第二步获取到的信息丢到刚新建的.csv文件中，并用print()方法打印到屏幕中
TickersRawData.to_csv(file)
print('tickers save')
# # ----------------这里穿插一段代码用于测试--------------------


# step 6:当做到第5步时，我们已经完成了一个功能函数的定义，我们只需调用这个函数便可以获取一只股票的信息
# 所以我们想要获取A股所有股票信息，只需要对它进行遍历就行。

for i ,ticker in enumerate(tickers):
    # 在循环中加一个异常的反馈，try ,except:  最后break 完成程序
    try:
        print('intraday',i,'/',len(tickers))
        stockPriceIntraday(ticker, folder='../Data/intradayCN')
        time.sleep(5)
    except:
        pass
    if i>50:

        break

print('end')





# stockPriceIntraday('600031',folder = '../Data/intradayCN')