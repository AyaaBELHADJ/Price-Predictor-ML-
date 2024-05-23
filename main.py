import requests   #send the API request
import pandas as pd #put final data into csv form

products_master_list = []
START_PAGE = 64
END_PAGE = 100

category_headers = {     #got from converting CURL to a python code
        'accept': '*/*',
        'accept-language': 'fr',
        'authorization': '',
        'content-type': 'application/json',
        'locale': 'fr',
        'origin': 'https://www.ouedkniss.com',
        'priority': 'u=1, i',
        'referer': 'https://www.ouedkniss.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-app-version': '"3.0.22"',
        'x-referer': 'https://www.ouedkniss.com/automobiles/1',
        'x-track-id': 'c066a1ca-c084-46ed-97ad-08c214c773cf',
        'x-track-timestamp': '1716413595',
    }

product_headers = {
    'accept': '*/*',
    'accept-language': 'fr',
    'authorization': '',
    'content-type': 'application/json',
    'locale': 'fr',
    'origin': 'https://www.ouedkniss.com',
    'priority': 'u=1, i',
    'referer': 'https://www.ouedkniss.com/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-app-version': '"3.0.22"',
    'x-referer': 'https://www.ouedkniss.com/citadine-renault-clio-4-2018-gt-line-medea-algerie-d41635254',
    'x-track-id': 'c066a1ca-c084-46ed-97ad-08c214c773cf',
    'x-track-timestamp': '1716413595',
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
    list_data = response.json() #list_data is a dictionary that holds the json response


    product_ids_with_price = []  #a list  to put ids inside
    
    #we will get the ids of cars using list_data
    #product is also a dictionary
    #get to get info from dictionary , append to insert into the dictionary
    
    
    for product in list_data['data']['search']['announcements']['data']:
        if product.get('price') is not None:  # Check if product has price
            product_ids_with_price.append(product['id'])
    print(f'Number of cars with price found on the page: {len(product_ids_with_price)}')

    ### loop through the product ids
    #basically, we iterated the list_data
    ### get the product data
    #we will get the info of the car using the id
    
    for product_index, product_id in enumerate(product_ids_with_price): #product index to give us the number of the page while scrapping 
        
        print(f'product_index: {product_index}, product_id: {product_id}')
        
        try: 
            #if an exception happens, we print a message e and skip to the next product 
            #( thats why we put it inside for, it happens after every id iteration)

            product_json_data = {
                'operationName': 'AnnouncementGet',
                'variables': {
                    'id': product_id,
                },
                'query': 'query AnnouncementGet($id: ID!) {\n  announcement: announcementDetails(id: $id) {\n    id\n    reference\n    title\n    slug\n    description\n    orderExternalUrl\n    createdAt: refreshedAt\n    price\n    pricePreview\n    oldPrice\n    oldPricePreview\n    priceType\n    exchangeType\n    priceUnit\n    hasDelivery\n    deliveryType\n    hasPhone\n    hasEmail\n    quantity\n    status\n    street_name\n    category {\n      id\n      slug\n      name\n      deliveryType\n      __typename\n    }\n    defaultMedia(size: ORIGINAL) {\n      mediaUrl\n      __typename\n    }\n    medias(size: LARGE) {\n      mediaUrl\n      mimeType\n      thumbnail\n      __typename\n    }\n    categories {\n      id\n      name\n      slug\n      parentId\n      __typename\n    }\n    specs {\n      specification {\n        label\n        codename\n        type\n        __typename\n      }\n      value\n      valueText\n      __typename\n    }\n    user {\n      id\n      username\n      displayName\n      avatarUrl\n      __typename\n    }\n    isFromStore\n    store {\n      id\n      name\n      slug\n      description\n      imageUrl\n      url\n      followerCount\n      announcementsCount\n      locations {\n        location {\n          address\n          region {\n            slug\n            name\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      categories {\n        name\n        slug\n        __typename\n      }\n      __typename\n    }\n    cities {\n      id\n      name\n      region {\n        id\n        name\n        slug\n        __typename\n      }\n      __typename\n    }\n    isCommentEnabled\n    noAdsense\n    variants {\n      id\n      hash\n      specifications {\n        specification {\n          codename\n          label\n          __typename\n        }\n        valueText\n        value\n        mediaUrl\n        __typename\n      }\n      price\n      oldPrice\n      pricePreview\n      oldPricePreview\n      quantity\n      __typename\n    }\n    showAnalytics\n    messengerLink\n    __typename\n  }\n}\n',
            }#$id: ID!  means the id should not be null, incase it is we throw the exception

            product_response = requests.post('https://api.ouedkniss.com/graphql', headers=product_headers, json=product_json_data)
            product_data = product_response.json()  #is a dictionary that holds the response in a json format

            product_dict = {
            'id': product_data['data']['announcement']['id'],
            'title': product_data['data']['announcement']['title'],
            'price': product_data['data']['announcement']['price'],
            'specs_annee': None,
            'specs_car_engine': None, 
            'specs_couleur_auto': None,
            'specs_papiers': None,   #it's better to define them outside the dic 
            'specs_kilometrage': None,
            'specs_marque-voiture': None,
            'specs_modele': None,
            'specs_finition' :None,
            'specs_energie' :None,
            'specs_boite' :None,
            }
            for i in range(0, 12):  #give every option a collumn in the dictionary
                product_dict[f'option{i}'] = None

            #fill the dic :
            #after checking the structure of ouedkniss we found out that all these infos are inside the spec tag
            #exactly inside an indexed list 
            #we thaught about using a dynamic way :
            #product_dictionary['marque] = product_dict['data']['announcment']['spec'][1]
            #but the order of the specifications change from a product to another
            # Iterate through specifications and extract values based on labels
            
            for spec in product_data['data']['announcement']['specs']:
                
                #spec refers to the tag that contains the list of specifications
                 # Map the label to the corresponding key in the product dictionary
                 
                label = spec['specification']['label']   
                
                if label == 'Année':
                    product_dict['specs_annee'] = spec['valueText'][0] 
                elif label == 'Moteur':
                    product_dict['specs_car_engine'] = spec['valueText'][0] 
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
                elif label =='Finition':
                    product_dict['specs_finition'] = spec['valueText'][0]
                elif label =='Energie':
                    product_data['specs_energie'] = spec['valueText'][0]
                elif label =='Boite':
                    product_data['specs_boite'] = spec['valueText'][0]
                elif label == 'Options de voiture':
                    option_values = spec['valueText'] 
                    for i, value in enumerate(option_values):
                        product_dict[f'option{i}'] = value
                           
            products_master_list.append(product_dict)
             
            #after every iteration of the product , we will append 
            #it inside the predefined products_master_list list (used to store the resulted dictionaries)
            
            df = pd.DataFrame(products_master_list)
            df.to_csv('cars_data_from_ouedkniss_csv.csv', index=True)
           
        
        except Exception as e:   #in every page iteration, when an exception happens inside try : , we send a message,  and we continue scraping
            print(f'error occurred: {e}')

