from sympy import solve,symbols,simplify,expand

def parse(equation):
	equation_temp = equation.split('=')
	equation_temp[1]=simplify(equation_temp[1])
	if equation_temp[1]>0:
		equation_temp[1]=str(equation_temp[1])#bad
		equation_done='-'.join(equation_temp)
	else:
		equation_temp[1]=str(abs(equation_temp[1])) #bad
		equation_done='+'.join(equation_temp)
	return equation_done

def main(equation_done):
	x = symbols('x')
	print(solve(equation_done,x))

if __name__ == '__main__':
	equation = input()
	#equation = '13+5*x=10' #тестовый пример
	main(parse(equation))