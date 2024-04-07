import requests
import pandas as pd

products_master_list = []
START_PAGE = 1
END_PAGE = 2

category_headers = {
    'accept': '*/*',
    'accept-language': 'fr',
    'authorization': '',
    'content-type': 'application/json',
    'locale': 'fr',
    'origin': 'https://www.ouedkniss.com',
    'referer': 'https://www.ouedkniss.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-app-version': '"2.2.42"',
    'x-referer': 'https://www.ouedkniss.com/automobiles/1?keywords=voiture&hasPrice=true',
    # 'x-track-id': '498fc604-2a6e-48a7-a279-f1e1e6d549e1',
    # 'x-track-timestamp': '1711900530',
    # 'x-track-timestamp': '1712016638',
}

product_headers = {
    'accept': '*/*',
    'accept-language': 'fr',
    'authorization': '',
    'content-type': 'application/json',
    'locale': 'fr',
    'origin': 'https://www.ouedkniss.com',
    'referer': 'https://www.ouedkniss.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-app-version': '"2.2.42"',
    'x-referer': 'https://www.ouedkniss.com/commerciale-fiat-doblo-2024-saida-algerie-d40107025',
    # 'x-track-id': '498fc604-2a6e-48a7-a279-f1e1e6d549e1',
    # 'x-track-timestamp': '1712018449',
}

#### loop through the pages
for page_number in range(START_PAGE, END_PAGE):

    print(f'*** Scraping Ids for page: {page_number}')
    
    category_json_data = {
        'operationName': 'SearchQuery',
        'variables': {
            'mediaSize': 'MEDIUM',
            'q': None,
            'filter': {
                'categorySlug': 'automobiles',
                'origin': None,
                'connected': False,
                'delivery': None,
                'regionIds': [],
                'cityIds': [],
                'priceRange': [
                    None,
                    None,
                ],
                'exchange': False,
                'hasPictures': False,
                'hasPrice': False,
                'priceUnit': None,
                'fields': [],
                'page': page_number,
                'count': 48,
            },
        },
        'query': 'query SearchQuery($q: String, $filter: SearchFilterInput, $mediaSize: MediaSize = MEDIUM) {\n  search(q: $q, filter: $filter) {\n    announcements {\n      data {\n        ...AnnouncementContent\n        smallDescription {\n          valueText\n          __typename\n        }\n        noAdsense\n        __typename\n      }\n      paginatorInfo {\n        lastPage\n        hasMorePages\n        __typename\n      }\n      __typename\n    }\n    active {\n      category {\n        id\n        name\n        slug\n        icon\n        delivery\n        deliveryType\n        priceUnits\n        children {\n          id\n          name\n          slug\n          icon\n          __typename\n        }\n        specifications {\n          isRequired\n          specification {\n            id\n            codename\n            label\n            type\n            class\n            datasets {\n              codename\n              label\n              __typename\n            }\n            dependsOn {\n              id\n              codename\n              __typename\n            }\n            subSpecifications {\n              id\n              codename\n              label\n              type\n              __typename\n            }\n            allSubSpecificationCodenames\n            __typename\n          }\n          __typename\n        }\n        parentTree {\n          id\n          name\n          slug\n          icon\n          children {\n            id\n            name\n            slug\n            icon\n            __typename\n          }\n          __typename\n        }\n        parent {\n          id\n          name\n          icon\n          __typename\n        }\n        __typename\n      }\n      count\n      __typename\n    }\n    suggested {\n      category {\n        id\n        name\n        slug\n        icon\n        __typename\n      }\n      count\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AnnouncementContent on Announcement {\n  id\n  title\n  slug\n  createdAt: refreshedAt\n  isFromStore\n  isCommentEnabled\n  userReaction {\n    isBookmarked\n    isLiked\n    __typename\n  }\n  hasDelivery\n  deliveryType\n  likeCount\n  description\n  status\n  cities {\n    id\n    name\n    slug\n    region {\n      id\n      name\n      slug\n      __typename\n    }\n    __typename\n  }\n  store {\n    id\n    name\n    slug\n    imageUrl\n    isOfficial\n    isVerified\n    __typename\n  }\n  user {\n    id\n    __typename\n  }\n  defaultMedia(size: $mediaSize) {\n    mediaUrl\n    mimeType\n    thumbnail\n    __typename\n  }\n  price\n  pricePreview\n  priceUnit\n  oldPrice\n  oldPricePreview\n  priceType\n  exchangeType\n  category {\n    id\n    slug\n    __typename\n  }\n  __typename\n}\n',
    }  

    response = requests.post('https://api.ouedkniss.com/graphql', headers=category_headers, json=category_json_data)
    list_data = response.json()

    ### get product ids with price
    product_ids_with_price = [product['id'] for product in list_data['data']['search']['announcements']['data'] ]
    print(f'Number of cars with price found on the page: {len(product_ids_with_price)}')
    # print(product_ids_with_price)

    ### loop through the product ids
    ### get the product data
    for product_index, product_id in enumerate(product_ids_with_price):
        print(f'product_index: {product_index}, product_id: {product_id}')
        try:

            product_json_data = {
                'operationName': 'AnnouncementGet',
                'variables': {
                    'id': product_id,
                },
                'query': 'query AnnouncementGet($id: ID!) {\n  announcement: announcementDetails(id: $id) {\n    id\n    reference\n    title\n    slug\n    description\n    orderExternalUrl\n    createdAt: refreshedAt\n    price\n    pricePreview\n    oldPrice\n    oldPricePreview\n    priceType\n    exchangeType\n    priceUnit\n    hasDelivery\n    deliveryType\n    hasPhone\n    hasEmail\n    quantity\n    status\n    street_name\n    category {\n      id\n      slug\n      name\n      deliveryType\n      __typename\n    }\n    defaultMedia(size: ORIGINAL) {\n      mediaUrl\n      __typename\n    }\n    medias(size: LARGE) {\n      mediaUrl\n      mimeType\n      thumbnail\n      __typename\n    }\n    categories {\n      id\n      name\n      slug\n      parentId\n      __typename\n    }\n    specs {\n      specification {\n        label\n        codename\n        type\n        __typename\n      }\n      value\n      valueText\n      __typename\n    }\n    user {\n      id\n      username\n      displayName\n      avatarUrl\n      __typename\n    }\n    isFromStore\n    store {\n      id\n      name\n      slug\n      description\n      imageUrl\n      url\n      followerCount\n      announcementsCount\n      locations {\n        location {\n          address\n          region {\n            slug\n            name\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      categories {\n        name\n        slug\n        __typename\n      }\n      __typename\n    }\n    cities {\n      id\n      name\n      region {\n        id\n        name\n        slug\n        __typename\n      }\n      __typename\n    }\n    isCommentEnabled\n    noAdsense\n    variants {\n      id\n      hash\n      specifications {\n        specification {\n          codename\n          label\n          __typename\n        }\n        valueText\n        value\n        mediaUrl\n        __typename\n      }\n      price\n      oldPrice\n      pricePreview\n      oldPricePreview\n      quantity\n      __typename\n    }\n    showAnalytics\n    messengerLink\n    __typename\n  }\n}\n',
            }

            product_response = requests.post('https://api.ouedkniss.com/graphql', headers=product_headers, json=product_json_data)
            product_data = product_response.json()

            product_dict = {
            'id': product_data['data']['announcement']['id'],
            'title': product_data['data']['announcement']['title'],
            'price': product_data['data']['announcement']['price'],
            'specs_annee': None,
            'specs_car_engine': None,
            'specs_car_options': None,
            'specs_couleur_auto': None,
            'specs_papiers': None,
            'specs_kilometrage': None,
            'specs_marque-voiture': None,
            'specs_modele': None,
            'specs_transmission': None,
            }
            for i in range(0, 12):
                product_dict[f'option{i}'] = None
                
            product_dict['id'] = product_data['data']['announcement']['id']
            product_dict['title'] = product_data['data']['announcement']['title']
            product_dict['price'] = product_data['data']['announcement']['price']

            # Iterate through specifications and extract values based on labels
            for spec in product_data['data']['announcement']['specs']:
                label = spec['specification']['label']
                if label == 'Année':
                    product_dict['specs_annee'] = spec['valueText'][0]
                elif label == 'Moteur':
                    product_dict['specs_car_engine'] = spec['valueText'][0]
                elif label == 'Options':
                    product_dict['specs_car_options'] = spec['valueText'][0]
                elif label == 'Couleur':
                    product_dict['specs_couleur_auto'] = spec['valueText'][0]
                elif label == 'Papiers':
                    product_dict['specs_papiers'] = spec['valueText'][0]
                elif label == 'Kilométrage':
                    product_dict['specs_kilometrage'] = spec['valueText'][0]
                elif label == 'Marque':
                    product_dict['specs_marque-voiture'] = spec['valueText'][0]
                elif label == 'Modèle':
                    product_dict['specs_modele'] = spec['valueText'][0]
                elif label == 'Transmission':
                    product_dict['specs_transmission'] = spec['valueText'][0]
                elif label == 'Options de voiture':
                    option_values = spec['valueText']  # Assuming spec['valueText'] contains values corresponding to each option
                    for i, value in enumerate(option_values):
                        product_dict[f'option{i}'] = value
                           
            products_master_list.append(product_dict)
            df = pd.DataFrame(products_master_list)
            df.to_csv('cars_data_from_ouedkniss_csv.csv', index=False)
            df.to_excel('cars_data_from_ouedkniss_excel.xlsx', index=False)
        
        except Exception as e:
            print(f'error occurred: {e}')

           
