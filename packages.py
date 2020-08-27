import subprocess
import pydoc

try:
    py_loc=subprocess.check_output(['where', 'python']).decode("utf-8")
    conda_loc = subprocess.check_output(['where', 'conda']).decode("utf-8")
    mode:bool = 1
except subprocess.CalledProcessError:
    print("Conda wasn't found")
    mode:bool = 0

def pip_pack():
    #Parsing the pip packages
    #returns a tuple like (dictionary of pip packages, errors/weird packages)
    pip_list = {}
    err = []
    for i in subprocess.check_output(['pip', 'list']).decode("utf-8").split('\n')[2:]:
        temp=i.split()
        if len(temp) == 2 and i[0][0]!='-':
            pip_list[temp[0]]=temp[1]
        else:
            print("invalid/weird package:",temp)
            err.append(temp)
    return (pip_list,err)

def conda_pack():
    #Parsing the conda packages
    #returns a tuple like (dictionary of pip packages, errors/weird packages)
    conda_list = {}
    err = []
    for i in subprocess.check_output(['conda', 'list']).decode("utf-8").split('\n')[2:]:
        temp=i.split()
        if (i) and len(temp) == 3:
            conda_list[temp[0]]=temp[1]
        else:
            print("invalid/weird package:",temp)
            err.append(temp)
    return (conda_list,temp)

#EWW so ugly
def get_info(env,name):
    use = py_loc if env=='pip' else conda_loc
    '''
    importlib.import_module(name)
    methods = dir(name)
    i=0
    while i<len(methods):
        if not methods[i][:2]==methods[i][-2:]=='__':
            break
        i+=1
    methods=methods[i:]+methods[:i]'''
    print(use)
    print(pydoc.render_doc(name))
    return pydoc.render_doc(name).replace('\n','<br>')
if __name__=='__main__':
    print(get_info('pip','math'))