from tests.fixtures.dto import Order, Buyer

composit_or_and_result = [
    Order(
        car="Subaru",
        vin=19419143852557674,
        price=49186,
        max_speed=265,
        power=841,
        buyer=Buyer(full_name="Lanie Herman", age=38, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Jeep",
        vin=63575861943466906,
        price=48178,
        max_speed=137,
        power=171,
        buyer=Buyer(full_name="Cornelius Fields", age=29, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Subaru",
        vin=6592654160762964,
        price=24731,
        max_speed=228,
        power=895,
        buyer=Buyer(full_name="Frances Montoya", age=65, telephone="+7(9**)***-**-**"),
    ),
]

composit_and_or_result = [
    Order(
        car="Subaru",
        vin=19419143852557674,
        price=49186,
        max_speed=265,
        power=841,
        buyer=Buyer(full_name="Lanie Herman", age=38, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Jeep",
        vin=3326129605236063,
        price=10180,
        max_speed=250,
        power=767,
        buyer=Buyer(full_name="Rochell Rich", age=43, telephone="+7(9**)***-**-**"),
    ),
]

composit_and_not_result = [
    Order(
        car="Audi",
        vin=1573108778233139,
        price=23499,
        max_speed=237,
        power=144,
        buyer=Buyer(full_name="Olene Gomez", age=29, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Audi",
        vin=40813570994967359,
        price=19720,
        max_speed=271,
        power=249,
        buyer=Buyer(full_name="Edelmira Snider", age=23, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Audi",
        vin=92943043210343979,
        price=24896,
        max_speed=173,
        power=716,
        buyer=Buyer(full_name="Daren Morrison", age=21, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Audi",
        vin=49850764408362096,
        price=35825,
        max_speed=251,
        power=574,
        buyer=Buyer(full_name="Buster Shelton", age=50, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Audi",
        vin=72329768969115621,
        price=48232,
        max_speed=162,
        power=943,
        buyer=Buyer(full_name="Jamey Gonzalez", age=56, telephone="+7(9**)***-**-**"),
    ),
]

composit_and_or_2_result = [
    Order(
        car="Daewoo",
        vin=95056458578058897,
        price=28853,
        max_speed=199,
        power=26,
        buyer=Buyer(full_name="Chauncey Webster", age=33, telephone="+7(9**)***-**-**"),
    )
]

composit_and_or_3_result = [
    Order(
        car="Lamborghini",
        vin=2249518716467164,
        price=39841,
        max_speed=94,
        power=567,
        buyer=Buyer(full_name="Don Pierce", age=18, telephone="+7(9**)***-**-**"),
    )
]

and_eq_ge_result = [
    Order(
        car="Jeep",
        vin=63575861943466906,
        price=48178,
        max_speed=137,
        power=171,
        buyer=Buyer(full_name="Cornelius Fields", age=29, telephone="+7(9**)***-**-**"),
    )
]

and_eq_eq_result = [
    Order(
        car="Lamborghini",
        vin=2249518716467164,
        price=39841,
        max_speed=94,
        power=567,
        buyer=Buyer(full_name="Don Pierce", age=18, telephone="+7(9**)***-**-**"),
    )
]

and_eq_eq_2_result = [
    Order(
        car="Mini",
        vin=46178158948220088,
        price=47745,
        max_speed=110,
        power=743,
        buyer=Buyer(full_name="Sixta Goodman", age=62, telephone="+7(9**)***-**-**"),
    )
]

or_eq_ge_result = [
    Order(
        car="Subaru",
        vin=19419143852557674,
        price=49186,
        max_speed=265,
        power=841,
        buyer=Buyer(full_name="Lanie Herman", age=38, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Dacia",
        vin=4517077067136953,
        price=48038,
        max_speed=260,
        power=616,
        buyer=Buyer(full_name="Elois Ramsey", age=54, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Jeep",
        vin=63575861943466906,
        price=48178,
        max_speed=137,
        power=171,
        buyer=Buyer(full_name="Cornelius Fields", age=29, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Jeep",
        vin=3326129605236063,
        price=10180,
        max_speed=250,
        power=767,
        buyer=Buyer(full_name="Rochell Rich", age=43, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="SsangYong",
        vin=11775394201886094,
        price=49886,
        max_speed=197,
        power=624,
        buyer=Buyer(full_name="Kyoko Browning", age=66, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Audi",
        vin=72329768969115621,
        price=48232,
        max_speed=162,
        power=943,
        buyer=Buyer(full_name="Jamey Gonzalez", age=56, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="McLaren",
        vin=74085384620452664,
        price=48329,
        max_speed=195,
        power=295,
        buyer=Buyer(full_name="Moshe Fischer", age=50, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Jeep",
        vin=26097695043673919,
        price=21863,
        max_speed=160,
        power=220,
        buyer=Buyer(full_name="Ligia Workman", age=51, telephone="+7(9**)***-**-**"),
    ),
]

or_eq_eq_result = [
    Order(
        car="Mercedes-Benz",
        vin=68023430263724271,
        price=45454,
        max_speed=111,
        power=373,
        buyer=Buyer(full_name="Carson White", age=18, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Chrysler",
        vin=45094713610798296,
        price=36382,
        max_speed=288,
        power=986,
        buyer=Buyer(full_name="Lavelle Delgado", age=18, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Lamborghini",
        vin=2249518716467164,
        price=39841,
        max_speed=94,
        power=567,
        buyer=Buyer(full_name="Don Pierce", age=18, telephone="+7(9**)***-**-**"),
    ),
]

or_eq_eq_2_result = [
    Order(
        car="Mini",
        vin=91051650610121691,
        price=42797,
        max_speed=123,
        power=370,
        buyer=Buyer(
            full_name="Augustina Frederick", age=54, telephone="+7(9**)***-**-**"
        ),
    ),
    Order(
        car="Mini",
        vin=46178158948220088,
        price=47745,
        max_speed=110,
        power=743,
        buyer=Buyer(full_name="Sixta Goodman", age=62, telephone="+7(9**)***-**-**"),
    ),
]

not_eq_result = [
    Order(
        car="Maserati",
        vin=87451386981840811,
        price=47730,
        max_speed=168,
        power=922,
        buyer=Buyer(full_name="Golden Sampson", age=20, telephone="+7(900)000-00-00"),
    )
]

not_le_result = [
    Order(
        car="SsangYong",
        vin=11775394201886094,
        price=49886,
        max_speed=197,
        power=624,
        buyer=Buyer(full_name="Kyoko Browning", age=66, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Rover",
        vin=71020604349825316,
        price=17119,
        max_speed=265,
        power=355,
        buyer=Buyer(full_name="Javier Garrison", age=66, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Maserati",
        vin=21882439599048619,
        price=34229,
        max_speed=290,
        power=532,
        buyer=Buyer(full_name="Nathan Rodriguez", age=66, telephone="+7(9**)***-**-**"),
    ),
]

not_le_2_result = [
    Order(
        car="Maserati",
        vin=87451386981840811,
        price=47730,
        max_speed=168,
        power=922,
        buyer=Buyer(full_name="Golden Sampson", age=20, telephone="+7(900)000-00-00"),
    ),
    Order(
        car="Abarth",
        vin=83944490248983501,
        price=17336,
        max_speed=213,
        power=979,
        buyer=Buyer(full_name="Earlean Clay", age=23, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Kia",
        vin=50070971744073889,
        price=41809,
        max_speed=252,
        power=937,
        buyer=Buyer(full_name="Vern Herman", age=60, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Donkervoort",
        vin=93243716185825541,
        price=27003,
        max_speed=131,
        power=980,
        buyer=Buyer(full_name="Doria Erickson", age=41, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Chrysler",
        vin=61936340343464557,
        price=43912,
        max_speed=114,
        power=941,
        buyer=Buyer(full_name="Tisa Decker", age=56, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Audi",
        vin=72329768969115621,
        price=48232,
        max_speed=162,
        power=943,
        buyer=Buyer(full_name="Jamey Gonzalez", age=56, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Aston Martin",
        vin=99190093820726528,
        price=16789,
        max_speed=253,
        power=911,
        buyer=Buyer(full_name="Sulema Mcintosh", age=37, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Chrysler",
        vin=45094713610798296,
        price=36382,
        max_speed=288,
        power=986,
        buyer=Buyer(full_name="Lavelle Delgado", age=18, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Lancia",
        vin=49579257767074558,
        price=21965,
        max_speed=135,
        power=908,
        buyer=Buyer(full_name="Rocky Washington", age=27, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Mercedes-Benz",
        vin=40236918947493819,
        price=30859,
        max_speed=246,
        power=948,
        buyer=Buyer(full_name="Lera Webb", age=49, telephone="+7(9**)***-**-**"),
    ),
    Order(
        car="Ferrari",
        vin=46457930469348117,
        price=34619,
        max_speed=116,
        power=968,
        buyer=Buyer(
            full_name="Mariette Valenzuela", age=28, telephone="+7(9**)***-**-**"
        ),
    ),
    Order(
        car="Infiniti",
        vin=33966304262255117,
        price=23690,
        max_speed=295,
        power=929,
        buyer=Buyer(full_name="Roberto Mccall", age=59, telephone="+7(9**)***-**-**"),
    ),
]
