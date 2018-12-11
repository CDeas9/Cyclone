def main():
    is_type = False
    another = True
    while is_type == False:  # while the type input is not miles or km
        speed_type = str.lower(input("Do you want to input miles/hr or km/hr? (type m or k) "))
        if speed_type == "k":
            km = float(input("What is the speed in km/hr? "))
            is_type = True
            m = km/1.60934  # km/hr to miles/hr
            print("This is " + str(m) + " miles/hr.")
        elif speed_type == "m":
            m = float(input("What is the speed in m/hr? "))
            is_type = True
            km = m*1.60934  # miles/hr to km/hr
            print("This is " + str(km) + " km/hr.")
        else:
            print("Please type m or k")
    while another == True:  # while the user still wants to see another scale
        print("What scale would you like to see?")
        scale = str.lower(input("Type h for hurricane, t for typhoon, c for cyclone, or a for all. "))
        if scale == "h":
            check_lvl_hur(m)
        elif scale == "t":
            check_lvl_ty(km)
        elif scale == "c":
            check_cyc_lvl(km)
        elif scale == "a":
            check_lvl_hur(m)
            check_lvl_ty(km)
            check_cyc_lvl(km)
        else:
            print("Please type h, t, c, or a.")
        ans = str.lower(input("Would you like to see another scale? (n or y) "))
        if ans == "n":
            another = False


def check_lvl_hur(speed):
    if speed < 39:
        print("On the hurricane scale, this is a tropical depression.")
    elif 39 <= speed < 74:
        print("On the hurricane scale, this is a tropical storm.")
    elif 74 <= speed < 96:
        print("On the hurricane scale this is a category 1 hurricane.")
    elif 96 <= speed < 111:
        print("On the hurricane scale this is a category 2 hurricane.")
    elif 111 <= speed < 130:
        print("On the hurricane scale this is a category 3 hurricane.")
    elif 130 <= speed < 157:
        print("On the hurricane scale this is a category 4 hurricane.")
    elif 157 <= speed:
        print("On the hurricane scale this is a category 5 hurricane.")


def check_lvl_ty(speed):
    if speed < 63:
        print("On the typhoon scale, this is a tropical depression.")
    elif 63 <= speed < 88:
        print("On the typhoon scale, this is a tropical storm.")
    elif 88 <= speed < 118:
        print("On the typhoon scale, this is a severe tropical storm.")
    elif 118 <= speed < 150:
        print("On the typhoon scale, this is a typhoon.")
    elif 150 <= speed < 185:
        print("On the typhoon scale, this is a severe typhoon.")
    elif 185 <= speed :
        print("On the typhoon scale, this is a super typhoon.")


def check_cyc_lvl(speed):
    if speed <= 88:
        print("On the Australian scale, this is a level 1 cyclone")
    elif 88 < speed <= 117:
        print("On the Australian scale, this is a level 2 cyclone")
    elif 117 < speed <= 157:
        print("On the Australian scale, this is a level 3 cyclone")
    elif 157 < speed <= 198:
        print("On the Australian scale, this is a level 4 cyclone")
    elif 198 < speed:
        print("On the Australian scale, this is a level 5 cyclone")


main()
