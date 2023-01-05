''' docstring '''
import requests


def shorten(url):
    ''' shorten url via cleanuri.com '''
    short_api_url = "https://cleanuri.com/api/v1/shorten"
    from_url = url
    data = {'url': from_url}
    resp = requests.post(short_api_url, data=data)
    return resp.json()['result_url']


def readfile(file):
    ''' read from file '''
    with open(file, "r") as file:
        lines = file.readlines()
    return lines


def shorten_out(lines_list):
    ''' iterates through list of urls, calls shorten '''
    out_list = []
    for urls in lines_list:
        out_list.append(shorten(urls))
    return out_list


def output_file(url_list):
    ''' writes resulting list out to file in order '''
    file = open('out_file', 'w')
    for items in url_list:
        file.writelines(f'{items}\n')
    file.close()
    print('Output file updated')


if __name__ == '__main__':
    in_list = readfile('in_file')
    outp = shorten_out(in_list)
    output_file(outp)
