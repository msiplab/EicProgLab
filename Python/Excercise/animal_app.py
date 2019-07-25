from animal_factory import AnimalFactory
def main():
    names = [ 'Mouse', 'Dragon', 'Snake' ]
    for idx in range(len(names)):
        animal = AnimalFactory.create(names[idx])
        print(animal.name + ': ',end='')
        print(animal.type)

if __name__ == '__main__':
    main()
