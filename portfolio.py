# Amit Samra
# Portfolio

skills = {
	'proficient':['python', 'numpy', 'pandas', 'matplotlib', 'postgres', 'mysql', 'tableau', 'airflow'],
	'familiar':['r', 'mongodb', 'aws', 'kafka', 'spark']
	}

for i,j in skills.items():
    if i == 'proficient':
    	for k in j:
    		print(f"I am {i} in {k}.")
    elif i == 'familiar':
    	for k in j:
    		print(f"I am {i} with {k}.")
else:
    print("I love to code!")


