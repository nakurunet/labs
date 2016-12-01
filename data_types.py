def data_type(argt):
	if type(argt) == str: #check if value is string
		return len(argt)
	if argt == None: #check if its None
		return "no value"
	if type(argt) == bool: #check if its boolean
		return argt
	if isinstance(argt,int):#check if its int
		if argt < 100: #if less than 100 return less than 100
			return "less than 100"
		elif argt > 100: #if greater than 100 return more than 100
			return "more than 100"
		return "equal to 100" #otherwise return equal to 100
	if isinstance(argt,list):#check if value is a list
		try: 
			return argt[2]#check the third element if exist and return it
		except: #if not return None
			return None