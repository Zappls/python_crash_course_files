def make_shirt(text='I love Python', size='L'):
	print(f"The size of the T-shirt is {size.upper()}."
		f"\nThe text printed on the T-shirt is: {text}\n")

make_shirt()
make_shirt(size='M')
make_shirt(size='XS', text='Kinderkörper')