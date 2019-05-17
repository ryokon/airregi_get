import os
import glob
import pandas as pd
os.chdir("./sales")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined = pd.concat([pd.read_csv(f, encoding='cp932') for f in all_filenames ])
combined = combined.sort_values('集計期間')
#export to csv
combined.to_csv( "combined.csv", index=False, encoding='utf-8-sig')
