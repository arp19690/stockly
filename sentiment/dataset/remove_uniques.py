lines=set([line for line in open('unclean_test.data').readlines()])
data_file=open('train.data','w')
for line in lines: data_file.write(line+"\n")


