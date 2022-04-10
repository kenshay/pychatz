import json
import httpx
import asyncio


async def send_slack_channel_notification():
    message = {
        "blocks": [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": 'test'
                }
            }
        ]
    }

    slack_payload = json.dumps(message).encode("utf-8")
    slack_headers = [(b"content-type", b"application/json")]

    slack_url = "https://hooks.slack.com/services/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"

    if slack_url:
        async with httpx.AsyncClient() as client:
            await client.post(
                    slack_url, headers=slack_headers, data=slack_payload
                )





asyncio.run(send_slack_channel_notification())

