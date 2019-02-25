from flask import Flask, render_template, request,flash
from time import time
import pyodbc
import redis
import random
import csv


app = Flask(__name__)
app.secret_key = "Secret"


connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};Server=tcp:cloud3.database.windows.net,1433;Database=cloud3;Uid=dvk@cloud3;Pwd={Gmail2019!};")
cursor = connection.cursor()
print(cursor)

# # r = redis.Redis(host='rdb3.redis.cache.windows.net', port=6380, password='iA3zVvBHpA+QJD1fPynGJ0gCr5qp4pv5fma8hUfi6MA=',db=0,ssl=True)
# # print(r)
#
# r = redis.StrictRedis(host='rdb3.redis.cache.windows.net', port=6380, db=0, password='iA3zVvBHpA+QJD1fPynGJ0gCr5qp4pv5fma8hUfi6MA=', ssl=True)
#
# # r = redis.StrictRedis(host='rdb3.redis.cache.windows.net',
# # port=6380, password='iA3zVvBHpA+QJD1fPynGJ0gCr5qp4pv5fma8hUfi6MA=', ssl=True)
#
#
#
# @app.route('/')
# def index():
#
#
#     return render_template('home.html')
#
#
# @app.route('/data', methods=['GET', 'POST'])
# def data():
#     if request.method == 'POST':
#         input3 = request.form['find']
#         # runs = request.form['runs']
#
#         start_time = time()
#         cursor.execute('SELECT count(*) FROM dbo.records where "mag" >= ' + input3)
#
#         # for run in runs:
#         #     start_time = time()
#         #     cursor.execute('SELECT count(*) FROM dbo.records where "mag" >= ' + input3)
#
#         while True:
#             rows = cursor.fetchone()
#             if not rows:
#                 break
#             # rows1.append(result1.copy())
#             # result1 = cursor.fetchall()
#             print(rows)
#
#
#         end_time = time()
#         time_taken = (end_time - start_time)
#         return render_template('index.html', t=time_taken)
#         # print("Search over")
#         # return str(rows)
#         # return render_template("data.html", info=rows)
#
#
# @app.route('/rdata', methods=['GET', 'POST'])
# def rdata():
#     if request.method == 'POST':
#         input3 = request.form['find1']
#
#         rows=[]
#         query = 'SELECT count(*) FROM dbo.records where "mag" >= '+input3
#         if r.get(query) == None:
#             print(query)
#             start_time = time()
#             cursor.execute(query)
#             data = cursor.fetchall()
#             # r.set(query,data)
#             # print(data)
#         else:
#             start_time = time()
#             data = r.get(query)
#             # print(data)
#         connection.commit()
#         end_time = time()
#         time_taken = (end_time - start_time)
#         flash('The Average Time taken to execute the random queries is : ' + "%.4f" % time_taken + " seconds")
#         return render_template('rData.html', t=time_taken, rec=data)


@app.route('/')
def index():
    start_time = time()
    cursor.execute("CREATE TABLE [dbo].[population](\
        [State][nvarchar](100) NULL,\
        [2010] [int] NULL,\
        [2011] [int] NULL,\
        [2012] [int] NULL,\
        [2013] [int] NULL,\
        [2014] [int] NULL,\
        [2015] [int] NULL,\
        [2016] [int] NULL,\
        [2017] [int] NULL,\
        [2018] [int] NULL)")
    connection.commit()




    query = "INSERT INTO dbo.population (State,2010,2011,2012,2013,2014,2015,2016,2017,2018) VALUES (?,?,?,?,?,?,?,?,?,?)"
    with open('population.csv') as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(row)
            cursor.execute(query, row)

        connection.commit()
    end_time = time()
    time_taken = (end_time - start_time)
    # flash('The Average Time taken to execute the random queries is : ' + "%.4f" % time_taken + " seconds")
    return render_template('index.html', t=time_taken)


if __name__ == '__main__':
    app.run()
