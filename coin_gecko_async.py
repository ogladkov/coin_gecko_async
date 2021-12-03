import pickle
import asyncio
import time
from aiocoingecko import AsyncCoinGeckoAPISession


class CoinGeckoLoader:
    def __init__(self):
        with open('categories_with_tokens', 'rb') as cwt:
            # Load list of coins for categories
            self.cwt = pickle.load(cwt)

        self.coin_market_chart_by_id = None

    def get_coin_market_chart_by_id(self, coins_list, alt_cur='usd'):
        # Download historical data for all coins of category
        all_data = {}

        async def get_data(cur, con):
            all_data[cur] = await con.get_coin_market_chart_by_id(cur, alt_cur, 'max')

        async def main(coins_list_shorten):
            async with AsyncCoinGeckoAPISession() as con:
                tasks = []
                for t in [get_data]:
                    for cur in coins_list_shorten:
                        tasks.append(asyncio.create_task(t(cur, con)))
                await asyncio.gather(*tasks)

        t0 = time.time()
        c1 = 0
        c2 = 50
        while True:
            coins_list_shorten = coins_list[c1:c2]
            if len(coins_list) > 0:
                asyncio.run(main(coins_list_shorten))
                while time.time() < t0 + 60:
                    time.sleep(1)
                t0 = time.time()
                c1 += 50
                c2 += 50
            else:
                break

        self.coin_market_chart_by_id = all_data


if __name__ == '__main__':
    cga = CoinGeckoLoader()
    metaverse_coins = cga.cwt['metaverse']
    result = cga.get_coin_market_chart_by_id(metaverse_coins)
    print(result)