# user-agent-scraper

You can view all possible browsers [here](http://www.useragentstring.com/pages/useragentstring.php).

`import user_agent_scraper`

`user_agent_scraper.get_valid_agents()` - get all browsers, returned in an array
`user_agent_scraper.scrape_user_agents(browsers)` - gets all user agents for the browsers passed into an array

## example:
`
import user_agent_scraper
import requests

agents = user_agent_scraper.scrape_user_agents(["Firefox", "Edge"])

requests.get("http://example.com", headers={"User-Agent":random.choice(agents)})
`
