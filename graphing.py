'''
Graphing

Author: Rylan Santinon
'''
import pygal
from csv_io import CsvIo
from urlparse import urlparse

class Graphing(object):
    '''Graphs and diagrams based on retrieved data'''
    def __init__(self):
        pass

    def domain_frequency(self, topn, outpng):
        '''Make a png frequency graph for topn domains'''
        csvio = CsvIo()
        stories = csvio.get_all_stories()
        count_map = {}
        for k in stories.keys():
            count_map_key = self.canonical(stories[k][-1])
            count = count_map.get(count_map_key, 0)
            count_map[count_map_key] = count + 1
        count_list = []

        for k in count_map.keys():
            count_list.append([count_map[k], k])
        sorted_list = sorted(count_list)

        top = sorted_list[-topn:]
        top.reverse()

        count_axis = [l[0] for l in top]
        name_axis = [l[1] for l in top]

        bar_chart = pygal.Bar()
        bar_chart.x_labels = name_axis
        bar_chart.title = "Frequency of top " + str(topn) + " domains"
        bar_chart.add('Domains', count_axis)
        bar_chart.render_to_png(outpng)

    def canonical(self, url):
        '''Canonical representation of url's domain'''
        loc = urlparse(url).netloc
        if 'www.' in loc:
            return loc.split('.')[1]
        else:
            return loc

if __name__ == '__main__':
    G = Graphing()
    G.domain_frequency(10, 'frequency_bar.png')
