from app import app
import os

# sinple block of code to check if app is running in a virtual environment
running_in_virtualemv = "VIRTUAL_ENV " in os.environ

in_venv = bool(os.environ.get("VIRTUAL_ENV"))
in_venv2 = bool(os.getenv("VIRTUAL_ENV"))


def in_virtual_env_method_one():
    print('[RUNNING IN A VIRTUAL ENVIRONMENT (method 1)] : ',in_venv )

def in_virtual_env_method_two():
    print( '[RUNNING IN A VIRTUAL ENVIRONMENT (method 2)] : ', in_venv2)



in_virtual_env_method_one()
in_virtual_env_method_two()
# end of function block

# print (in_virtual_env())

if __name__ == '__main__':
	app.run(host='192.168.43.27', port=70,debug=True) 