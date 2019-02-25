from flask import Flask, render_template, request,flash
from time import time
import pyodbc
import redis
import csv


app = Flask(__name__)
app.secret_key = "Secret"


connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};Server=tcp:cloud3.database.windows.net,1433;Database=cloud3;Uid=dvk@cloud3;Pwd={Gmail2019!};")
cursor = connection.cursor()
print(cursor)

r = redis.Redis(host='rdb3.redis.cache.windows.net', port=6380, password='iA3zVvBHpA+QJD1fPynGJ0gCr5qp4pv5fma8hUfi6MA=',db=0,ssl=True)
print(r)

@app.route('/')
def index():


    return render_template('home.html')


@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        input3 = request.form['find']
        start_time = time()

        cursor.execute('SELECT * FROM dbo.records where "mag" >= '+input3)

        print("Fetched results")
        while True:
            rows = cursor.fetchone()
            if not rows:
                break
            # rows1.append(result1.copy())
            # result1 = cursor.fetchall()
            print(rows)

        end_time = time()
        time_taken = (end_time - start_time)
        return render_template('index.html', t=time_taken)
        # print("Search over")
        # return str(rows)
        # return render_template("data.html", info=rows)


# @app.route('/rdata', methods=['GET', 'POST'])
# def rdata():
#     if request.method == 'POST':
#         input3 = request.form['find1']
#         start_time = time()
#         rows=[]
#         query = 'SELECT * FROM dbo.records where "mag" >= '+input3
#         if r.get(query) == None:
#             cursor.execute(query)
#             data = cursor.fetchall()
#             r.set(query, data)
#             rows=data
#             print("No Cache")
#         else:
#             data = r.get(query)
#             print(data)
#             data = data.replace(')', '')
#             data = data.replace('[', '')
#             data = data.replace(']', '')
#             rowL = data.split('(')
#             for row in rowL:
#                 print(row)
#                 item = row.split(',')
#                 rows.append(item)
#                 print(rows)
#                 print("Redis")
#         db.close()
#         end_time = time()
#         time_taken = (end_time - start_time)
#         return render_template('rData.html', data=rows)


# @app.route('/')
# def index():
#     start_time = time()
#     cursor.execute("CREATE TABLE [dbo].[records](\
#     	[time] [datetime2](7) NULL,\
#     	[latitude] [float] NULL,\
#     	[longitude] [float] NULL,\
#     	[depth] [float] NULL,\
#     	[mag] [float] NULL,\
#     	[magType] [nvarchar](50) NULL,\
#     	[nst] [int] NULL,\
#     	[gap] [float] NULL,\
#     	[dmin] [float] NULL,\
#     	[rms] [float] NULL,\
#         [net] [nvarchar](50) NULL,\
#         [id][nvarchar](50) NULL,\
#         [updated] [datetime2](7) NULL,\
#         [place][nvarchar](100) NULL,\
#         [type][nvarchar](50) NULL,\
#         [horizontalError][float] NULL,\
#         [depthError][float] NULL,\
#         [magError][float] NULL,\
#         [magNst][int] NULL,\
#         [status][nvarchar](50) NULL,\
#         [locationSource][nvarchar](50) NULL,\
#         [magSource][nvarchar](50) NULL)")
#     connection.commit()
#
#
#
#
#     query = "INSERT INTO dbo.records (time,latitude,longitude,depth,mag,magType,nst,gap,dmin,rms,net,id,updated,place,type,horizontalError,depthError,magError,magNst,status,locationSource,magSource) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
#     with open('quakes.csv') as csvfile:
#         next(csvfile)
#         reader = csv.reader(csvfile, delimiter=',')
#         for row in reader:
#             print(row)
#             cursor.execute(query, row)
#
#         connection.commit()
#     end_time = time()
#     time_taken = (end_time - start_time)
#     # flash('The Average Time taken to execute the random queries is : ' + "%.4f" % time_taken + " seconds")
#     return render_template('index.html', t=time_taken)


if __name__ == '__main__':
    app.run()
