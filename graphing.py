'''
Graphing

Author: Rylan Santinon
'''
import pygal
from csv_io import CsvIo
from urlparse import urlparse

def canonical(url):
    loc = urlparse(url).netloc
    if 'www.' in loc:
        return loc.split('.')[1]
    else:
        return loc

def main():
    csvio = CsvIo()
    stories = csvio.get_all_stories()
    count_map = {}
    for k in stories.keys():
        count_map_key = canonical(stories[k][-1])
        count = count_map.get(count_map_key, 0)
        count_map[count_map_key] = count + 1
    count_list = []

    for k in count_map.keys():
        count_list.append([count_map[k], k])
    sorted_list = sorted(count_list)

    top10 = sorted_list[-10:]
    top10.reverse()

    count_axis = [l[0] for l in top10]
    name_axis = [l[1] for l in top10]

    bar_chart = pygal.Bar()
    bar_chart.x_labels = name_axis
    bar_chart.title = "Frequency of top 10 domains"
    bar_chart.add('Domains', count_axis)
    bar_chart.render_to_file('frequency_bar.svg')

if __name__ == '__main__':
    main()
