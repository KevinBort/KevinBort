while True:
    smallest=None
print(f'Before{smallest}')
for itervar in [1,2,3,4,5,6,7,8,9]:
    if itervar <= smallest:
        itervar=smallest
    break
print('Tu vieja')