from flask import Flask, render_template, request,flash
from time import time
import pyodbc


app = Flask(__name__)
app.secret_key = "Secret"


connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};Server=tcp:cld3.database.windows.net,1433;Database=cl3;Uid=dvk@cld3;Pwd={Gmail2019!};")
cursor = connection.cursor()
print(cursor)

@app.route('/')
def index():
    # page="<h1>Devaki Kamat<h1>"
    # page += "<h1>1001635004</h1>"
    # return page

    return render_template('home.html')


# @app.route('/data', methods=['GET', 'POST'])
# def data():
#     if request.method == 'POST':
#         input3 = request.form['find']
#
#         cursor.execute('SELECT * FROM dbo.records where "mag" >= '+input3+'')
#         rows1 = []
#         result1 = cursor.fetchall()
#         while result1 != False :
#
#             rows1.append(result1.copy())
#             result1 = cursor.fetchall()
#
#     return render_template("data.html", info=rows1)

# @app.route('/')
# def index():
#     start_time = time()
    # cursor.execute("CREATE TABLE [dbo].[records](\
    # 	[time] [datetime2](7) NULL,\
    # 	[latitude] [float] NULL,\
    # 	[longitude] [float] NULL,\
    # 	[depth] [float] NULL,\
    # 	[mag] [float] NULL,\
    # 	[magType] [nvarchar](50) NULL,\
    # 	[nst] [int] NULL,\
    # 	[gap] [float] NULL,\
    # 	[dmin] [float] NULL,\
    # 	[rms] [float] NULL,\
    #     [net] [nvarchar](50) NULL,\
    #     [id][nvarchar](50) NULL,\
    #     [updated] [datetime2](7) NULL,\
    #     [place][nvarchar](100) NULL,\
    #     [type][nvarchar](50) NULL,\
    #     [horizontalError][float] NULL,\
    #     [depthError][float] NULL,\
    #     [magError][float] NULL,\
    #     [magNst][int] NULL,\
    #     [status][nvarchar](50) NULL,\
    #     [locationSource][nvarchar](50) NULL,\
    #     [magSource][nvarchar](50) NULL)")
    # connection.commit()
    #
    #
    #
    #
    # query = "INSERT INTO dbo.records (time,latitude,longitude,depth,mag,magType,nst,gap,dmin,rms,net,id,updated,place,type,horizontalError,depthError,magError,magNst,status,locationSource,magSource) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    # with open('quakes.csv') as csvfile:
    #     next(csvfile)
    #     reader = csv.reader(csvfile, delimiter=',')
    #     for row in reader:
    #         print(row)
    #         cursor.execute(query, row)
    #
    #     connection.commit()
    # end_time = time()
    # time_taken = (end_time - start_time)
    # # flash('The Average Time taken to execute the random queries is : ' + "%.4f" % time_taken + " seconds")
    # return render_template('index.html', t=time_taken)


if __name__ == '__main__':
    app.run()
