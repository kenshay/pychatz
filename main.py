async def send_slack_channel_notification(nuula_request_info_dict):

    nuula_request_header = nuula_request_info_dict.get('header',{})
    nuula_request_payload = nuula_request_info_dict.get('payload',{})

    nuula_request_payload_str = f"\n####### INTERNAL INFO #########\n\n"

    nuula_request_payload_str += f"*destination_url*: " \
        f" {nuula_request_info_dict.get('api_web_hook_nuula','')}\n" \
        f"*internal_event*: " \
        f"{nuula_request_info_dict.get('internal_event','')}\n"

    nuula_request_payload_str += f"\n####### REQUEST HEADER #########\n\n"

    for key in nuula_request_header.keys():
        if key == AUTH_HEADER:
            line = f"*{key}*: ***********\n"
        else:
            line = f"*{key}*: {nuula_request_header.get(key, '')}\n"
        nuula_request_payload_str += line

    nuula_request_payload_str += f"\n####### REQUEST PAYLOAD #########\n\n"

    for key in nuula_request_payload.keys():
        line = f"*{key}*: {nuula_request_payload.get(key, '')}\n"
        nuula_request_payload_str += line

    message = {
        "blocks": [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": nuula_request_payload_str
                }
            }
        ]
    }

    slack_payload = json.dumps(message).encode("utf-8")
    slack_headers = [(b"content-type", b"application/json")]

    slack_url = nuula_request_info_dict.get("slack_url")

    if slack_url:
        async with httpx.AsyncClient() as client:
            await client.post(
                slack_url, headers=slack_headers, data=slack_payload
            )