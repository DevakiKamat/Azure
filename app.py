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
        [col2010][nvarchar](100) NULL,\
        [col2011][nvarchar](100) NULL,\
        [col2012][nvarchar](100) NULL,\
        [col2013][nvarchar](100) NULL,\
        [col2014][nvarchar](100) NULL,\
        [col2015][nvarchar](100) NULL,\
        [col2016][nvarchar](100) NULL,\
        [col2017][nvarchar](100) NULL,\
        [col2018][nvarchar](100) NULL)")
    connection.commit()




    query = "INSERT INTO dbo.population (State,col2010,col2011,col2012,col2013,col2014,col2015,col2016,col2017,col2018) VALUES (?,?,?,?,?,?,?,?,?,?)"
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
