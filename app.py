import asyncio

from eth_async.client import Client
from eth_async.models import Networks


async def check_wallet(task_id: int):
    while True:
        client = Client(network=Networks.Ethereum)
        bal = await client.wallet.balance()
        s = f"{task_id}: {client.account.address} | {client.account.key.hex()} | {bal.Ether}"
        print(s)
        if bal.Wei != 0:
            with open("success.txt", "a", encoding="utf-8") as f:
                f.write(s + "\n")
        await asyncio.sleep(1)


async def main(count: int):
    tasks = []
    for t_id in range(count):
        tasks.append(asyncio.create_task(check_wallet(t_id)))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main(10))
