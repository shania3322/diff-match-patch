import diff_match_patch as dmp
import pandas as pd
import numpy as np
import sys
from termcolor import colored


def diff_wordMode(text1,text2):
    pass
        
def highlight(color, text:str):
    pass

def highlight_diff(text:str, diff:tuple):
    pass
    



def main():	
	
    pd.options.display.max_colwidth = 100
    #num_rows =50
    path = 'out1.csv'
    #data = pd.read_csv(path, nrows=num_rows, index_col=[0])
    data = pd.read_csv(path, index_col=[0],names = ['Predictions','Scores','Confidence scores'])
    data = data.reset_index(drop=True)
    data.style.set_properties(**{'text-align': 'left'})
    #print(data.head())
    	
    ref = data['Predictions'][0]
    hyps = data['Predictions'][1:4].astype(str).values.tolist()
	
    for i, hyp in enumerate(hyps):
         print(f'The {i}th: ')
         print(f'ref: {ref}')
         print(f'hyp {i}: {hyps[i]}')
         new_compare = dmp.diff_match_patch()
         line_diffs = new_compare.diff_lineMode(hyps[i],ref,deadline=1.0)
         print(line_diffs,"\n")

    '''
    line_diffs = map(new_compare.diff_lineMode(hyp, ref), hyp for hyp in hyps)
    print(set(line_diffs))
    '''
	

if __name__ == "__main__":
    main()
