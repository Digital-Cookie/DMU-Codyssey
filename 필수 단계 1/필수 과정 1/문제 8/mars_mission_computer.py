import random
import time
import platform
import psutil

class DummySensor:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': random.randint(18, 30),
            'mars_base_external_temperature': random.randint(0, 21),
            'mars_base_internal_humidity': random.randint(50, 60),
            'mars_base_external_illuminance': random.randint(500, 715),
            'mars_base_internal_co2': round(random.uniform(0.02, 0.1), 2),
            'mars_base_internal_oxygen': random.randint(4, 7)
        }

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = random.randint(18, 30)
        self.env_values['mars_base_external_temperature'] = random.randint(0, 21)
        self.env_values['mars_base_internal_humidity'] = random.randint(50, 60)
        self.env_values['mars_base_external_illuminance'] = random.randint(500, 715)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 2)
        self.env_values['mars_base_internal_oxygen'] = random.randint(4, 7)

    def get_env(self):
        return self.env_values
    
    def save_log(self):
        with open('DummySensor.log', 'a') as file:
            file.write(str(self.env_values) + '\n')

class MissionComputer:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': [],
            'mars_base_external_temperature': [],
            'mars_base_internal_humidity': [],
            'mars_base_external_illuminance': [],
            'mars_base_internal_co2': [],
            'mars_base_internal_oxygen': [],
        }
        self.running = True
        self.settings = self.load_settings()

    def get_sensor_data(self, sensor):
        start_time = time.time()
        try:
            while self.running:
                sensor.set_env()
                sensor_data = sensor.get_env()
                
                for i in self.env_values:
                    self.env_values[i].append(sensor_data[i])

                print(self.to_JSON(sensor_data))

                if time.time() - start_time >= 10:
                    averages = {key: round(sum(value[-2:]) / len(value[-2:]), 2) if value else 0 for key, value in self.env_values.items()}
                    print(averages)
                    start_time = time.time()

                time.sleep(5)

        except KeyboardInterrupt:
            print('\nSystem stopped....')
            self.running = False

    def get_mission_computer_info(self):
        system_info = {
            'Operating System': platform.system(),
            'OS Version': platform.version(),
            'CPU Type': platform.processor(),
            'CPU Cores': psutil.cpu_count(logical = False),
            'Memory Size': round(psutil.virtual_memory().total / (1024**3), 2),
        }
        filtered_info = {key: value for key, value in system_info.items() if self.settings.get(key, False)}
        print(self.to_JSON(filtered_info))

    def get_mission_computer_load(self):
        system_load = {
            'Current CPU Usage': psutil.cpu_percent(interval = 1),
            'Current Memory Usage': psutil.virtual_memory().percent,
        }
        filtered_info = {key: value for key, value in system_load.items() if self.settings.get(key, False)}
        print(self.to_JSON(filtered_info))

    def to_JSON(self, data):
        json_str = '{\n'
        for key, value in data.items():
            json_str += f'    "{key}": {value},\n'
        json_str = json_str.rstrip(',\n') + '\n}'
        return json_str
    
    def load_settings(self):
        settings = {
            'Operating System': True,
            'OS Version': True,
            'CPU Type': True,
            'CPU Cores': True,
            'Memory Size': True,
            'Current CPU Usage': True,
            'Current Memory Usage': True
        }
        try:
            with open('setting.txt', 'r') as file:
                for i in file:
                    key, value = i.strip().split('=')
                    settings[key] = value.lower() == "true"  
        except FileNotFoundError:
            print('setting.txt not found')
        return settings

runComputer = MissionComputer()
runComputer.get_mission_computer_info()
runComputer.get_mission_computer_load()
