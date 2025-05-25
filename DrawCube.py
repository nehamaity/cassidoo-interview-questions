# Write a function that draws an ASCII art cube of given height n.
def draw_cube(n):
    print(" " * int(n/2 + 1) + "+" + "-" * 2 * n + "+")
    print(" " * int(n/2) + "/" + ' ' * 2 * n + "/|")

    if n > 3:
        print(" /" + ' ' * 2 * n + "/" + " " + "|")

    print("+" + "-" * 2 * n + "+" + " " * int(n/2) + "|")

    for i in range(int(n/2) - 1):
        print("|" + ' ' * (2 * n) +"|" + ' ' * int(n/2) + "|")

    print("|" + ' ' * 2 * n +"|" + " " * int(n/2) + "+")

    s = int(n/2) - 1
    for i in range(int(n/2) - 1):
        print("|" + ' ' * 2 * n +"|" + " " * s + "/")
        s -= 1

    print("|" + ' ' * 2 * n +"|" + "/")
    print("+" + "-" * 2 * n + "+")



draw_cube(2)
'''
  +----+
 /    /|
+----+ |
|    | +
|    |/
+----+
'''

draw_cube(4)
'''
   +--------+
  /        /|
 /        / |
+--------+  |
|        |  |
|        |  +
|        | /
|        |/
+--------+
'''
