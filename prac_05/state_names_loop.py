STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


def main():
    for short_state in STATE_NAMES:
        print('{:<5} is {:>5}'.format(short_state, STATE_NAMES[short_state]))


main()
