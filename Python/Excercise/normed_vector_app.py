from normed_vector import NormedVector
def main():
    array_a = [ 1.0, 1.0 ]
    array_b = [ 2.0, 3.0 ]
    vec_a = NormedVector(array_a)
    vec_b = NormedVector(array_b)
    print('vec_a')
    display(vec_a)
    print('vec_b')
    display(vec_b)
    vec_a.add_to(vec_b)
    print('vec_a')
    display(vec_a)
    vec_b.scale_by(2.0)
    print('vec_b')
    display(vec_b)
    print('<vec_a,vec_b> = {0:5.2f}'.format(vec_a.inner_product(vec_b)))
    print('||vecA|| = {0:5.2f}'.format(vec_a.norm()))

def display(vector):
    array = vector.array
    for idx in range(len(array)):
        print('{0:5.2f}'.format(array[idx]))

if __name__ == '__main__':
    main()
