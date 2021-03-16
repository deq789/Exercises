import analyzer

# Exercise 1
example_urls = ['https://volgograd.masterdel.ru/master/byttehnika/', 'https://masterdel.ru/master/?p=SprinchanSU',
                'https://ekt.masterdel.ru/master/?p=ZvedeninovVV', 'https://repetitors.info/repetitor/russian/']

print('**********Exercise 1**********')
for example_url in example_urls:
    print(analyzer.get_phones_from_url(example_url))

