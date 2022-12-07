def add_stop(data, stops):
    index, string = [int(x) if x.isdigit() else x for x in data]
    if 0 <= index < len(stops):
        stops = stops[:index] + string + stops[index:]
    return stops


def remove_stop(data, stops):
    start_index, end_index = [int(x) for x in data]
    if 0 <= start_index <= end_index < len(stops):
        stops = stops[:start_index] + stops[end_index + 1:]
    return stops


def switch(data, stops):
    old_string, new_string = [x for x in data]
    if old_string in stops:
        stops = stops.replace(old_string, new_string)
    return stops


def main():
    stops = input()
    while True:
        commands = input()
        if "Travel" in commands:
            break
        commands, *data = commands.split(":")
        if "Add Stop" in commands:
            stops = add_stop(data, stops)
        elif "Remove Stop" in commands:
            stops = remove_stop(data, stops)
        elif "Switch" in commands:
            stops = switch(data, stops)
        print(stops)
    print(f"Ready for world tour! Planned stops: {stops}")


if __name__ == "__main__":
    main()
