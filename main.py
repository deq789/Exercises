import analyzer

# Exercise 1
example_urls = ['https://volgograd.masterdel.ru/master/byttehnika/', 'https://masterdel.ru/master/?p=SprinchanSU',
                'https://ekt.masterdel.ru/master/?p=ZvedeninovVV', 'https://repetitors.info/repetitor/russian/']

print('**********Exercise 1**********')
for example_url in example_urls:
    print(example_url + ' : ' + str(analyzer.get_phones_from_url(example_url)))


print('**********Exercise 2**********')
input_array = [1, 4, 7, 6, 6, 2, 8, 12, 4]
output_array = list(sorted(set(input_array), key=input_array.index))
print('input array:', str(input_array))
print('output array:', str(output_array))
