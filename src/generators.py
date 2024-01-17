from uuid import uuid4
from string import ascii_lowercase, ascii_uppercase
from random import choice, randint

LETTER_VALUES = dict(zip(ascii_uppercase, filter(lambda i: i % 11, range(10, 39))))


def random_string(size=10):
    return "".join(choice(ascii_lowercase + ascii_uppercase) for _ in range(size))


def random_email():
    return "".join([random_string(10), "@", random_string(7), ".com"]).lower()


def random_imei():
    imei = [randint(0, 9) for _ in range(14)]

    tmp = []

    for index, digit in enumerate(imei):
        if index % 2:
            digit = digit * 2

        tmp.extend(divmod(digit, 10))

    imei.append((sum(tmp) * 9) % 10)
    return "".join(map(str, imei))


def random_unit_number():
    number = [
        choice(ascii_uppercase),
        choice(ascii_uppercase),
        choice(ascii_uppercase),
        choice("UJZ"),
        randint(0, 9),
        randint(0, 9),
        randint(0, 9),
        randint(0, 9),
        randint(0, 9),
        randint(0, 9),
    ]

    values = list(map(lambda d: int(LETTER_VALUES.get(d, d)), number))
    checksum = sum(d * 2 ** i for i, d in enumerate(values)) % 11

    if checksum > 9:
        return random_unit_number()

    number.append(checksum)
    return "".join(map(str, number))


def random_phone():
    number = [random_phone_us(), random_phone_uk(), random_phone_cn(), random_phone_rr()]
    random_phone_method = choice(number)
    return random_phone_method


def random_phone_us():
    area_code = choice(['201', '202', '203', '205', '206', '207', '208', '209', '210', '212',
                        '213', '214', '215', '216', '217', '218', '219', '224', '225', '228',
                        '229', '231', '234', '239', '240', '248', '251', '252', '253', '254',
                        '256', '260', '262', '267', '269', '270', '276', '281', '283', '301',
                        '302', '303', '304', '305', '307', '308', '309'])
    central_office_code = randint(200, 999)
    line_number = randint(1000, 9999)
    us_phone_number = f"({area_code}) {central_office_code}-{line_number}"
    return us_phone_number


def random_phone_uk():
    area_code = choice(['20', '23', '24', '28', '29', '31', '33', '34', '37', '38', '44',
                        '45', '46', '47', '48', '49', '51', '52', '53', '56', '57', '58',
                        '59', '61', '65', '71', '72', '73', '74', '75', '76', '77', '78',
                        '79', '91', '92', '93', '117', '118', '141', '142', '143', '144',
                        '145', '146', '147', '148', '149', '150', '151', '152', '153', '154',
                        '155', '156', '157', '158', '159', '161', '162', '163', '164', '165',
                        '166', '167', '168', '169', '170', '171', '172', '173', '174', '175',
                        '176', '177', '178', '179', '180', '181', '182', '183', '190', '191'])
    subscriber_number = ''.join(choice('0123456789') for _ in range(8))
    uk_phone_number = f"({area_code}) {subscriber_number}"
    return uk_phone_number


def random_phone_cn():
    prefixes = ['130', '131', '132', '133', '134', '135', '136', '137', '138', '139',
                '150', '151', '152', '153', '155', '156', '157', '158', '159',
                '180', '181', '182', '183', '184', '185', '186', '187', '188', '189']

    prefix = choice(prefixes)
    number = ''.join(choice('0123456789') for _ in range(8))
    phone_number = prefix + number
    return phone_number


def random_phone_rr():
    first_digits = choice(['9', '8'])
    remaining_digits = ''.join(choice('0123456789') for _ in range(9))
    russian_phone_number = f"{first_digits}{remaining_digits}"
    return russian_phone_number


def random_uuid():
    return str(uuid4())
