import twint
from multiprocessing import Pool
def twitter_search(word):
	c = twint.Config()
	c.Search = word
	c.Store_csv = True
	c.Since = "2016-06-24"
	c.Until = "2016-06-25"
	c.Format = '| Date: {date} | Time: {time} |'
	#"Tweet id: {id} | Date: {date} | Time: {time} | Username: {username} | User_id: {user_id} | Tweet: {tweet} | Hashtags: {hashtags} | Replies: {replies} | Retweets: {retweets} | Likes: {likes} | Location: {location}"
	c.Output = "bx_results_test.csv".format(word)
	c.Location = True
	twint.run.Search(c)

words = ["Brexit", 'Eureferendum', 'EUreferendum', 'EU Referendum', 'brexit', 'Euref', 'BREXIT']
p = Pool(8)
p.map(twitter_search, words)


#The Right one:
#gcloud compute scp ~Users\owner\Desktop\Scraper_par.py scraping: --zone us-central1-a
