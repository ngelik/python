# -*- coding: utf-8 -*-
import argparse


class Settings(object):
    def __init__(self):
        self.args = self._get_args()
        self.in_file_name = self.args['file']
        self.count = self.args['count']
        self.start_count = self.args['start_count']
        #self.template = self.args['template'] if (self.args['template'] is not None) else "%N%"
        self.template = self.args['template']
        self.file_template = self.args['file_template']
        self.file_start_counter = self.args['file_start_counter']

    def _get_args(self):
        program = {'version': '1.0.0', 'modify_date': '21.04.2014'}

        parser = argparse.ArgumentParser(description='%(prog)s, version - ' + program["version"],
                                         prog='TemplateGenerator', epilog="Good luck!")

        parser.add_argument("--file", '-f', type=str, required=True, dest='file',
                            help="File name with text", metavar='file_name')

        parser.add_argument("--template", '-t', type=str, required=False, dest='template', default="#N#",
                            help='Template for counter. Default value - N', metavar='%N%')

        parser.add_argument("--start-count", '-sc', type=int, required=False, dest='start_count', default=1,
                            help="Start counter of templates. Default value - 1", metavar='1')

        parser.add_argument("--count", '-c', type=int, required=True, dest='count',
                            help="Count of templates", metavar='123')

        parser.add_argument("--file-template", '-ft', type=str, required=False, dest='file_template',
                            help='Template for file name. If defined templates will put in different files',
                            metavar='%N%')

        parser.add_argument("--file-start-count", '-fsc', type=int, required=False,
                            dest='file_start_counter', default=1,
                            help="Start counter for file names. Default value - 1", metavar='1')

        return vars(parser.parse_args())
