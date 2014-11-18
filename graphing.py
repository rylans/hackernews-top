'''
Graphing

Author: Rylan Santinon
'''
import pygal
from csv_io import CsvIo
from urlparse import urlparse
import os

class Graphing(object):
    '''Graphs and diagrams based on retrieved data'''
    def __init__(self, directory):
        self.directory = directory
        self.csvio = CsvIo()
        self.make_directory()

    def make_directory(self):
        '''Make the output directory if one does not exist'''
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def output_png(self, chart, filename):
        '''Output the chart to a png file at directory/filename'''
        chart.render_to_png(os.path.join(self.directory, filename))

    def karma_by_created(self, outpng):
        FACTOR = 1.0/1000000000
        users = self.csvio.get_all_users_full()
        user_list = []
        for k in users.keys():
            user_list.append(users[k])

        karmas = []
        createds = []
        c = 0
        for u in user_list:
            c = c + 1
            if int(u[1]) > 250 and int(u[1]) < 110000:
                if c % 15 != 0:
                    continue
                karmas.append(int(u[1]))
                createds.append(int(u[2])/FACTOR)

        xychart = pygal.XY(stroke=False, x_title='Created time (seconds past epoch) x 10^-9')
        xychart.title = 'Karma vs Created time'
        xychart.add('Karma', zip(createds, karmas))

        self.output_png(xychart, outpng)

    def domain_frequency(self, topn, outpng):
        '''Make a png frequency graph for top-n domains'''
        stories = self.csvio.get_all_stories()
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
        self.output_png(bar_chart, outpng)

    def canonical(self, url):
        '''Canonical representation of url's domain'''
        loc = urlparse(url).netloc
        if 'www.' in loc:
            return loc.split('.')[1]
        else:
            return loc

if __name__ == '__main__':
    G = Graphing('diagrams')
    G.domain_frequency(10, 'frequency_bar.png')
    G.karma_by_created('karma_created.png')
