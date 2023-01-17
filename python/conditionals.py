"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    if temperature < 800 and neutrons_emitted > 500:
      if temperature * neutrons_emitted < 500000:
        return True
    return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    percentage = (generated_power / theoretical_max_power) * 100
    if percentage >= 80.0:
      return 'green'
    elif percentage < 80.0 and percentage >= 60.0:
      return 'orange'
    elif percentage < 60 and percentage >= 30:
      return 'red'
    else:
      return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    threshold_ninety_percent = (90 / 100) * threshold
    threshold_one_ten_percent = (110 / 100) * threshold

    critical_diff = threshold - threshold_ninety_percent
    print("Critical diff: ", critical_diff)
    temp_neutrons = temperature * neutrons_produced_per_second
    diff = temp_neutrons - threshold_ninety_percent

    print('90% Threshold:', threshold_ninety_percent)
    print('Temp neutrons: ', temp_neutrons)
    
    
    if diff < 0:
      diff *= -1

    print('Diff: ', diff)

    if temp_neutrons < (90 / 100) * threshold:
      return 'LOW'
    elif threshold_ninety_percent + temp_neutrons <= threshold or temp_neutrons <= threshold_one_ten_percent:
      return 'NORMAL'
    # elif diff <= critical_diff:
    #   return 'NORMAL'
    else:
      return 'DANGER'

# print(reactor_efficiency(200,50,15000))
# print(fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000))
# print(fail_safe(temperature=10, neutrons_produced_per_second=901, threshold=10000))
# print(fail_safe(temperature=10, neutrons_produced_per_second=1000, threshold=10000))
# print(fail_safe(temperature=10, neutrons_produced_per_second=1099, threshold=10000))