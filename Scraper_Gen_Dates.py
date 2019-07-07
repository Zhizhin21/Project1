import twint
from multiprocessing import Pool
def twitter_search(date):
	c = twint.Config()
	#words = ["Brexit", 'Eureferendum', 'EUreferendum', 'EU Referendum', 'brexit', 'Euref', 'BREXIT']
	c.Search = "Brexit" or 'Eureferendum' or 'EUreferendum' or 'EU Referendum' or 'brexit' or 'Euref' or 'BREXIT'
	c.Store_csv = True
	c.Since = "2016-06-2{}".format(date)
	c.Until = "2016-06-2{}".format(date+1)
	c.Format = '| Date: {date} | Time: {time} |'
	#"Tweet id: {id} | Date: {date} | Time: {time} | Username: {username} | User_id: {user_id} | Tweet: {tweet} | Hashtags: {hashtags} | Replies: {replies} | Retweets: {retweets} | Likes: {likes} | Location: {location}"
	c.Output = "brexit_results_{}.csv".format(date)
	c.Location = True
	twint.run.Search(c)



dates = list(range(1,7))
p = Pool(4)
p.map(twitter_search, dates)
