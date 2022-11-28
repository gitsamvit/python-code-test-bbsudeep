cooling_type_limits = {
'PASSIVE_COOLING': {'low': 0, 'high':35 },
'HI_ACTIVE_COOLING': {'low': 0, 'high':45 },
'MED_ACTIVE_COOLING': {'low': 0, 'high':40 }
}

boundary_constants_text = {'TOO_LOW':'too low', 'TOO_HIGH':'too high', 'NORMAL': 'normal'}
boundary_constants = {'low':'TOO_LOW', 'high': 'TOO_HIGH', 'normal' : 'NORMAL'}

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return boundary_constants['low']
  if value > upperLimit:
    return boundary_constants['high']
  return boundary_constants['normal']


def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit = cooling_type_limits[coolingType]['low']
  upperLimit = cooling_type_limits[coolingType]['high']
  return infer_breach(temperatureInC, lowerLimit, upperLimit)

def send_to_controller(breachType):
  send_status_to_controller(breachType)




def send_to_console(breachType):
  send_status_to_console(breachType)


def send_to_email(breachType):
  send_status_email(breachType)


def send_status_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')
  return breachType

def send_status_email(breachType):
  recepient = "a.b@c.com"
  print(f'To: {recepient}')
  print('Hi, the temperature is {}'.format(boundary_constants_text[breachType]))
  return breachType

def send_status_to_console(breachType):
  print(breachType)
  return breachType

receiver = {
  "TO_CONTROLLER": send_to_controller,
  "TO_EMAIL" : send_to_email,
  "TO_CONSOLE" : send_to_console
}
def check_and_alert(alertTarget, coolingType, temperatureInC):
  breachType =\
    classify_temperature_breach(coolingType, temperatureInC)
  receiver[alertTarget](breachType)
  return breachType
