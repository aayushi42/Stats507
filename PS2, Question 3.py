"""
Question 3
Part a
Importing files from the internet and using Pandas to read, clean, and append
the data files.
Finally, save the resulting data frame to pickle format in directory.
"""
# File Path
path = './'

# Column names
demo_cols = {
    'SEQN': 'id',
    'RIDAGEYR': 'age',
    'RIDRETH3': 'race',
    'DMDEDUC2': 'education',
    'DMDMARTL': 'marital_status',
    'RIDSTATR': 'exam_status',
    'SDMVPSU': 'psu',
    'SDMVSTRA': 'strata',
    'WTMEC2YR': 'exam_wt',
    'WTINT2YR': 'interview_wt'
    }
# levels for int variabls
demo_int = ('id', 'age', 'psu', 'strata')
# levels for categorical variables
demo_cat = {
    'gender': {1: 'Male', 2: 'Female'},
    'race': {1: 'Mexican American',
             2: 'Other Hispanic',
             3: 'Non-Hispanic White',
             4: 'Non-Hispanic Black',
             6: 'Non-Hispanic Asian',
             7: 'Other/Multiracial'
             },
    'education': {1: 'Less than 9th grade',
                  2: '9-11th grade (Includes 12th grade with no diploma)',
                  3: 'High school graduate/GED or equivalent',
                  4: 'Some college or AA degree',
                  5: 'College graduate or above',
                  7: 'Refused',
                  9: "Don't know"
                  },
    'marital_status': {1: 'Married',
                       2: 'Widowed',
                       3: 'Divorced',
                       4: 'Separated',
                       5: 'Never married',
                       6: 'Living with partner',
                       77: 'Refused',
                       99: "Don't know"
                       },
    'exam_status': {1: 'Interviewed only',
                    2: 'Both interviewed and MEC examined'
                    }
    }


data1 = pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DEMO_G.XPT').copy()
data2 = pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DEMO_H.XPT').copy()
data3 = pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.XPT').copy()
data4 = pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT').copy()
data1["cohort"] = "2011-2012"
data2["cohort"] = "2013-2014"
data3["cohort"] = "2015-2016"
data4["cohort"] = "2017-2018"

dataset = pd.concat([data1, data2, data3, data4])
dataset['cohort'] = pd.Categorical(dataset['cohort'])
dataset = dataset[list(demo_cols.keys())].rename(columns=demo_cols)
# categorical variables
for col, d in demo_cat.items():
    dataset[col] = pd.Categorical(dataset[col].replace(d))

    # integer variables
for col in demo_int:
    dataset[col] = pd.to_numeric(dataset[col], downcast='integer')
# All the other columns have the type float64 which is fine.
dataset.to_pickle(
    "C:/Users/Aayushi Sinha/Desktop/M.S Applied Statistics/Fall 2021/STATS 507/demographicdataset.sas"
    )
dataset.shape

"""
Part b
"""
ohx_cols = {'SEQN': 'id', 'OHDDESTS': 'dentition_status'}
tc_cols = {'OHX' + str(i).zfill(2) + 'TC':
           'tc_' + str(i).zfill(2) for i in range(1, 33)}
ctc_cols = {'OHX' + str(i).zfill(2) + 'CTC':
            'ctc_' + str(i).zfill(2) for i in range(2, 32)}
_, _ = ctc_cols.pop('OHX16CTC'), ctc_cols.pop('OHX17CTC')
ohx_cols.update(tc_cols)
ohx_cols.update(ctc_cols)
ohx_int = ('id', )
ohx_cat = {
    'dentition_status': {1: 'Complete', 2: 'Partial', 3: 'Not Done'}
    }
tc = {
      1: 'Primary tooth present',
      2: 'Permanent tooth present',
      3: 'Dental Implant',
      4: 'Tooth not present',
      5: 'Permanent dental root fragment present',
      9: 'Could not assess'
      }
ctc = (
 {
  'A': 'Primary tooth with a restored surface condition',
  'D': 'Sound primary tooth',
  'E': 'Missing due to dental disease',
  'F': 'Permanent tooth with a restored surface condition',
  'J':
    'Permanent root tip is present but no restorative replacement is present',
  'K': 'Primary tooth with a dental carious surface condition',
  'M': 'Missing due to other causes',
  'P':
    'Missing due to dental disease but replaced by a removable restoration',
  'Q':
    'Missing due to other causes but replaced by a removable restoration',
  'R':
    'Missing due to dental disease but replaced by a fixed restoration',
  'S': 'Sound permanent tooth',
  'T':
    'Permanent root tip is present but a restorative replacement is present',
  'U': 'Unerupted',
  'X': 'Missing due to other causes but replaced by a fixed restoration',
  'Y': 'Tooth present, condition cannot be assessed',
  'Z': 'Permanent tooth with a dental carious surface condition'
 })

df1 = pd.read_sas("https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/OHXDEN_G.XPT").copy()
df2 = pd.read_sas("https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OHXDEN_H.XPT").copy()
df3 = pd.read_sas("https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/OHXDEN_I.XPT").copy()
df4 = pd.read_sas("https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/OHXDEN_J.XPT").copy()
df1["cohort"] = "2011-2012"
df2["cohort"] = "2013-2014"
df3["cohort"] = "2015-2016"
df4["cohort"] = "2017-2018"
data = pd.concat([df1, df2, df3, df4])
data['cohort'] = pd.Categorical(data['cohort'])
data = data[list(ohx_cols.keys())].rename(columns=ohx_cols)
# categorical variables
for col, d in ohx_cat.items():
    data[col] = pd.Categorical(data[col].replace(d))
    
for col in tc_cols.values():
    data[col] = pd.Categorical(data[col].replace(tc))

# ctc columns get read in as bytes
for col in ctc_cols.values():
    data[col] = data[col].apply(lambda x: x.decode('utf-8'))
    data[col] = pd.Categorical(data[col].replace(ctc))
    
# integer variables
for col in ohx_int:
    data[col] = pd.to_numeric(data[col], downcast='integer')
    
data.to_pickle(
    "C:/Users/Aayushi Sinha/Desktop/M.S Applied Statistics/Fall 2021/STATS 507/dentaldata.sas"
    )
"""
Question 3
Part c
"""
print(dataset.shape)
print(data2.shape)
