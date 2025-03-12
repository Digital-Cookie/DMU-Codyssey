import random

class DummySensor:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature(C)': random.randint(18, 30),
            'mars_base_external_temperature(C)': random.randint(0, 21),
            'mars_base_internal_humidity(%)': random.randint(50, 60),
            'mars_base_external_illuminance(W/m2)': random.randint(500, 715),
            'mars_base_internal_co2(%)': round(random.uniform(0.02, 0.1), 2),
            'mars_base_internal_oxygen(%)': random.randint(4, 7)
        }

    def set_env(self):
        self.env_values['mars_base_internal_temperature(C)'] = random.randint(18, 30)
        self.env_values['mars_base_external_temperature(C)'] = random.randint(0, 21)
        self.env_values['mars_base_internal_humidity(%)'] = random.randint(50, 60)
        self.env_values['mars_base_external_illuminance(W/m2)'] = random.randint(500, 715)
        self.env_values['mars_base_internal_co2(%)'] = round(random.uniform(0.02, 0.1), 2)
        self.env_values['mars_base_internal_oxygen(%)'] = random.randint(4, 7)

    def get_env(self):
        return self.env_values
    
    def save_log(self):
        with open('DummySensor.log', 'a') as file:
            file.write(str(self.env_values) + '\n')


ds = DummySensor()
ds.set_env()
print(ds.get_env())
ds.save_log()
