DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
    all_python_devs=[worker['name'] for worker in DATA if worker['language']=='python']
    for worker in all_python_devs:
        print(worker)
    print('*-'*32)

    all_python_devs_fm=list(filter( lambda worker: worker['language']=='python',DATA))
    all_python_devs_fm=list(map(lambda worker: worker['name'], all_python_devs_fm))
    for worker in all_python_devs_fm:
        print(worker)
    print("-*"*32)

    print("-*"*32)
    all_platzi_workers = [ worker['name'] for worker in DATA if worker['organization']=='Platzi']
    for worker in all_platzi_workers:
        print(worker)
    
    print("-*"*32)

    all_platzi_workers_fm = list(filter(lambda worker: worker['organization']=='Platzi', DATA))
    all_platzi_workers_fm = list(map(lambda worker: worker['name'], all_platzi_workers_fm))
    for worker in all_platzi_workers_fm:
        print(worker)


    adults = list(filter(lambda worker : worker['age']>=18 ,DATA))
    adults = list(map( lambda worker: worker['name'], adults))
    for worker in adults:
        print(worker)
    print("-*"*32)

    adults_lc = [worker['name'] for worker in DATA if worker['age']>=18]
    for worker in adults_lc:
        print(worker)
        
    print("-*"*32)

    old_people = list(map(lambda worker: worker | {'old': worker['age']>70}, DATA))
    for worker in old_people:
        print(worker['old'] )
    print("-*"*32)

    old_people_lc = [ worker|{'old':worker['age']>70} for worker in DATA]
    for worker in old_people_lc:
        print(worker['old'] )

if __name__== '__main__':
    main()