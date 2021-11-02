class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def create_car_tuple(make, model, color, year, mileage):
    return make, model, color, year, mileage


def create_car_list(make, model, color, year, mileage):
    return [make, model, color, year, mileage]


def create_car_dict(make, model, color, year, mileage):
    return {
        'make': make,
        'model': model,
        'color': color,
        'year': year,
        'mileage': mileage
    }


car1_tuple = create_car_tuple('Audi', 'e-tron GT', 'black', '2021', 3000)
car2_tuple_make, car2_tuple_model, car2_tuple_color, car2_tuple_year, car2_tuple_mileage = create_car_tuple('Tesla',
                                                                                                            'Model S',
                                                                                                            'red',
                                                                                                            '2020',
                                                                                                            15000)

car1_list = create_car_list('Audi', 'e-tron GT', 'black', '2021', 3000)
car2_list = create_car_list('Tesla', 'Model S', 'red', '2020', 15000)

car1_dict = create_car_dict('Audi', 'e-tron GT', 'black', '2021', 3000)
car2_dict = create_car_dict('Tesla', 'Model S', 'red', '2020', 15000)

print(f"Car 1: {Colors.OKBLUE}{car1_tuple}{Colors.ENDC} Type: {Colors.OKGREEN}{type(car1_tuple)}{Colors.ENDC}")
print(f"Car 2 Make:{Colors.OKBLUE}{car2_tuple_make}{Colors.ENDC}, Type: {Colors.OKGREEN}{type(car2_tuple_make)}{Colors.ENDC}")
print(f"Car 2 Model: {Colors.OKBLUE}{car2_tuple_model}{Colors.ENDC}, Type: {Colors.OKGREEN}{type(car2_tuple_model)}{Colors.ENDC}")
print(f"Car 2 Color: {Colors.OKBLUE}{car2_tuple_color}{Colors.ENDC}, Type: {Colors.OKGREEN}{type(car2_tuple_color)}{Colors.ENDC}")
print(f"Car 2 Year: {Colors.OKBLUE}{car2_tuple_year}{Colors.ENDC}, Type: {Colors.OKGREEN}{type(car2_tuple_year)}{Colors.ENDC}")
print(f"Car 2 Mileage: {Colors.OKBLUE}{car2_tuple_mileage}{Colors.ENDC}, Type: {Colors.OKGREEN}{type(car2_tuple_mileage)}{Colors.ENDC}")
print()
print(f"Car 1: {Colors.OKBLUE}{car1_list}{Colors.ENDC} Type: {Colors.OKGREEN}{type(car1_list)}{Colors.ENDC}")
print(f"Car 2: {Colors.OKBLUE}{car2_list}{Colors.ENDC} Type: {Colors.OKGREEN}{type(car2_list)}{Colors.ENDC}")
print()
print(f"Car 1: {Colors.OKBLUE}{car1_dict}{Colors.ENDC} Type: {Colors.OKGREEN}{type(car1_dict)}{Colors.ENDC}")
print(f"Car 2: {Colors.OKBLUE}{car2_dict}{Colors.ENDC} Type: {Colors.OKGREEN}{type(car2_dict)}{Colors.ENDC}")
