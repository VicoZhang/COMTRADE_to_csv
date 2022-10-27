import PyComtrade_Base

# comtrade文件所在文件夹路径，务必保证'.dat'和'.cfg'文件在该目录下
path = '../example'  # 注意不要加后缀

# comtrade文件名，注意不加后缀名
filename = 'BAY01_0001_20221020_114520_483'

Comtrade_reader = PyComtrade_Base.ComtradeFile(file_path=path, file_name=filename)

Comtrade_reader.save_csv(csv_path='../example/csv')  # 生成.csv文件
Comtrade_reader.save_png(png_path='../example/png')  # 生成.png文件
Comtrade_reader.save_mat(mat_path='../example/mat')  # 生成.mat文件

print('comtrade文件已处理结束')
