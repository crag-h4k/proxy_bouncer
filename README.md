# Proxy Bouncer

Proxies are scraped and saved from  https://free-proxy-list.net

To save a log of anonymous active proxies use the command

`get_proxy(log=True)`

Used as a function in another program, ` get_proxy() ` will return a random it will a proxy oject as shown in the example below:

`
    
    P = get_proxy()

    print(P.ip_addr)        

    '103.18.133.34'

    print(P.port)

    '21776'

    print(P.code)

    'ID'

    print(P.country)

    'Indonesia'

    print(P.anon_level)

    'elite proxy'

    print(P.google)

    'no'

    print(P.https

    'no'
`

