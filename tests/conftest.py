import pytest
from dataclasses import dataclass, field
from specification import (
    AttributeSpecification,
    AndSpecification,
    OrSpecification,
    NotSpecification
)

gearbox = {
    "type": "sequential",
    "gears": [

    ]
}


@dataclass
class Transport:
    model: str
    speed: int
    gearbox: dict = field(default_factory=lambda x: dict)


class Car(Transport):
    pass


class Moto(Transport):
    pass


@pytest.fixture()
def test_transports():
    transports = [
        Car("tesla", 300, gearbox),
        Car("zhiguli", 120, gearbox),
        Moto("jupiter", 90, gearbox),
        Moto("harley", 90, {
            "type": "dog_box",
            "gears": [
                {"first": {"min": 100, "max": 300}},
                {"second": {"min": 300, "max": 1000}},
            ]
        }),

        # Looking for:
        Moto("bmw", 190, gearbox),
        Moto("bmw", 210, gearbox),
        Car("bmw", 220, gearbox),
    ]
    return transports


@pytest.fixture()
def test_spec():
    bmw_or_harley_transport_over_80_spec = AndSpecification(
        AttributeSpecification("speed", "gt", 80),
        OrSpecification(
            AttributeSpecification("model", "eq", "bmw"),
            AttributeSpecification("model", "eq", "harley"),
        ),
        AttributeSpecification("gearbox.type", "in", ["dog_box", "sequential"]),

        # Same as AttributeSpecification("gearbox.gears.second.max", "ne", 1000)
        NotSpecification(
            OrSpecification(
                AttributeSpecification("gearbox.gears.second.max", "eq", 1000)
            )
        ),
    )
    return bmw_or_harley_transport_over_80_spec


@dataclass
class Buyer:
    full_name: str
    age: int
    telephone: str


@dataclass
class Order:
    car: str
    vin: int
    price: int
    max_speed: int
    power: int
    buyer: Buyer


# @pytest.fixture()
# def test_mimesis(n=100):
#     from mimesis import Transport, Finance, Person, random
#     """
#     class mimesis.Transport(*args, **kwargs)
#         manufacturer()
#         vehicle_registration_code(locale=None)
#
#     class mimesis.Finance(*args, **kwargs)
#         price(minimum=500, maximum=1500)
#
#     class mimesis.Person(*args, **kwargs)
#         age(minimum=16, maximum=66)
#         full_name(gender=None, reverse=False)
#         telephone(mask='', placeholder='#')
#     """
#     trans = Transport(locale='ru')
#     finance = Finance(locale='ru')
#     person = Person(locale='ru')
#     rand = random.Random()
#
#     orders_list = list()
#     for _ in range(0, n):
#         car = trans.manufacturer()
#         vin = int(rand.custom_code(mask="#" * 17))
#         max_speed = rand.randint(a=80, b=300)
#         power = rand.randint(a=10, b=1000)
#
#         price = int(finance.price(minimum=10000, maximum=50000))
#
#         full_name = person.full_name()
#         age = person.age(minimum=18)
#         telephone = person.telephone("+7(9##)###-##-##")
#         order = Order(
#             car,
#             vin,
#             price,
#             max_speed,
#             power,
#             Buyer(full_name, age, telephone)
#         )
#         orders_list.append(order)
#         print()
#     return orders_list


""" 
(Jeep OR Subaru) AND price>10000 AND max_speed>230
"""
specification_jeep_and_subaru_price_10000_230 = AndSpecification(
    OrSpecification(
        AttributeSpecification("car", "eq", "Jeep"),
        AttributeSpecification("car", "eq", "Subaru"),
    ),
    AttributeSpecification("price", "gt", 10000),
    AttributeSpecification("max_speed", "gt", 230),

)

""" 
(Jeep price>=48000) OR (Subaru power>=840)
"""
specification_jeep_price_48000_and_subaru_power_230 = OrSpecification(
    AndSpecification(
        AttributeSpecification("car", "eq", "Jeep"),
        AttributeSpecification("price", "ge", 48000)
    ),
    AndSpecification(
        AttributeSpecification("car", "eq", "Subaru"),
        AttributeSpecification("power", "ge", 840)
    )
)

""" 
Audi NOT power>900
"""
specification_audi_not_power_900 = AndSpecification(
    AttributeSpecification("car", "eq", "Audi"),
    NotSpecification(
        AttributeSpecification("power", "gt", "900")
    )
)

"""
Daewoo AND Bmw
"""
specification_daewoo_bmw = AndSpecification(
    OrSpecification(
        AttributeSpecification("car", "eq", "Daewoo"),
        AttributeSpecification("car", "eq", "Bmw"),
    ),
)

"""
age = 18 AND (car Lamborghini OR car Bmw)
"""
specification_age_18 = AndSpecification(
    AttributeSpecification("buyer.age", "eq", 18),
    OrSpecification(
        AttributeSpecification("car", "eq", "Lamborghini"),
        AttributeSpecification("car", "eq", "Bmw"),
    ),
)

"""
generated_data randomly generated 
"""
generated_data = [Order(car='Maserati', vin=87451386981840811, price=47730, max_speed=168, power=922,
                        buyer=Buyer(full_name='Марианна Олейникова', age=20, telephone='+7(997)118-92-76')),
                  Order(car='Chevrolet', vin=94080768105561902, price=40641, max_speed=160, power=217,
                   buyer=Buyer(full_name='Флориана Девяткина', age=28, telephone='+7(963)708-69-14')),
                  Order(car='DS', vin=56741022834084974, price=23836, max_speed=209, power=137,
                   buyer=Buyer(full_name='Жансая Алфимова', age=42, telephone='+7(938)867-04-58')),
                  Order(car='MG', vin=21914452603945993, price=14726, max_speed=262, power=831,
                   buyer=Buyer(full_name='Эраст Пивоваров', age=49, telephone='+7(947)708-61-04')),
                  Order(car='Subaru', vin=19419143852557674, price=49186, max_speed=265, power=841,
                   buyer=Buyer(full_name='Серафима Изосимова', age=38, telephone='+7(913)093-32-60')),
                  Order(car='Seat', vin=29653152494954891, price=31510, max_speed=143, power=675,
                   buyer=Buyer(full_name='Андрей Казакевич', age=51, telephone='+7(911)057-87-39')),
                  Order(car='Audi', vin=1573108778233139, price=23499, max_speed=237, power=144,
                   buyer=Buyer(full_name='Мавлюда Ивонова', age=29, telephone='+7(995)001-61-20')),
                  Order(car='Dacia', vin=4517077067136953, price=48038, max_speed=260, power=616,
                   buyer=Buyer(full_name='Мелентий Малецкий', age=54, telephone='+7(972)581-02-86')),
                  Order(car='Lexus', vin=86788120968329453, price=15269, max_speed=202, power=336,
                   buyer=Buyer(full_name='Тамара Балкова', age=24, telephone='+7(950)236-03-16')),
                  Order(car='Honda', vin=74683211158364420, price=35316, max_speed=207, power=439,
                   buyer=Buyer(full_name='Архипп Сударушкин', age=41, telephone='+7(915)570-82-54')),
                  Order(car='Morgan', vin=21933807156882684, price=23821, max_speed=283, power=327,
                   buyer=Buyer(full_name='Эсмеральда Захарова', age=30, telephone='+7(945)174-26-80')),
                  Order(car='Landwind', vin=1468609519868593, price=17185, max_speed=208, power=289,
                   buyer=Buyer(full_name='Венедикт Бессараб', age=57, telephone='+7(989)441-74-55')),
                  Order(car='Audi', vin=40813570994967359, price=19720, max_speed=271, power=249,
                   buyer=Buyer(full_name='Артемий Казимиров', age=23, telephone='+7(986)430-37-61')),
                  Order(car='Cadillac', vin=90607453354675681, price=29107, max_speed=272, power=801,
                   buyer=Buyer(full_name='Мина Грунина', age=27, telephone='+7(967)378-34-29')),
                  Order(car='Abarth', vin=83944490248983501, price=17336, max_speed=213, power=979,
                   buyer=Buyer(full_name='Роза Смородинская', age=23, telephone='+7(986)152-34-80')),
                  Order(car='Abarth', vin=70496127499372867, price=28139, max_speed=292, power=712,
                   buyer=Buyer(full_name='Семён Кривомазов', age=44, telephone='+7(900)247-56-71')),
                  Order(car='Jeep', vin=63575861943466906, price=48178, max_speed=137, power=171,
                   buyer=Buyer(full_name='Геласий Мирошников', age=29, telephone='+7(994)110-09-16')),
                  Order(car='Jeep', vin=3326129605236063, price=10180, max_speed=250, power=767,
                   buyer=Buyer(full_name='Фёкла Казанцева', age=43, telephone='+7(996)171-14-50')),
                  Order(car='Honda', vin=73811472366418973, price=11429, max_speed=253, power=250,
                   buyer=Buyer(full_name='Далида Лагина', age=44, telephone='+7(944)369-26-22')),
                  Order(car='SsangYong', vin=11775394201886094, price=49886, max_speed=197, power=624,
                   buyer=Buyer(full_name='Лаура Карагодина', age=66, telephone='+7(965)914-48-19')),
                  Order(car='Mercedes-Benz', vin=78009962533776793, price=44975, max_speed=249, power=526,
                   buyer=Buyer(full_name='Ария Анисимова', age=42, telephone='+7(928)520-98-84')),
                  Order(car='Chevrolet', vin=50323133256057175, price=12207, max_speed=245, power=788,
                   buyer=Buyer(full_name='Капитон Герасимов', age=38, telephone='+7(973)425-03-42')),
                  Order(car='KTM', vin=87310788991997992, price=28728, max_speed=276, power=184,
                   buyer=Buyer(full_name='Лили Жемчужникова', age=45, telephone='+7(971)726-00-05')),
                  Order(car='Infiniti', vin=80762709322938844, price=22706, max_speed=257, power=407,
                   buyer=Buyer(full_name='Жозефина Серова', age=56, telephone='+7(901)445-16-23')),
                  Order(car='Hummer', vin=45300332099999250, price=13181, max_speed=98, power=546,
                   buyer=Buyer(full_name='Айгерим Мартемьянова', age=36, telephone='+7(948)609-40-00')),
                  Order(car='Kia', vin=50070971744073889, price=41809, max_speed=252, power=937,
                   buyer=Buyer(full_name='Амира Быкова', age=60, telephone='+7(914)815-47-25')),
                  Order(car='Peugeot', vin=75716366748602560, price=34514, max_speed=240, power=306,
                   buyer=Buyer(full_name='Ника Лаврентьева', age=44, telephone='+7(950)609-24-77')),
                  Order(car='Bugatti', vin=99464376753073081, price=17011, max_speed=269, power=134,
                   buyer=Buyer(full_name='Святополк Слепнёв', age=39, telephone='+7(921)725-93-73')),
                  Order(car='Chrysler', vin=81486426823352928, price=41468, max_speed=180, power=263,
                   buyer=Buyer(full_name='Севастьян Афанасов', age=56, telephone='+7(901)874-90-70')),
                  Order(car='Landwind', vin=67661241440516425, price=25425, max_speed=90, power=888,
                   buyer=Buyer(full_name='Лора Евтихеева', age=62, telephone='+7(941)317-16-96')),
                  Order(car='Cadillac', vin=48160987654355349, price=38956, max_speed=272, power=875,
                   buyer=Buyer(full_name='Айнагуль Ганичева', age=30, telephone='+7(970)580-21-56')),
                  Order(car='Subaru', vin=6592654160762964, price=24731, max_speed=228, power=895,
                   buyer=Buyer(full_name='Роза Арбузова', age=65, telephone='+7(950)789-59-22')),
                  Order(car='Donkervoort', vin=93243716185825541, price=27003, max_speed=131, power=980,
                   buyer=Buyer(full_name='Олег Парфеньев', age=41, telephone='+7(929)019-96-00')),
                  Order(car='Bugatti', vin=80586458759998786, price=36021, max_speed=188, power=497,
                   buyer=Buyer(full_name='Мирослав Воронов', age=55, telephone='+7(948)518-34-88')),
                  Order(car='Iveco', vin=58919132031365609, price=35401, max_speed=254, power=74,
                   buyer=Buyer(full_name='Ростислав Пименов', age=21, telephone='+7(937)959-77-91')),
                  Order(car='Daihatsu', vin=43684848127909700, price=20414, max_speed=161, power=723,
                   buyer=Buyer(full_name='Фока Бацкалевич', age=46, telephone='+7(993)154-97-77')),
                  Order(car='Chrysler', vin=76285804399875561, price=26177, max_speed=278, power=341,
                   buyer=Buyer(full_name='Герасим Афанасьев', age=38, telephone='+7(947)480-12-97')),
                  Order(car='Mercedes-Benz', vin=27695010116126353, price=39866, max_speed=266, power=703,
                   buyer=Buyer(full_name='Елена Виноградова', age=52, telephone='+7(919)597-71-75')),
                  Order(car='Seat', vin=10837486764095036, price=24293, max_speed=212, power=696,
                   buyer=Buyer(full_name='Софья Фионина', age=41, telephone='+7(928)786-94-70')),
                  Order(car='Lotus', vin=36799784137382509, price=12350, max_speed=119, power=440,
                   buyer=Buyer(full_name='Афанасий Есенин', age=56, telephone='+7(934)467-18-69')),
                  Order(car='Bugatti', vin=42303268173827900, price=29394, max_speed=149, power=748,
                   buyer=Buyer(full_name='Бажена Новосельцева', age=62, telephone='+7(906)731-79-50')),
                  Order(car='Hyundai', vin=76015319136667706, price=15915, max_speed=189, power=761,
                   buyer=Buyer(full_name='Фома Заволокин', age=26, telephone='+7(906)611-57-18')),
                  Order(car='Maybach', vin=6876383125965285, price=43483, max_speed=211, power=830,
                   buyer=Buyer(full_name='Феликс Позамантир', age=59, telephone='+7(988)906-83-99')),
                  Order(car='Rolls-Royce', vin=21765200114217714, price=33707, max_speed=257, power=635,
                   buyer=Buyer(full_name='Мелентий Ольбик', age=54, telephone='+7(935)254-64-37')),
                  Order(car='Volkswagen', vin=88903503481227489, price=47620, max_speed=286, power=514,
                   buyer=Buyer(full_name='Сальма Ерофеева', age=53, telephone='+7(926)606-25-89')),
                  Order(car='Dacia', vin=38171086038624432, price=45718, max_speed=198, power=314,
                   buyer=Buyer(full_name='Ефим Хрисогонов', age=34, telephone='+7(992)597-87-71')),
                  Order(car='Jaguar', vin=19134631231011633, price=25252, max_speed=236, power=840,
                   buyer=Buyer(full_name='Белинда Памфилова', age=21, telephone='+7(974)939-11-50')),
                  Order(car='Landwind', vin=55635254849200471, price=32430, max_speed=174, power=34,
                   buyer=Buyer(full_name='Белинда Золотцева', age=61, telephone='+7(904)231-76-94')),
                  Order(car='Honda', vin=12078181403436686, price=33428, max_speed=194, power=785,
                   buyer=Buyer(full_name='Рената Михеева', age=35, telephone='+7(991)625-03-06')),
                  Order(car='Audi', vin=92943043210343979, price=24896, max_speed=173, power=716,
                   buyer=Buyer(full_name='Ираклий Патрикеев', age=21, telephone='+7(913)529-96-88')),
                  Order(car='Audi', vin=49850764408362096, price=35825, max_speed=251, power=574,
                   buyer=Buyer(full_name='Лика Багринцева', age=50, telephone='+7(960)806-99-75')),
                  Order(car='Hyundai', vin=56150352166552617, price=42503, max_speed=204, power=296,
                   buyer=Buyer(full_name='Поликарп Платов', age=50, telephone='+7(910)036-66-94')),
                  Order(car='Chrysler', vin=61936340343464557, price=43912, max_speed=114, power=941,
                   buyer=Buyer(full_name='Анфим Евменов', age=56, telephone='+7(958)021-91-69')),
                  Order(car='Audi', vin=72329768969115621, price=48232, max_speed=162, power=943,
                   buyer=Buyer(full_name='Ника Казанцева', age=56, telephone='+7(957)491-19-46')),
                  Order(car='KTM', vin=18674948105058389, price=28576, max_speed=218, power=442,
                   buyer=Buyer(full_name='Юстин Агутин', age=40, telephone='+7(977)149-90-15')),
                  Order(car='Maserati', vin=39121996402662071, price=23175, max_speed=94, power=880,
                   buyer=Buyer(full_name='Амира Прошина', age=24, telephone='+7(906)673-40-38')),
                  Order(car='Smart', vin=39620328929313715, price=20675, max_speed=270, power=547,
                   buyer=Buyer(full_name='Иннокентий Василов', age=46, telephone='+7(934)368-36-94')),
                  Order(car='Jaguar', vin=64406734729318335, price=46524, max_speed=264, power=873,
                   buyer=Buyer(full_name='Милада Гермогенова', age=19, telephone='+7(956)092-80-01')),
                  Order(car='Volvo', vin=79988410591990467, price=21017, max_speed=145, power=852,
                   buyer=Buyer(full_name='Раиса Макина', age=47, telephone='+7(954)183-88-70')),
                  Order(car='Toyota', vin=87722005250456790, price=15776, max_speed=247, power=554,
                   buyer=Buyer(full_name='Филимон Банников', age=56, telephone='+7(970)699-06-04')),
                  Order(car='Aston Martin', vin=99190093820726528, price=16789, max_speed=253, power=911,
                   buyer=Buyer(full_name='Жозефина Максимушкина', age=37, telephone='+7(903)829-87-24')),
                  Order(car='Dodge', vin=48015454322183484, price=46293, max_speed=118, power=686,
                   buyer=Buyer(full_name='Илина Пермякова', age=60, telephone='+7(917)109-75-32')),
                  Order(car='Daewoo', vin=95056458578058897, price=28853, max_speed=199, power=26,
                   buyer=Buyer(full_name='Аркадий Левонов', age=33, telephone='+7(937)651-19-74')),
                  Order(car='Mercedes-Benz', vin=68023430263724271, price=45454, max_speed=111, power=373,
                   buyer=Buyer(full_name='Ава Обухова', age=18, telephone='+7(958)780-50-74')),
                  Order(car='Nissan', vin=71813548458032291, price=34392, max_speed=299, power=581,
                   buyer=Buyer(full_name='Мстислав Демидов', age=58, telephone='+7(958)025-94-48')),
                  Order(car='Chrysler', vin=45094713610798296, price=36382, max_speed=288, power=986,
                   buyer=Buyer(full_name='Гульназ Евсюкова', age=18, telephone='+7(915)562-24-11')),
                  Order(car='Landwind', vin=33584988237659876, price=13189, max_speed=240, power=92,
                   buyer=Buyer(full_name='Варсонофий Феонин', age=26, telephone='+7(962)955-35-08')),
                  Order(car='KTM', vin=84844191929518185, price=26123, max_speed=124, power=582,
                   buyer=Buyer(full_name='Антонин Гогуа', age=61, telephone='+7(981)875-56-77')),
                  Order(car='MG', vin=48636403672768350, price=23070, max_speed=111, power=858,
                   buyer=Buyer(full_name='Геласий Носов', age=28, telephone='+7(967)268-14-67')),
                  Order(car='BMW', vin=25863621628214271, price=45380, max_speed=190, power=892,
                   buyer=Buyer(full_name='Лиана Алипова', age=54, telephone='+7(976)656-02-69')),
                  Order(car='Mitsubishi', vin=52876881758152844, price=39515, max_speed=166, power=703,
                   buyer=Buyer(full_name='Зиновий Денежкин', age=63, telephone='+7(984)911-01-24')),
                  Order(car='Chrysler', vin=63671096555320973, price=27021, max_speed=155, power=304,
                   buyer=Buyer(full_name='Платон Пикуль', age=21, telephone='+7(944)206-96-89')),
                  Order(car='Dacia', vin=44732864029111518, price=32949, max_speed=213, power=84,
                   buyer=Buyer(full_name='Никита Скоренко', age=50, telephone='+7(974)918-61-61')),
                  Order(car='BMW', vin=78167611258085316, price=14498, max_speed=272, power=305,
                   buyer=Buyer(full_name='Сила Иринеев', age=49, telephone='+7(996)498-45-76')),
                  Order(car='Rover', vin=71020604349825316, price=17119, max_speed=265, power=355,
                   buyer=Buyer(full_name='Айлин Ананьева', age=66, telephone='+7(998)080-27-62')),
                  Order(car='Lexus', vin=75376771787459871, price=38793, max_speed=237, power=792,
                   buyer=Buyer(full_name='Павлина Азольская', age=24, telephone='+7(970)820-18-53')),
                  Order(car='Lancia', vin=49579257767074558, price=21965, max_speed=135, power=908,
                   buyer=Buyer(full_name='Хрисанф Афросимов', age=27, telephone='+7(935)113-95-50')),
                  Order(car='Mercedes-Benz', vin=5400265038226435, price=40113, max_speed=284, power=497,
                   buyer=Buyer(full_name='Сара Евгенова', age=53, telephone='+7(940)860-67-03')),
                  Order(car='McLaren', vin=74085384620452664, price=48329, max_speed=195, power=295,
                   buyer=Buyer(full_name='Ребекка Полевая', age=50, telephone='+7(910)092-82-94')),
                  Order(car='Aston Martin', vin=70828108494998174, price=14699, max_speed=189, power=63,
                   buyer=Buyer(full_name='Виолетта Скатова', age=47, telephone='+7(908)783-56-31')),
                  Order(car='Chevrolet', vin=86522005398760522, price=31253, max_speed=254, power=472,
                   buyer=Buyer(full_name='Вавила Слюсаренко', age=26, telephone='+7(937)820-36-01')),
                  Order(car='Honda', vin=30681258325311376, price=33302, max_speed=193, power=818,
                   buyer=Buyer(full_name='Вениамин Берёзин', age=28, telephone='+7(910)076-14-71')),
                  Order(car='Morgan', vin=10989440945799935, price=46133, max_speed=90, power=456,
                   buyer=Buyer(full_name='Константин Петрушевский', age=46, telephone='+7(962)384-48-88')),
                  Order(car='Maserati', vin=21882439599048619, price=34229, max_speed=290, power=532,
                   buyer=Buyer(full_name='Марика Назарова', age=66, telephone='+7(980)391-28-59')),
                  Order(car='Mercedes-Benz', vin=6852085157642612, price=21448, max_speed=295, power=645,
                   buyer=Buyer(full_name='Владимир Соколов', age=34, telephone='+7(913)873-41-63')),
                  Order(car='KTM', vin=62888603425502214, price=42272, max_speed=273, power=35,
                   buyer=Buyer(full_name='Леона Окатова', age=51, telephone='+7(908)219-29-13')),
                  Order(car='Mercedes-Benz', vin=40236918947493819, price=30859, max_speed=246, power=948,
                   buyer=Buyer(full_name='Пахомий Лесин', age=49, telephone='+7(990)256-68-32')),
                  Order(car='Mazda', vin=56127506429262013, price=16875, max_speed=107, power=829,
                   buyer=Buyer(full_name='Лука Гиваргизов', age=64, telephone='+7(997)710-68-82')),
                  Order(car='Rolls-Royce', vin=76784972859574903, price=43536, max_speed=213, power=107,
                   buyer=Buyer(full_name='Парфений Павлов', age=24, telephone='+7(964)346-58-18')),
                  Order(car='Lamborghini', vin=2249518716467164, price=39841, max_speed=94, power=567,
                   buyer=Buyer(full_name='Руслан Римский', age=18, telephone='+7(900)309-27-26')),
                  Order(car='Ferrari', vin=46457930469348117, price=34619, max_speed=116, power=968,
                   buyer=Buyer(full_name='Климент Ягужинский', age=28, telephone='+7(951)607-22-34')),
                  Order(car='Infiniti', vin=33966304262255117, price=23690, max_speed=295, power=929,
                   buyer=Buyer(full_name='Марфа Картофельникова', age=59, telephone='+7(974)230-91-69')),
                  Order(car='Chrysler', vin=94589835907069879, price=43276, max_speed=258, power=221,
                   buyer=Buyer(full_name='Пафнутий Аврамов', age=48, telephone='+7(963)633-21-30')),
                  Order(car='Mini', vin=91051650610121691, price=42797, max_speed=123, power=370,
                   buyer=Buyer(full_name='Серафим Савостьянов', age=54, telephone='+7(910)937-71-10')),
                  Order(car='Rover', vin=25260176496274050, price=32992, max_speed=208, power=837,
                   buyer=Buyer(full_name='Вячеслав Работников', age=56, telephone='+7(933)125-57-54')),
                  Order(car='Jaguar', vin=97891670089576521, price=14678, max_speed=94, power=309,
                   buyer=Buyer(full_name='Азалия Углева', age=47, telephone='+7(962)226-19-22')),
                  Order(car='Volkswagen', vin=43018648782141299, price=35950, max_speed=263, power=393,
                   buyer=Buyer(full_name='Люсьена Бондарева', age=45, telephone='+7(933)760-91-18')),
                  Order(car='Jeep', vin=26097695043673919, price=21863, max_speed=160, power=220,
                   buyer=Buyer(full_name='Марк Карагодин', age=51, telephone='+7(904)767-54-61')),
                  Order(car='Kia', vin=49951022209620845, price=14463, max_speed=180, power=185,
                   buyer=Buyer(full_name='Пафнутий Арсеньев', age=33, telephone='+7(913)802-37-47')),
                  Order(car='Mini', vin=46178158948220088, price=47745, max_speed=110, power=743,
                   buyer=Buyer(full_name='Клара Нарицина', age=62, telephone='+7(930)200-16-51'))]

test_specification_jeep_price_48000_and_subaru_power_230_result = [
    Order(car='Subaru', vin=19419143852557674, price=49186, max_speed=265, power=841,
          buyer=Buyer(full_name='Серафима Изосимова', age=38, telephone='+7(913)093-32-60')),
    Order(car='Jeep', vin=63575861943466906, price=48178, max_speed=137, power=171,
          buyer=Buyer(full_name='Геласий Мирошников', age=29, telephone='+7(994)110-09-16')),
    Order(car='Subaru', vin=6592654160762964, price=24731, max_speed=228, power=895,
          buyer=Buyer(full_name='Роза Арбузова', age=65, telephone='+7(950)789-59-22'))]

test_specification_jeep_and_Subaru_price_10000_230_result = [
    Order(car='Subaru', vin=19419143852557674, price=49186, max_speed=265, power=841,
          buyer=Buyer(full_name='Серафима Изосимова', age=38, telephone='+7(913)093-32-60')),
    Order(car='Jeep', vin=3326129605236063, price=10180, max_speed=250, power=767,
          buyer=Buyer(full_name='Фёкла Казанцева', age=43, telephone='+7(996)171-14-50'))]

test_specification_audi_not_power_900_result = [
    Order(car='Audi', vin=1573108778233139, price=23499, max_speed=237, power=144,
          buyer=Buyer(full_name='Мавлюда Ивонова', age=29, telephone='+7(995)001-61-20')),
    Order(car='Audi', vin=40813570994967359, price=19720, max_speed=271, power=249,
          buyer=Buyer(full_name='Артемий Казимиров', age=23, telephone='+7(986)430-37-61')),
    Order(car='Audi', vin=92943043210343979, price=24896, max_speed=173, power=716,
          buyer=Buyer(full_name='Ираклий Патрикеев', age=21, telephone='+7(913)529-96-88')),
    Order(car='Audi', vin=49850764408362096, price=35825, max_speed=251, power=574,
          buyer=Buyer(full_name='Лика Багринцева', age=50, telephone='+7(960)806-99-75')),
    Order(car='Audi', vin=72329768969115621, price=48232, max_speed=162, power=943,
          buyer=Buyer(full_name='Ника Казанцева', age=56, telephone='+7(957)491-19-46'))]

test_specification_daewoo_bmw_result = [Order(car='Daewoo', vin=95056458578058897, price=28853, max_speed=199, power=26,
                                              buyer=Buyer(full_name='Аркадий Левонов', age=33,
                                                          telephone='+7(937)651-19-74'))]

test_specification_age_18_result = [Order(car='Lamborghini', vin=2249518716467164, price=39841, max_speed=94, power=567,
                                          buyer=Buyer(full_name='Руслан Римский', age=18,
                                                      telephone='+7(900)309-27-26'))]
