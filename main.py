ft = open("subtitle.txt", encoding="utf-8")
def loop_some_min():
    for x in range(0, 19):    # Up to 120 iteration run through up to 9minutes 55 second
        min_a = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]  # Pre Minutes hardcode indicator

        minute = 0                      # The minute counter adds 1 (ONE) when step (int mul) reach every 12.
        if x == 0:
            continue                    # First number of step will skip while pre. (premiere) pro start at 1.
        print(x)                        # Render the step number use for indices in pre. pro
        mul1 = 5*(x-1)
        mul2 = 5*x

        while mul1 >= 60:
            mul1 -= 60
        while mul2 >= 60:
            mul2 -= 60
            minute += 1

        # For everytime reach 60, minute counter increase by 1. And subtract itself by 60.
        # mul1, mul2 are local timer, print out timestamp for template.
        # But, in human eyes second will not count above 60, so, implement a counter to tell computer,
        # it's time to carry a number to the more significant digits

        if mul1 < 10:
            mul1 = "0"+str(mul1)
        if mul2 < 10:
            mul2 = "0"+str(mul2)

        # When mul1,2 is lower than 10, meant counted time is less than 1 minute, we don't need to carry number.

        if x == min_a[minute-1]:
            print("00:0" + str(minute-1) + ":" + str(mul1) + ",000 --> 00:0" + str(minute) + ":" + str(mul2) + ",000")
        else:
            print("00:0" + str(minute) + ":" + str(mul1) + ",000 --> 00:0" + str(minute) + ":" + str(mul2) + ",000")
        print(ft.readline())

        # Finally, a string of text will print out when placeholders defined with content.
        # There is some syntax holder inside the ("") symbol, which premiere pro use as srt files intake stream holder.

loop_some_min()   # Call above code and do their work