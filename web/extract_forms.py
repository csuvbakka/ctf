import argparse
import requests
from bs4 import BeautifulSoup
from collections import namedtuple, defaultdict

Form = namedtuple('Form', ['name', 'action', 'method'])
Input = namedtuple('Input', ['name', 'type', 'value'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extracts forms and inputs from a given URL.')
    parser.add_argument('url', help='The URL to use. Example: http://github.com')

    args = parser.parse_args()

    r = requests.get(args.url)
    html = r.text

    soup = BeautifulSoup(html, 'html.parser')

    forms = defaultdict(list)
    inputs = soup.find_all('input')
    for input in inputs:
        form = input.find_parent('form')
        form_name = form.get('name', '<anonymous>')
        form_action = form.get('action', '<no action>')
        form_method = form.get('method', 'GET')

        input_name = input.get('name', '<anonymous>')
        input_type = input.get('type', '<unknown type>')
        input_value = input.get('value', '<no value>')

        forms[Form(form_name, form_action, form_method)].append(
                Input(input_name, input_type, input_value))

    for form, inputs in forms.items():
        print('{} -> {} [{}]'.format(form.name, form.action, form.method.upper()))
        max_length = max(len(i.name) for i in inputs) + 1
        for input in inputs:
            print('  {}: {} = {}'.format(input.name.ljust(max_length), input.type, input.value or '""'))
        print()
