import csv
with open('./data/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count_python = 0
    line_count_javascript = 0
    line_count_java = 0
    for row in csv_reader:
        for col in row:
            col2 = col.lower()
            if (col2.count('python')>0  ) :  
                line_count_python += 1
            if (col2.count('javascript')>0):   
                line_count_javascript += 1
            if (col2.count('java')>0 and col2.count('javascript')==0 ) :  
                line_count_java += 1

    print(f'Number of lines with Python or python:  {line_count_python}')
    print(f'Number of lines with JavaScript, javascript or Javascript:  {line_count_javascript}')
    print(f'Number of lines with Java and not JavaScript:  {line_count_java}')