import twint
c = twint.Config()
c.Search = "Brexit" or 'Eureferendum' or 'EUreferendum' or 'EU Referendum' or 'brexit' or 'Euref' or 'BREXIT'
c.Store_csv = True
c.Since = "2016-06-23"
c.Until = "2016-06-24"
c.Format = '| Date: {date} | Time: {time} |'
c.Output = "brexit_results_23.csv"
c.Location = True
twint.run.Search(c)
