from flask import Flask, render_template, request, flash, jsonify, Response, make_response
from time import time
import pyodbc
# import json
# import redis
# import random
# import csv
from sqlalchemy import create_engine
import urllib

app = Flask(__name__)
app.secret_key = "Secret"


# connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};Server=tcp:dvkc4.database.windows.net,1433;Database=dbc4;Uid=dvk@dvkc4;Pwd={Gmail2019!};")
# cursor = connection.cursor()
# print(cursor)

params = urllib.quote_plus("Driver={ODBC Driver 17 for SQL Server};Server=tcp:dvkc4.database.windows.net,1433;Database=dbc4;Uid=dvk@dvkc4;Pwd={Gmail2019!};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
#params = urllib.parse.quote_plus("Driver={ODBC Driver 13 for SQL Server};Server=tcp:dvkc4.database.windows.net,1433;Database=dbc4;Uid=dvk@dvkc4;Pwd={Gmail2019!};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

# r = redis.StrictRedis(host='rdb3.redis.cache.windows.net', port=6380, db=0, password='iA3zVvBHpA+QJD1fPynGJ0gCr5qp4pv5fma8hUfi6MA=', ssl=True)

@app.route('/')
def index():
    # start_time = time()
    # query = "SELECT State,col2011 FROM dbo.population"
    # print(query)
    # r = engine.execute(query).fetchall()
    # r = [dict(row) for row in r]
    #
    # end_time = time()
    # time_taken = (end_time - start_time)
    # return render_template('index.html', t=time_taken, data=r)


    return render_template('home.html')


# @app.route('/data', methods=['GET', 'POST'])
# def data():



@app.route('/rdata', methods=['GET', 'POST'])
def rdata():
    if request.method == 'POST':
        input3 = request.form['state']


        start_time = time()
        query= "SELECT code,count(county) as mycnt FROM dbo.statecode,dbo.counties where Statec = cState and code = '"+input3+"' group by code"
        print(query)
        r = engine.execute(query).fetchall()
        print(r)
        r = [dict(row) for row in r]



    end_time = time()
    time_taken = (end_time - start_time)
    return render_template('rdata.html', t=time_taken , rec=r)


@app.route('/barg', methods=['GET', 'POST'])
def barg():
    start_time = time()
    query = "SELECT Sum(blpercent) as sum,year FROM dbo.edshare group by year"
    print(query)
    r = engine.execute(query).fetchall()
    r = [dict(row) for row in r]

    end_time = time()
    time_taken = (end_time - start_time)
    return render_template('barg.html', t=time_taken, rec=r)


# @app.route('/pieg', methods=['GET', 'POST'])
# def pieg():
#     if request.method == 'POST':
#         input5 = request.form['year']
#         input6 = request.form['r1']
#         input7 = request.form['r2']
#         input8 = request.form['r3']
#         input9 = request.form['r4']
#         input10 = request.form['r5']
#         input11 = request.form['r6']
#
#         start_time = time()
#         query = "SELECT count(State) as count,State FROM dbo.population where "+input5+" between '" + input6 + "' and '" + input7 + "' and "+input5+" between '" + input8 + "' and '" + input9 + "' and "+input5+" between '" + input10 + "' and '" + input11 + "' group by State"
#         print(query)
#         r = engine.execute(query).fetchall()
#         # # print(r)
#         # r = [dict(row) for row in r]
#
#     end_time = time()
#     time_taken = (end_time - start_time)
#     return render_template('pieg.html', t=time_taken, rec=r)


@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        input3 = request.form['loc']
        input4 = request.form['y1']
        input5 = request.form['y2']


        start_time = time()
        query= "SELECT year,blpercent FROM dbo.edshare where year between '"+input4+"' and '"+input5+"'"
        print(query)
        r = engine.execute(query).fetchall()
        print(r)
        r = [dict(row) for row in r]



    end_time = time()
    time_taken = (end_time - start_time)
    return render_template('data.html', t=time_taken, rec=r)





# @app.route('/pdata', methods=['GET', 'POST'])
# def pdata():
#     if request.method == 'POST':
#         input3 = request.form['code']
#
#         rows=[]
#         query = 'SELECT col2011 FROM dbo.population,dbo.statecode where "State" = "cState" and "code" = \'+input3\''#         if r.get(query) == None:
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



# @app.route('/')
# def index():
#     start_time = time()
#     cursor.execute("CREATE TABLE [dbo].[population](\
#         [State][nvarchar](100) NULL,\
#         [col2010][nvarchar](100) NULL,\
#         [col2011][nvarchar](100) NULL,\
#         [col2012][nvarchar](100) NULL,\
#         [col2013][nvarchar](100) NULL,\
#         [col2014][nvarchar](100) NULL,\
#         [col2015][nvarchar](100) NULL,\
#         [col2016][nvarchar](100) NULL,\
#         [col2017][nvarchar](100) NULL,\
#         [col2018][nvarchar](100) NULL)")
#     connection.commit()
#
#
#
#
#     query = "INSERT INTO dbo.population (State,col2010,col2011,col2012,col2013,col2014,col2015,col2016,col2017,col2018) VALUES (?,?,?,?,?,?,?,?,?,?)"
#     with open('population.csv') as csvfile:
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


# @app.route('/')
# def index():
#     start_time = time()
#     cursor.execute("CREATE TABLE [dbo].[counties](\
#         [county][nvarchar](100) NULL,\
#         [Statec][nvarchar](100) NULL)")
#     connection.commit()
#
#
#
#
#     query = "INSERT INTO dbo.counties (county,Statec) VALUES (?,?)"
#     with open('counties.csv') as csvfile:
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


# @app.route('/')
# def index():
#     start_time = time()
#     cursor.execute("CREATE TABLE [dbo].[statecode](\
#         [code][nvarchar](100) NULL,\
#         [cState][nvarchar](100) NULL)")
#     connection.commit()
#
#
#     query = "INSERT INTO dbo.statecode (code,cState) VALUES (?,?)"
#     with open('statecode.csv') as csvfile:
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



# @app.route('/')
# def index():
#     start_time = time()
#     cursor.execute("CREATE TABLE [dbo].[quakes](\
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
#         [net][nvarchar](50) NULL,\
#         [id][nvarchar](50) NULL,\
#         [updated] [datetime2](7) NULL,\
#         [place][nvarchar](100) NULL,\
#         [type][nvarchar](50) NULL,\
#         [horizontalError][float] NULL,\
#         [depthError][float] NULL,\
#         [magError][float] NULL,\
#         [magNst][int] NULL,\
#         [status] [nvarchar](50) NULL,\
#         [locationSource][nvarchar](50) NULL,\
#         [magSource][nvarchar](50) NULL)")
#     connection.commit()
#
#
#
#
#     query = "INSERT INTO dbo.quakes (time,latitude,longitude,depth,mag,magType,nst,gap,dmin,rms,net,id,updated,place,type,horizontalError,depthError,magError,magNst,status,locationSource,magSource) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
#
#
#     with open('quakes.csv') as csvfile:
#           next(csvfile)
#           reader = csv.reader(csvfile, delimiter=',')
#           for row in reader:
#               print(row)
#               cursor.execute(query,row)
#
#           connection.commit()
#     end_time = time()
#     time_taken = (end_time - start_time)
#     flash('The Average Time taken to execute the random queries is : ' + "%.4f" % time_taken + " seconds")
#     return render_template('index.html', t=time_taken)


# @app.route('/')
# def index():
#     start_time = time()
#     cursor.execute("CREATE TABLE [dbo].[edshare](\
#         [entity][nvarchar](100) NULL,\
#         [code][nvarchar](50) NULL,\
#         [year][nvarchar](50) NULL,\
#         [blpercent][float] NULL)")
#     connection.commit()
#
#
#     query = "INSERT INTO dbo.edshare (entity,code,year,blpercent) VALUES (?,?,?,?)"
#     with open('edshare.csv') as csvfile:
#         next(csvfile)
#         reader = csv.reader(csvfile, delimiter=',')
#         for row in reader:
#             print(row)
#             cursor.execute(query, row)
#
#         connection.commit()
#     end_time = time()
#     time_taken = (end_time - start_time)
#     # # flash('The Average Time taken to execute the random queries is : ' + "%.4f" % time_taken + " seconds")
#     # return render_template('index.html', t=time_taken)


if __name__ == '__main__':
    app.run()
