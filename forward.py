from telethon import TelegramClient, events
import asyncio

# 🔵 এখানে আপনার hasan অ্যাকাউন্টের numeric user ID দিন
FORWARD_TO_ID = 7400511368  # 🔴 এটাকে পরিবর্তন করুন

# 🟡 নিচে ৫টি টেলিগ্রাম একাউন্টের api_id, api_hash এবং session_name বসান
accounts = [
    {
        'session_name': 'tn_textnow12',  # ✅ আপনি যেকোনো নাম দিতে পারেন (যেমন: md1)
        'api_id': 22154406,           # 🔴 এখানে ১ম একাউন্টের API ID দিন
        'api_hash': '65f1d3d3935243b83e381f577150a8fe'  # 🔴 এখানে ১ম একাউন্টের API Hash দিন
    },
    {
        'session_name': 'gv_2fa',
        'api_id': 24071259,
        'api_hash': '86d973bfc8bdae59c6b8bfd889a4e39c'
    },
    {
        'session_name': 'gvtnslsof',
        'api_id': 21452724,
        'api_hash': 'b8eb04e8909eaf872a840e4ca372810a'
    },
    {
        'session_name': 'TN_SL365',
        'api_id': 26325474,
        'api_hash': 'b8eb04e8909eaf872a840e4ca372810a'
    },
    {
        'session_name': 'gmailgv123',
        'api_id': 25103261,
        'api_hash': '1467cd6d30263426a496931be0123e52'
    }
]

clients = []

async def main():
    for acc in accounts:
        client = TelegramClient(acc['session_name'], acc['api_id'], acc['api_hash'])
        await client.start()
        clients.append(client)

        @client.on(events.NewMessage(incoming=True))
        async def handler(event):
            try:
                await client.send_message(FORWARD_TO_ID, event.message)
            except Exception as e:
                print(f"Error forwarding message: {e}")

    print("Forwarding bot is running...")
    await asyncio.gather(*(client.run_until_disconnected() for client in clients))

asyncio.run(main())
