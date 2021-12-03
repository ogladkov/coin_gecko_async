Coin Geck Async Data downloader for Python

It downloads data fast by the reason of using aiocoingecko - async wrapper for CoinGecko API.

### Installation
1. Clone repo
2. Install requiremets from 'requirements.txt'
3. Import 'oin_gecko_async'


### How to use

- Create class instance of CoinGeckoLoader
- Load coins with categories by calling 'cga.cwt[{name_of_class}]'
- Call a method:
  - get_coin_market_chart_by_id(coins_list) - gathers prices, market capitalization and volumes history for a list of coins.
