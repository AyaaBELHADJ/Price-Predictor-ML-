from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from joblib import load

model_path = r'C:\Users\LENOVO\Documents\Joblib\random_forest_model1.joblib'
try:
    model = load(model_path)
except FileNotFoundError:
    print(f"Model file not found at {model_path}")
    model = None

def engine_capacity_binf(score):
  
    if score <= 9:
        grade = 1
    elif score <= 18:
        grade = 2
    elif score <= 25:
        grade = 3
    return grade
   

def kilometrage_binf(score):
    
    if score <= 120000:
        grade = 1
    elif score <= 400000:
        grade = 2
    elif score <= 9999999:
        grade = 3
    return grade

# definition de mappings
COLOR_MAPPING = {
    'Gris': 4,
    'Noir': 7,
    'Blanc': 2,
    'Rouge': 10,
    'Autre': 0,
    'Vert': 11,
    'Jaune': 5,
    'Beige': 1,
    'Bleu': 3,
    'Marron': 6,
    'Orange': 8,
    'Violet': 12,
    'Rose': 9
}

PAPER_MAPPING = {
    'Carte grise / safia': 1,
    'Licence / Délai': 2,
    'Carte jaune': 3
}

brand_mapping = {
    'Dacia': 19,
    'Seat': 62,
    'Kia': 43,
    'Nissan': 54,
    'Volkswagen': 72,
    'Peugeot': 57,
    'Fiat': 26,
    'Renault': 59,
    'Chery': 12,
    'Great Wall': 30,
    'Citroen': 15,
    'Hyundai': 36,
    'Suzuki': 68,
    'Alfa Romeo': 0,
    'Chevrolet': 13,
    'Mercedes': 52,
    'BMW': 3,
    'DS': 18,
    'Toyota': 71,
    'Huanghai': 34,
    'Skoda': 63,
    'Daewoo': 20,
    'Other': 56,
    'Haima': 32,
    'Zotye': 75,
    'Audi': 2,
    'Gonow': 29,
    'Land Rover': 46,
    'DFSK': 17,
    'SsangYong': 66,
    'JAC': 39,
    'Ford': 27,
    'Lada': 44,
    'Chana': 9,
    'Opel': 55,
    'Baic': 5,
    'Honda': 33,
    'MG': 48,
    'Faw': 25,
    'Chrysler': 14,
    'DFM': 16,
    'Daihatsu': 21,
    'Hafei motors': 31,
    'Isuzu': 38,
    'Geely': 28,
    'Mazda': 51,
    'Lifan': 47,
    'Tata': 69,
    'Rover': 60,
    'Mitsubishi': 53,
    'Changan': 10,
    'Porsche': 58,
    'Aston Martin': 1,
    'Tesla': 70,
    'Brilliance': 6,
    'Maserati': 50,
    'Jaguar': 41,
    'Cadillac': 8,
    'Bugatti': 7,
    'IKCO': 37,
    'Jeep': 42,
    'BYD': 4,
    'Yamaha': 74,
    'Emgrand': 23,
    'JMC': 40,
    'Hummer': 35,
    'Mahindra': 49,
    'Subaru': 67,
    'Volvo': 73,
    'Lancia': 45,
    'Dodge': 22,
    'Smart': 64,
    'FOTON': 24,
    'Saipa': 61,
    'Sokon': 65,
    'Changhe': 11
}

engine_mapping = {
    'dci': 92,
    'missing': 95,
    'HDI': 45,
    'ess': 94,
    'TDI': 74,
    'VTI': 88,
    'VVT': 89,
    'Ecomotive': 35,
    'CH': 13,
    'VVTI': 90,
    'VM': 84,
    'MPI': 51,
    'CRDI': 14,
    'DSG': 27,
    'S90': 65,
    'DDTI': 23,
    'CVVT': 17,
    'CDI': 10,
    'S': 62,
    'CV': 15,
    'GTI': 43,
    'BVA': 5,
    'Turbo': 78,
    'E-XDI': 31,
    'DDI': 22,
    'GT': 41,
    'VCDI': 82,
    '4MATIC': 0,
    'DTR': 29,
    'Quattro': 59,
    'HTP': 49,
    'STD': 69,
    'Diesel': 30,
    'Matic': 54,
    'S-tronic': 64,
    'D4D': 21,
    'PureTech': 58,
    'TDI177': 75,
    'TCE': 71,
    'TFSI': 76,
    'tsi': 96,
    'SE': 67,
    'V8': 81,
    'GPL': 40,
    'DSG6': 28,
    'SR': 68,
    'D4': 20,
    'AMG': 3,
    'TD': 73,
    'VCT': 83,
    'TCI': 72,
    'CGI': 12,
    'GTS': 44,
    'Hybrid': 50,
    'PDK': 57,
    'MZR': 53,
    'V6': 80,
    'ACC': 2,
    'D-CVVT': 19,
    'CDTI': 11,
    'CVT': 16,
    '4WD': 1,
    'TS': 77,
    'Om': 56,
    'FR': 37,
    'GTD': 42,
    'DOHC': 26,
    'HT': 48,
    'Supercharged': 70,
    'Mjet': 55,
    'VTEC': 87,
    'GDI': 39,
    'EFI': 32,
    'HSE': 47,
    'DLX': 25,
    'BlueMotion': 8,
    'EcoBoost': 33,
    'XLI': 91,
    'Common Rail': 18,
    'AWD': 4,
    'RS': 61,
    'FSI': 38,
    'VMAX': 85,
    'CD': 9,
    'SCe': 66,
    'HLBMT': 46,
    'MT': 52,
    'BVM': 6,
    'eTorque': 93,
    'S&S': 63,
    'FAP': 36,
    'R-Line': 60,
    'BlueHDi': 7,
    'V12': 79,
    'VT': 86,
    'EcoTec': 34,
    'DI-D': 24
}

finition_mapping = {
"Stepway": 3733,
    "Ex": 1735,
    "nan": 4564,
    "Brésilien": 966,
    "Allure": 675,
    "Cité plus": 1218,
    "Expression": 1765,
    "Confort": 1340,
    "301": 372,
    "Golf 7": 2118,
    "Kangoo": 2433,
    "Transporter": 3998,
    "T4": 3828,
    "Symbol": 3795,
    "QQ": 3222,
    "505": 476,
    "Edition 30": 1677,
    "Brava": 956,
    "EX": 1655,
    "Tucson": 4034,
    "Maruti 800": 2755,
    "Swift": 3789,
    "القديمة": 4765,
    "MEGANE": 2719,
    "Fully": 1973,
    "GT-Line": 2042,
    "R line": 3251,
    "Sport Edition": 3671,
    "Double Cabine": 1562,
    "FR": 1807,
    "Série 5": 3809,
"Restylée": 3354,
    "Authentique": 744,
    "Star plus": 3718,
    "C4": 1039,
    "Patrol Long": 3067,
    "Collection": 1309,
    "Yaris": 4259,
    "Megane 2": 2779,
    "F1": 1795,
    "Tepee Allure": 3904,
    "Privilege": 3160,
    "Tikreud": 3936,
    "GT Line +": 2033,
    "Gtd": 2178,
    "FR+15": 1820,
    "Toute options": 3984,
    "City": 1203,
    "Ambiente": 704,
    "Duster": 1589,
    "Cielo": 1187,
    "GLS": 2004,
    "Chevrolet epica": 1177,
    "Origin": 3001,
    "Megane 1": 2777,
    "Bye bye": 991,
    "206 Plus": 298,
    "Alto": 693,
    "Lite Ls": 2661,
    "Nomad 2": 2936,
    "GTi": 2066,
    "Caddy": 1102,
    "S Line": 3423,
    "GL Plus": 1995,
    "Optra 5 portes": 2994,
    "Cup": 1415,
    "Megane 3": 2783,
    "Extrême": 1787,
    "La tt": 2566,
    "D": 1432,
    "جتيلاين": 4824,
    "Range Sport": 3323,
    "208": 310,
    "Restylée DZ": 3355,
    "308": 382,
    "Tepee": 3902,
    "Octavia": 2972,
    "New QQ": 2903,
    "307": 379,
    "مدال جديد": 4967,
    "Leon": 2613,
    "Commercial": 1322,
    "S Line Pack Tech": 3426,
    "Pickup": 3085,
    "Carat": 1122,
    "Classe E": 1236,
    "Elegance 4x4": 1689,
    "اصلية": 4742,
    "R Line": 3238,
    "GT Line": 2031,
    "Celerio": 1150,
    "25": 334,
    "Romania": 3395,
    "Exclusive": 1749,
    "Loca": 2666,
    "Polo": 3105,
    "Passat": 3058,
    "Sportline": 3700,
    "SC 2m30": 3473,
    "Confortline": 1348,
    "LT": 2504,
    "Line sport": 2650,
    "Clio 3": 1259,
    "Allure Facelift": 680,
    "Monte Carlo": 2841,
    "Sparco 7 rapport": 3659,
    "عطاوني 70": 4899,
    "Gti": 2183,
    "Laguna 1": 2581,
    "GL+": 1996,
    "GTI": 2053,
    "Titanium": 3947,
    "Limited": 2641,
    "Sail 4 portes": 3523,
    "Dynamique": 1596,
    "Styl": 3757,
    "نيفادة": 4993,
    "Niva": 2927,
    "Berlingo": 851,
    "Ibiza fr plus": 2311,
    "Biper": 870,
    "Optra 4 portes": 2993,
    "STD": 3500,
    "قديمة": 4918,
    "Prevelage": 3145,
    "i10 Plus": 4491,
    "Clio Campus": 1276,
    "206": 295,
    "Solenza": 3647,
    "406": 435,
    "K10": 2414,
    "Start+": 3727,
    "Combi Startline": 1313,
    "Style": 3758,
    "Suzuki Grand Vitara 4x4": 3786,
    "Tdi": 3876,
    "Xsara": 4253,
    "Actyon": 646,
    "Dynamique 5 Portes": 1600,
    "New Spark": 2905,
    "Access": 622,
    "Life": 2621,
    "Limited 2": 2643,
    "Clever": 1248,
    "Tiguan": 3932,
    "Aveo 5 portes": 769,
    "Logan": 2669,
    "Lauréate": 2605,
    "AVANTGARDE Pack AMG": 605,
    "تم": 4815,
    "GTD": 2044,
    "Fr Beats": 1937,
    "بارتنار": 4781,
    "Extrem": 1776,
    "R-Line": 3260,
    "Cruze": 1402,
    "45 AMG Pack Exclusif": 443,
    "Corsa": 1366,
    "Extrem": 1776,
    "R-Line": 3260,
    "Cruze": 1402,
    "45 AMG Pack Exclusif": 443,
    "Corsa": 1366,
    "4": 406,
    "Ambiance": 703,
    "Laureate": 2601,
    "JOIN": 2375,
    "Serie 2 A": 3592,
    "Active": 635,
    "MILADI (Extrême)": 2722,
    "Mini Truck Double Cabine": 2810,
    "High Facelift": 2264,
    "Altrak": 698,
    "Civic": 1221,
    "Made In Bladi": 2738,
    "golf7 Rline": 4463,
    "Sandero": 3531,
    "Sorento": 3651,
    "Deluxe": 1481,
    "Alour": 689,
    "C5 AIRCROSS": 1045,
    "C3": 1032,
    "Korando": 2455,
    "Gt": 2162,
    "Match": 2758,
    "Origin VU": 3002,
    "Rio 5 portes": 3372,
    "Clio 1": 1255,
    "CL": 1071,
    "Vitamine": 4147,
    "Symbole": 3798,
    "LTZ": 2508,
    "Hilux": 2280,
    "Fresh": 1956,
    "Gtl": 2187,
    "Golf 5": 2115,
    "Astra": 729,
    "Privilège plus": 3165,
    "Freelander 2": 1953,
    "L3H2": 2480,
    "LX": 2514,
    "Spark": 3660,
    "Besnice": 859,
    "i10": 4490,
    "Ambition": 705,
    "Sail 5 portes": 3524,
    "Laguna 2": 2582,
}

def estimate_vehicle(features):
    # Check if any feature is None
           if any(feature is None for feature in features.values()):
             return "Error: Missing feature(s)"

    # Check if horsepower and capacity are not None and not zero
             cheval_vapeur = features.get('cheval_vapeur')
             capacite = features.get('capacite')
           if cheval_vapeur is None or capacite is None:
              return "Error: Horsepower or capacity is missing"
           if cheval_vapeur == 0 or capacite == 0:
              return "Error: Horsepower or capacity cannot be zero"

   
              HorsPowerParCapacite = cheval_vapeur / capacite

    # Make prediction using the model
              prediction = model.predict(features)[0]
              return prediction


@csrf_exempt
def estimer_vehicule(request):
    if request.method == 'POST':
     
            data = json.loads(request.body)

#Extract the data from the request
            
            marque = data.get('marque')
            modele = data.get('modele')
            annee = int(data.get('annee'))
            energie = data.get('energie')
            kilometrage = data.get('kilometrage')
            boite = data.get('boite')
            capacite = data.get('capacite')
            couleur = data.get('couleur')
            finition = data.get('finition')
            moteur = data.get('Type du moteur')
            papiers = data.get('papiers')
            cheval_vapeur = data.get('Cheval-Vapeur')
            options = data.get('options', [])
            

            couleur_code = COLOR_MAPPING.get(couleur, 0)
            papiers_code = PAPER_MAPPING.get(papiers, -1)
            marque_code = brand_mapping.get(marque, 56)
            engine_code = engine_mapping.get(moteur, 95)
            finition_code = finition_mapping.get(finition,-1)
            CarAge = 2025 - annee
            HorsPowerParCapacite = cheval_vapeur/capacite
            CapaciteParAge = capacite/CarAge
            KilometrageParAnnee = kilometrage/CarAge

            engine_capacity_bin = engine_capacity_binf(capacite)

            kilometrage_bin = kilometrage_binf(kilometrage)
            kilometrage_par_annee_bin = kilometrage
            Min_price_par_bin = 330.05
            Min_price_par_kilometre = Min_price_par_bin/kilometrage
            Min_price2_par_kilometre =(Min_price_par_bin) **2 / kilometrage
            titre = marque + modele + finition 
            engine = capacite + moteur + cheval_vapeur
             # features = [annee, couleur, papiers, kilometrage, marque, modele, finition, 2, capacite, moteur, cheval_vapeur, titre, engine, CarAge, engine_capacity_bin, kilometrage_bin,HorsPowerParCapacite, CapaciteParAge, KilometrageParAnnee, kilometrage_par_annee_bin,Min_price_par_bin, Min_price_par_kilometre, Min_price2_par_kilometre]
          #Convertir en format approprié 
            #features = np.array(features).reshape(1, -1)
          #Faire la prédiction
            #estimation = model.predict(features)[0]
            
            #features = [data['annee'], data['couleur'],data['papiers'],data['kilometrage'],data['marque'],data['modele'],data['finition'],1,data['capacite'],data['moteur'],data['cheval_vapeur'],data['titre'],data['aengine'],data['CarAge'],data['engine_capacity_bin'],data['kilometrage_bin'],data['HorsPowerParCapacite'],data['CapaciteParAge'],data['kilometrage_par_annee'],data['kilometrage_par_annee_bin'],data['Min_price_par_bin'],data['Min_price_par_kilometre'],data['Min_price2_par_kilometre']]  
         

          # Faire la prédiction
            #prediction = model.predict(features)[0]

            # Renvoyer la prédiction
            #estimation  = {'prediction': prediction}

            
            #return JsonResponse({'estimation': estimation, 'couleur_code': couleur_code, 'papiers_code': papiers_code, 
           # 'marque_code': marque_code, 'engine_code':engine_code,'finition_code': finition_code })

       
           # Simuler une estimation 
            estimation = 25000000  # Exemple d'estimations

            return JsonResponse({'estimation': estimation})
    else:
            return JsonResponse({'error': 'Invalid request method'}, status=400)
