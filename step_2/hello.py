postition_pattern = "Lat: {} - Long: {}"


def format_position(lat, long):
    def some_function(message):
        print(message)

    some_function("test")

    # global pattern
    formatedPosition = postition_pattern.format(lat, long)
    print("abc")

    return formatedPosition


def calculate_sum(p1, p2):
    return p1 + p2


print(postition_pattern)

print(format_position(-52.33, 120.00))
