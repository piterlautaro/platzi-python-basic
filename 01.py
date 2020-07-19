import turtle

def main():
	window = turtle.Screen()
	colors = ['red','purple','blue','green','yellow','orange']
	t = turtle.Pen()

	make_square(t,colors)

	turtle.mainloop()

def make_square(t,colors):
	t.speed(0)

	for x in range(360):
		make_line_and_turn(x,t,colors)


def make_line_and_turn(x,t,colors):
	t.pencolor(colors[x%6])
	t.width(x/100+1)
	t.forward(x)
	t.left(59)

if __name__ == '__main__':
	main()