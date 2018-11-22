运用pandas把users.bat文件写入msql数据库

1.连接数据库

     import sqlalchemy as sqla

     db= sqla.create_engine('mysql+pymysql://root:123456@127.0.0.1/movies')

2.把.dat文件转成dataframe

    mnames = ['movie_id', 'title', 'genres']
    users = pd.read_table('datasets/movielens/movies.dat', sep='::',
    .....: header=None, names=mnames, engine='python')

3.写入数据库,tablename:数据库表名

    user.to_sql('tablename',con=db,index=False,if_exsits='append')
